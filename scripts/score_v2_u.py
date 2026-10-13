#!/usr/bin/env python3
"""Aggregate assessor scores for corrected official v2 and U1-U8 runs. Does not grade.

  python scripts/score_v2_u.py disagreements  -> per-set item-level disagreements
  python scripts/score_v2_u.py summary        -> unblinds adjudicated-scores.json -> evaluation/v2-u-summary.json

Every adjudicated item must equal one assessor's scores or carry an `adjudication` note.
Arithmetic and the hard cap are re-checked.
"""
import json
import sys
from itertools import combinations
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SETS = {
    'official_v2': {'dir': ROOT / 'evaluation/v2-20261013/official', 'key': 'blind_key.json'},
    'unseen_U': {'dir': ROOT / 'evaluation/unseen-20261013/scoring-U_01', 'key': 'packet/mapping.json'},
}
CATS = {'conclusion': 4, 'rules': 2, 'exceptions': 2, 'evidence': 1, 'unsupported': 1}
FIELDS = list(CATS) + ['evidence_strict', 'capped_total', 'conclusion_wrong', 'false_authorization', 'ambiguity_deduction']


def mapping(spec):
    raw = json.loads((spec['dir'] / spec['key']).read_text(encoding='utf-8'))['responses']
    return {rid: {'arm': v['arm'], 'q': v.get('q') or v.get('question')} for rid, v in raw.items()}


def load(path):
    return {s['id']: s for s in json.loads(path.read_text(encoding='utf-8'))}


def capped(s, ev='evidence'):
    t = sum(s[k] for k in CATS if k != 'evidence') + s[ev]
    return min(t, 4) if s['conclusion_wrong'] else t


def check(scores, key, label):
    assert set(scores) == set(key), f'{label}: ID set mismatch'
    for rid, s in scores.items():
        assert s['q'] == key[rid]['q'], f'{label}: question mismatch {rid}'
        assert all(type(s[k]) is int and 0 <= s[k] <= top for k, top in CATS.items()), f'{label}: range {rid}'
        assert capped(s) == s['capped_total'], f'{label}: arithmetic {rid}'


def disagreements():
    out = []
    for name, spec in SETS.items():
        key = mapping(spec)
        a1, a2 = (load(spec['dir'] / f'assessor-{i}-scores.json') for i in (1, 2))
        check(a1, key, f'{name}/a1'); check(a2, key, f'{name}/a2')
        rows = []
        for rid in sorted(a1):
            diff = {k: [a1[rid].get(k), a2[rid].get(k)] for k in FIELDS if a1[rid].get(k) != a2[rid].get(k)}
            if diff:
                rows.append({'id': rid, 'q': a1[rid]['q'], 'diff': diff, 'a1_note': a1[rid].get('note'), 'a2_note': a2[rid].get('note')})
        out.append({'set': name, 'assessor_totals': [sum(s['capped_total'] for s in a.values()) for a in (a1, a2)],
                    'items_disagreeing': len(rows), 'rows': rows})
    print(json.dumps(out, indent=1))


def summary():
    out = {}
    for name, spec in SETS.items():
        key = mapping(spec)
        adj = load(spec['dir'] / 'adjudicated-scores.json')
        a1, a2 = (load(spec['dir'] / f'assessor-{i}-scores.json') for i in (1, 2))
        check(adj, key, f'{name}/adjudicated')
        for rid, s in adj.items():
            same = any(all(s.get(k) == a[rid].get(k) for k in FIELDS) for a in (a1, a2))
            assert same or s.get('adjudication'), f'{name}: {rid} changed without adjudication note'
        by_arm = {}
        for rid, s in adj.items():
            by_arm.setdefault(key[rid]['arm'], {})[key[rid]['q']] = s
        totals = lambda a: {arm: sum(a[r]['capped_total'] for r in a if key[r]['arm'] == arm) for arm in sorted(by_arm)}
        rep = {'assessor_1_totals': totals(a1), 'assessor_2_totals': totals(a2), 'arms': {}, 'pairwise': {}}
        for arm, qs in sorted(by_arm.items()):
            order = sorted(qs, key=lambda q: int(q[1:]))
            rep['arms'][arm] = {
                'total': sum(qs[q]['capped_total'] for q in order),
                'total_strict_evidence': sum(capped(qs[q], 'evidence_strict') for q in order),
                'per_question': {q: qs[q]['capped_total'] for q in order},
                'categories': {q: {k: qs[q][k] for k in list(CATS) + ['evidence_strict']} for q in order},
                'correct_conclusions': sum(not qs[q]['conclusion_wrong'] for q in order),
                'false_authorizations': [q for q in order if qs[q]['false_authorization']],
                'critical_omissions': {q: qs[q].get('critical_omissions') or qs[q].get('critical_omission') for q in order
                                       if qs[q].get('critical_omissions') or qs[q].get('critical_omission')},
                'ambiguity_deductions': {q: qs[q].get('ambiguity_deduction', 0) for q in order if qs[q].get('ambiguity_deduction')},
                'transparent_uncertainty': [q for q in order if qs[q].get('transparent_uncertainty')],
            }
        for x, y in combinations(sorted(by_arm), 2):
            w = sum(by_arm[x][q]['capped_total'] > by_arm[y][q]['capped_total'] for q in by_arm[x])
            l = sum(by_arm[x][q]['capped_total'] < by_arm[y][q]['capped_total'] for q in by_arm[x])
            rep['pairwise'][f'{x} vs {y}'] = {'wins': w, 'ties': len(by_arm[x]) - w - l, 'losses': l}
        out[name] = rep
    (ROOT / 'evaluation/v2-u-summary.json').write_text(json.dumps(out, indent=1) + '\n', encoding='utf-8', newline='\n')
    print(json.dumps(out, indent=1))


if __name__ == '__main__':
    {'disagreements': disagreements, 'summary': summary}[sys.argv[1]]()
