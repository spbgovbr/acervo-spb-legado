# Integridade da distribuição

O arquivo `INVENTARIO-DISTRIBUICAO.json` identifica todos os downloads vigentes por Release, nome, ID, tamanho e SHA-256. O histórico original é preservado nos metadados; ele não é uma lista de downloads atualmente disponíveis.

Para conferir a estrutura do inventário: `python3 scripts/verificar_integridade.py`.

Para comparar nomes, IDs, tamanhos e digests fornecidos pelo GitHub: `python3 scripts/verificar_integridade.py --remoto spbgovbr/acervo-spb-legado`. Em repositório privado, fornecer autenticação de leitura em `GH_TOKEN`, sem gravá-la no repositório ou em logs.

Para conferir bytes baixados independentemente: organizar os arquivos em `<diretorio>/<release_tag>/<arquivo>` e executar `python3 scripts/verificar_integridade.py --diretorio <diretorio>`.

A rotina retorna falha para arquivos ausentes, não inventariados ou divergentes. A comparação remota usa os digests informados pelo GitHub; a conferência dos bytes locais calcula o SHA-256 independentemente. Nenhuma dessas verificações executa ou instala os pacotes ou comprova segurança funcional.

O workflow de integridade usa somente permissão de leitura. Alterações legítimas nas Releases exigem atualização coordenada do inventário e dos metadados. Durante uma substituição coordenada, o workflow pode apontar a transição até o fechamento da operação.
