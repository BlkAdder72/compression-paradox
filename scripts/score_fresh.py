#!/usr/bin/env python3
"""Aggregate the 2026-10-13 fresh-run assessor scores. Does not grade.

Usage:
  python scripts/score_fresh.py disagreements   # list item-level assessor disagreements
  python scripts/score_fresh.py summary         # unblind adjudicated scores -> summary.json

`adjudicated-scores.json` (one per set) is written by the adjudicator. Every item must
equal one assessor's item or carry an `adjudication` note. Arithmetic and the hard cap
are re-checked here.
"""
import json
import sys
from itertools import combinations
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
BASE = ROOT / 'evaluation' / 'fresh-20261013'
CATS = {'conclusion': 4, 'rules': 2, 'exceptions': 2, 'evidence': 1, 'unsupported': 1}
FLAGS = ['conclusion_wrong', 'false_authorization']


def load(path):
    return {s['id']: s for s in json.loads(path.read_text(encoding='utf-8'))}


def capped(s, evidence_key='evidence'):
    total = sum(s[k] for k in CATS if k != 'evidence') + s[evidence_key]
    return min(total, 4) if s['conclusion_wrong'] else total


def check(scores, key, label):
    assert set(scores) == set(key['responses']), f'{label}: ID set mismatch'
    for rid, s in scores.items():
        assert s['q'] == key['responses'][rid]['q'], f'{label}: question mismatch {rid}'
        assert all(type(s[k]) is int and 0 <= s[k] <= top for k, top in CATS.items()), f'{label}: range {rid}'
        assert capped(s) == s['capped_total'], f'{label}: arithmetic {rid}'


def disagreements():
    for name in ('official', 'holdout'):
        key = json.loads((BASE / name / 'blind_key.json').read_text(encoding='utf-8'))
        a1, a2 = (load(BASE / name / f'assessor-{i}-scores.json') for i in (1, 2))
        check(a1, key, f'{name}/a1'); check(a2, key, f'{name}/a2')
        rows = []
        for rid in sorted(a1):
            diff = {k: (a1[rid][k], a2[rid][k]) for k in list(CATS) + ['evidence_strict', 'capped_total'] + FLAGS if a1[rid].get(k) != a2[rid].get(k)}
            if diff:
                rows.append({'id': rid, 'q': a1[rid]['q'], 'diff': diff, 'a1_note': a1[rid]['note'], 'a2_note': a2[rid]['note']})
        t1 = sum(s['capped_total'] for s in a1.values()); t2 = sum(s['capped_total'] for s in a2.values())
        print(json.dumps({'set': name, 'assessor_totals': [t1, t2], 'items_disagreeing': len(rows), 'rows': rows}, indent=1))


def summary():
    out = {}
    for name in ('official', 'holdout'):
        key = json.loads((BASE / name / 'blind_key.json').read_text(encoding='utf-8'))
        adj = load(BASE / name / 'adjudicated-scores.json')
        check(adj, key, f'{name}/adjudicated')
        a1, a2 = (load(BASE / name / f'assessor-{i}-scores.json') for i in (1, 2))
        for rid, s in adj.items():
            assert s in (a1[rid], a2[rid]) or s.get('adjudication'), f'{name}: {rid} adjudicated without note'
        arms = {}
        for rid, s in adj.items():
            r = key['responses'][rid]
            arms.setdefault(r['arm'], {})[r['q']] = s
        def per_arm(scores_by_id):
            res = {}
            for rid, s in scores_by_id.items():
                r = key['responses'][rid]
                res.setdefault(r['arm'], 0)
                res[r['arm']] += s['capped_total']
            return res
        rep = {'run_ids': key['runs'], 'assessor_1_totals': per_arm(a1), 'assessor_2_totals': per_arm(a2), 'arms': {}, 'pairwise': {}}
        for arm, qs in sorted(arms.items()):
            order = sorted(qs, key=lambda q: int(q[1:]))
            rep['arms'][arm] = {
                'run_id': key['runs'][arm],
                'total': sum(qs[q]['capped_total'] for q in order),
                'total_strict_evidence': sum(capped(qs[q], 'evidence_strict') for q in order),
                'per_question': {q: qs[q]['capped_total'] for q in order},
                'categories': {q: {k: qs[q][k] for k in list(CATS) + ['evidence_strict']} for q in order},
                'correct_conclusions': sum(not qs[q]['conclusion_wrong'] for q in order),
                'false_authorizations': [q for q in order if qs[q]['false_authorization']],
                'critical_omissions': {q: qs[q]['critical_omission'] for q in order if qs[q].get('critical_omission')},
                'transparent_uncertainty': [q for q in order if qs[q].get('transparent_uncertainty')],
            }
        for x, y in combinations(sorted(arms), 2):
            w = sum(arms[x][q]['capped_total'] > arms[y][q]['capped_total'] for q in arms[x])
            l = sum(arms[x][q]['capped_total'] < arms[y][q]['capped_total'] for q in arms[x])
            rep['pairwise'][f'{x} vs {y}'] = {'wins': w, 'ties': len(arms[x]) - w - l, 'losses': l}
        out[name] = rep
    (BASE / 'summary.json').write_text(json.dumps(out, indent=1) + '\n', encoding='utf-8', newline='\n')
    print(json.dumps(out, indent=1))


if __name__ == '__main__':
    {'disagreements': disagreements, 'summary': summary}[sys.argv[1]]()
