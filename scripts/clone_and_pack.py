#!/usr/bin/env python3
"""Clone the 42 upstream repositories and create a categorized source ZIP."""
import datetime, hashlib, json, pathlib, subprocess, sys, zipfile
ROOT=pathlib.Path(__file__).resolve().parents[1]
sources=json.loads((ROOT/'manifest.json').read_text())['sources']
assert len(sources)==42 and len({r['name'] for r in sources})==42
work=ROOT/'worktrees';dist=ROOT/'dist'
work.mkdir(exist_ok=True);dist.mkdir(exist_ok=True)
records=[];failures=[]
for i,r in enumerate(sources,1):
    p=work/r['category']/r['name']
    print(f"[{i}/42] {r['clone_url']}",flush=True)
    try:
        if p.exists(): raise RuntimeError(f"Directory exists: {p}")
        p.parent.mkdir(parents=True,exist_ok=True)
        subprocess.run(['git','clone','--depth','1','--no-tags',r['clone_url'],str(p)],check=True,timeout=420)
        sha=subprocess.check_output(['git','-C',str(p),'rev-parse','HEAD'],text=True).strip()
        license_files=[v.name for v in p.iterdir() if v.is_file() and v.name.lower().startswith(('license','copying','notice'))]
        records.append({**r,'status':'CLONED','commit':sha,'license_files':license_files})
    except Exception as exc:
        failures.append(r['name'])
        records.append({**r,'status':'FAILED','error':str(exc)})
provenance={'generated_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'complete':not failures,'sources':records}
(dist/'provenance.json').write_text(json.dumps(provenance,indent=2)+'\n')
if failures: sys.exit('Failed clones: '+', '.join(failures)+' (no complete source ZIP created)')
archive=dist/'ORE-MINECRAFT-sources.zip'
with zipfile.ZipFile(archive,'w',zipfile.ZIP_DEFLATED,compresslevel=6,allowZip64=True) as z:
    for file in work.rglob('*'):
        if file.is_file() and '.git' not in file.relative_to(work).parts:
            z.write(file,'ORE-MINECRAFT/categories/'+str(file.relative_to(work)))
    z.write(dist/'provenance.json','ORE-MINECRAFT/provenance.json')
    z.write(ROOT/'README.md','ORE-MINECRAFT/README.md')
print('Complete:',archive)
print('SHA256:',hashlib.sha256(archive.read_bytes()).hexdigest())
