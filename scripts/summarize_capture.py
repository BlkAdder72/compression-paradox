#!/usr/bin/env python3
"""Read-only summary of stream-json captures (never modifies raw files)."""
import json,sys,glob
for f in sorted(glob.glob(sys.argv[1])):
    ev=[json.loads(l) for l in open(f,encoding='utf-8') if l.strip()]
    init=next((e for e in ev if e.get('subtype')=='init'),{})
    res=next((e for e in ev if e.get('type')=='result'),{})
    models={e['message'].get('model') for e in ev if e.get('type')=='assistant'}
    tools=[c.get('name') for e in ev if e.get('type')=='assistant' for c in e['message'].get('content',[]) if c.get('type')=='tool_use']
    user_prompt=next((c.get('text') if isinstance(c,dict) else c for e in ev if e.get('type')=='user' for c in (e['message']['content'] if isinstance(e['message']['content'],list) else [e['message']['content']])),None)
    print(f"=== {f}\ninit_model={init.get('model')} resp_models={models} tools_avail={init.get('tools')} tool_calls={tools} denials={res.get('permission_denials')} is_error={res.get('is_error')} duration_ms={res.get('duration_ms')}")
    if '--text' in sys.argv: print(res.get('result'),'\n')
