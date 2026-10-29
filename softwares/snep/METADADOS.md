# SNEP

## Distribuição vigente

3 download(s) na Release correspondente. Esta seção e o inventário da raiz identificam a distribuição vigente; as anotações históricas abaixo registram situações anteriores.

| Arquivo / download | ID do asset | Bytes | SHA-256 |
|---|---:|---:|---|
| [manual-instalacao-snep-20.pdf](https://github.com/spbgovbr/acervo-spb-legado/releases/download/acervo-snep/manual-instalacao-snep-20.pdf) | 521351239 | 451678 | `f883ae987b4c2737c6977dce4f808c555636581c77e8f063a500cc71827c0d11` |
| [snep-2.0-rc1-rev-acervo-20261028-r1.tar.gz](https://github.com/spbgovbr/acervo-spb-legado/releases/download/acervo-snep/snep-2.0-rc1-rev-acervo-20261028-r1.tar.gz) | 685094838 | 15284920 | `d237143f1e89f5521d72e29c343f1e440f59ddb35a3a6eb8231a710b882002fb` |
| [versoes.html](https://github.com/spbgovbr/acervo-spb-legado/releases/download/acervo-snep/versoes.html) | 521351370 | 31533 | `d2b4ee37b03079ea7caabe4f489b14761560cbea9845375293aeac4dc09f02b1` |

Os originais de referência histórica são preservados separadamente. Um derivado revisado não constitui versão mantida ou homologação de segurança.

<details>
<summary>Inventário histórico e anotações anteriores — situações à época</summary>

# SNEP

## Identificação

**Software:** SNEP

**Situação:** Acervo histórico do Software Público Brasileiro.

**Manutenção:** O conteúdo deste diretório não representa uma versão atualmente mantida ou suportada pelo repositório.

## Conteúdos preservados

Foram identificados **3 conteúdo(s) digital(is) preservado(s)** associado(s) a este software.

| Arquivo | Tipo de artefato | SHA-256 |
|---|---|---|
| `manual-instalacao-snep-20.pdf` | Documentação | `f883ae987b4c2737c6977dce4f808c555636581c77e8f063a500cc71827c0d11` |
| `snep-2.0-rc1.tar.gz` | Arquivo compactado | `b54d8694c97b2b903c92651e1e1faf564eddbb16e7d069f9b2fe29d6e11686ee` |
| `versoes.html` | Conteúdo histórico | `d2b4ee37b03079ea7caabe4f489b14761560cbea9845375293aeac4dc09f02b1` |

## Versão revisada adicional ao inventário histórico

- Nome do arquivo: `snep-2.0-rc1-rev-acervo-20261028-r1.tar.gz`
- SHA-256: `d237143f1e89f5521d72e29c343f1e440f59ddb35a3a6eb8231a710b882002fb`
- Tamanho: 15284920 bytes
- Download: https://github.com/spbgovbr/acervo-spb-legado/releases/download/acervo-snep/snep-2.0-rc1-rev-acervo-20261028-r1.tar.gz
- Situação: disponível via GitHub Releases
- Data da publicação: 2026-10-28
- Observação: versão revisada para disponibilização no acervo, em substituição ao arquivo anteriormente distribuído.
- Limitação: requer configuração própria de banco e AMI conforme `SANITIZACAO.md`; instalação, atualização, desinstalação, backup e telefonia não verificados funcionalmente.

## Histórico de distribuição

O inventário acima identifica o original histórico. A substituição desta operação refere-se ao derivado intermediário abaixo, distribuído anteriormente sob o mesmo nome, mas com SHA-256 diferente do original catalogado.

- Nome do derivado intermediário: `snep-2.0-rc1.tar.gz`
- SHA-256 do derivado intermediário: `bebedc3197e39345ad79e9cba4a0ffd90e9d8fcbfe7638c90947c122795e4edc`
- Situação: removido da distribuição via GitHub Releases
- Data da retirada: 2026-10-28
- Motivo: incompatibilidade com os critérios de distribuição do acervo
- Substituto publicado: `snep-2.0-rc1-rev-acervo-20261028-r1.tar.gz`
- SHA-256 do substituto: `d237143f1e89f5521d72e29c343f1e440f59ddb35a3a6eb8231a710b882002fb`

## Aviso

Este registro integra o acervo histórico do Software Público Brasileiro. A preservação e a disponibilização do conteúdo não representam validação atual de segurança, compatibilidade, manutenção, atualização tecnológica ou adequação para uso em ambiente de produção.

## Versão revisada adicional ao inventário histórico

| Campo | Informação |
|---|---|
| Arquivo | `snep-2.0-rc1-sanitizado.tar.gz` |
| SHA-256 | `BEBEDC3197E39345AD79E9CBA4A0FFD90E9D8FCBFE7638C90947C122795E4EDC` |
| Situação | Versão sanitizada publicada no GitHub Releases |
| Observação | Artefato revisado para remoção de credenciais e segredos embutidos. |
| Validação | Integridade do arquivo compactado verificada; instalação e funcionamento completo não testados. |

### Alterações de sanitização

- Substituição de senhas de banco de dados embutidas pelo marcador `CHANGE_ME_DB_PASSWORD`.
- Substituição do segredo AMI embutido pelo marcador `CHANGE_ME_AMI_SECRET`.
- Ajustes nos scripts de instalação e backup para utilizar variáveis de ambiente e arquivos temporários de configuração, evitando a exposição de credenciais nos argumentos de linha de comando.
- Atualização da documentação HTML gerada e inclusão do arquivo `SANITIZACAO.md`.

**Atenção:** os marcadores de configuração devem ser substituídos por valores adequados antes da implantação.

## Retiradas da distribuição

| Campo | Informação |
|---|---|
| Arquivo original | `snep-2.0-rc1.tar.gz` |
| SHA-256 original | `B54D8694C97B2B903C92651E1E1FAF564EDDBB16E7D069F9B2FE29D6E11686EE` |
| Situação | Removido do GitHub Releases |
| Motivo | Substituição pela versão sanitizada |
| Arquivo substituto | `snep-2.0-rc1-sanitizado.tar.gz` |
| SHA-256 do substituto | `BEBEDC3197E39345AD79E9CBA4A0FFD90E9D8FCBFE7638C90947C122795E4EDC` |
| Data da retirada | Não informada |

</details>
