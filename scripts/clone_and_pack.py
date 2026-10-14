#!/usr/bin/env python3
"""Source snapshot archiver: Regolith Labs (42), HardhatChad (25), Blueshift (102).
Clones fresh heads with shallow history; records hashes; leaves upstream licenses intact.
"""
import argparse, datetime, hashlib, json, os, pathlib, subprocess, sys, zipfile
ROOT=pathlib.Path(__file__).resolve().parents[1]
p=argparse.ArgumentParser()
p.add_argument('--collections',nargs='+',choices=['regolith','hardhat','blueshift'],default=['regolith','hardhat','blueshift'])
p.add_argument('--include-large',action='store_true',help='Include repositories >200000 KB (potentially multi-GB)')
p.add_argument('--max-repos',type=int,default=0,help='Optional limit for smoke tests')
args=p.parse_args()
mapping={'regolith':'manifest.json','hardhat':'hardhatchad-manifest.json','blueshift':'blueshift-manifest.json'}
sources=[]
for collection in args.collections:
 for r in json.loads((ROOT/mapping[collection]).read_text())['sources']:
  sources.append({**r,'collection':collection})
if args.max_repos:sources=sources[:args.max_repos]
work=ROOT/'worktrees';dist=ROOT/'dist'
work.mkdir(exist_ok=True);dist.mkdir(exist_ok=True)
records=[];failures=[]
for i,r in enumerate(sources,1):
 if r.get('large_upstream') and not args.include_large:
  records.append({**r,'status':'SKIPPED_LARGE','reason':'Use --include-large'});continue
 path=work/r['collection']/r['category']/r['name']
 print(f"[{i}/{len(sources)}] {r['clone_url']}",flush=True)
 try:
  if path.exists(): raise RuntimeError('Path already exists: '+str(path))
  path.parent.mkdir(parents=True,exist_ok=True)
  subprocess.run(['git','clone','--depth=1','--no-tags',r['clone_url'],str(path)],check=True,timeout=420)
  sha=subprocess.check_output(['git','-C',str(path),'rev-parse','HEAD'],text=True).strip()
  licenses=[x.name for x in path.iterdir() if x.is_file() and x.name.lower().startswith(('license','copying','notice'))]
  records.append({**r,'status':'CLONED','commit':sha,'license_files':licenses})
 except Exception as e:
  failures.append(r['collection']+'/'+r['name'])
  records.append({**r,'status':'FAILED','error':str(e)})
dist.joinpath('provenance.json').write_text(json.dumps({'created_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'sources':records},indent=2)+'\n')
if failures:sys.exit('FAILED: '+', '.join(failures))
archive=dist/'ORE-MINECRAFT-sources.zip'
with zipfile.ZipFile(archive,'w',zipfile.ZIP_DEFLATED,compresslevel=6,allowZip64=True) as z:
 for file in work.rglob('*'):
  if file.is_file() and '.git' not in file.relative_to(work).parts:
   z.write(file,'ORE-MINECRAFT/sources/'+str(file.relative_to(work)))
 z.write(dist/'provenance.json','ORE-MINECRAFT/provenance.json')
 z.write(ROOT/'README.md','ORE-MINECRAFT/README.md')
print('ZIP:',archive,'size:',archive.stat().st_size,'SHA256:',hashlib.file_digest(open(archive,'rb'),'sha256').hexdigest())
