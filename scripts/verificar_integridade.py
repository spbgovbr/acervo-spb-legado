"""Conferencia do inventario de distribuicao; nao executa os pacotes."""
import argparse,hashlib,json,os,pathlib,re,sys,urllib.request

def validar(entries,require_ids=True):
    pairs=set();ids=set()
    for a in entries:
        pair=(a['release_tag'],a['arquivo'])
        if pair in pairs:raise ValueError('Arquivo duplicado no inventario')
        pairs.add(pair)
        if not re.fullmatch(r'sha256:[0-9a-f]{64}',a['digest']):raise ValueError('SHA-256 invalido')
        if not isinstance(a['bytes'],int) or a['bytes']<0:raise ValueError('Tamanho invalido')
        aid=a.get('asset_id')
        if require_ids and not isinstance(aid,int):raise ValueError('ID de publicacao pendente')
        if aid is not None:
            if aid in ids:raise ValueError('ID duplicado')
            ids.add(aid)
    return pairs

def verificar_arquivo(a,path):
    h=hashlib.sha256();size=0
    with open(path,'rb') as f:
        for b in iter(lambda:f.read(4*1024*1024),b''):h.update(b);size+=len(b)
    return size==a['bytes'] and 'sha256:'+h.hexdigest()==a['digest']

def ler_metadados(root):
    entries=[]
    for path in sorted((pathlib.Path(root)/'softwares').glob('*/METADADOS.md')):
        current=path.read_text(encoding='utf-8-sig').split('<details>',1)[0]
        for line in current.splitlines():
            if not line.startswith('| ['):continue
            match=re.fullmatch(r'\| \[([^\]]+)\]\((https://github\.com/spbgovbr/acervo-spb-legado/releases/download/([^/]+)/[^)]+)\) \| (\d+) \| (\d+) \| `([0-9a-f]{64})` \|',line)
            if not match:raise ValueError('Linha de distribuicao invalida: '+str(path))
            name,url,tag,aid,size,digest=match.groups()
            if tag!='acervo-'+path.parent.name:raise ValueError('Release incoerente com software')
            entries.append(dict(arquivo=name,url=url,release_tag=tag,asset_id=int(aid),bytes=int(size),digest='sha256:'+digest))
    if not entries:raise ValueError('Nenhum download nos metadados')
    return entries

def remoto(repo):
    def api(path):
        headers={'Accept':'application/vnd.github+json','User-Agent':'acervo-integridade'}
        if os.environ.get('GH_TOKEN'):headers['Authorization']='Bearer '+os.environ['GH_TOKEN']
        with urllib.request.urlopen(urllib.request.Request('https://api.github.com/repos/'+repo+'/'+path,headers=headers),timeout=90) as r:return json.load(r)
    def pages(path):
        page=1;out=[]
        while True:
            rows=api(path+('?page=' if '?' not in path else '&page=')+str(page)+'&per_page=100');out.extend(rows)
            if len(rows)<100:return out
            page+=1
    out=[]
    for r in pages('releases'):
        if r['draft']:continue
        for a in pages('releases/'+str(r['id'])+'/assets'):
            if a['state']!='uploaded':raise ValueError('Asset nao esta uploaded')
            out.append(dict(release_tag=r['tag_name'],arquivo=a['name'],asset_id=a['id'],digest=a.get('digest'),bytes=a['size']))
    return out

def comparar(expected,actual):
    e={(a['release_tag'],a['arquivo']):a for a in expected};r={(a['release_tag'],a['arquivo']):a for a in actual}
    errors=[]
    for k in e.keys()-r.keys():errors.append('Ausente: '+str(k))
    for k in r.keys()-e.keys():errors.append('Nao inventariado: '+str(k))
    for k in e.keys()&r.keys():
        for field in ['asset_id','digest','bytes']:
            if e[k].get(field)!=r[k].get(field):errors.append('Divergencia '+field+': '+str(k))
    return sorted(errors)

def main():
    p=argparse.ArgumentParser();p.add_argument('--inventario',help='Inventario JSON externo opcional; por padrao utiliza os METADADOS.md');p.add_argument('--remoto');p.add_argument('--diretorio');args=p.parse_args()
    entries=json.loads(pathlib.Path(args.inventario).read_text(encoding='utf-8'))['assets'] if args.inventario else ler_metadados(pathlib.Path(__file__).resolve().parents[1]);validar(entries);errors=[]
    if args.remoto:errors.extend(comparar(entries,remoto(args.remoto)))
    if args.diretorio:
        for a in entries:
            path=pathlib.Path(args.diretorio)/a['release_tag']/a['arquivo']
            if not path.is_file() or not verificar_arquivo(a,path):errors.append('Arquivo local divergente ou ausente: '+a['arquivo'])
    if errors:
        for error in errors:print(error)
        return 1
    print(str(len(entries))+' registros conferidos'+('; metadados remotos correspondem' if args.remoto else '')+'. Digests remotos nao substituem conferencia independente dos bytes baixados.')
    return 0
if __name__=='__main__':sys.exit(main())
