# Acervo do Catálogo de Software Público Brasileiro

Este repositório reúne e organiza o **acervo histórico do Catálogo do Software Público Brasileiro (SPB)**, com a finalidade de preservar registros e conteúdos digitais associados aos softwares disponibilizados no antigo ambiente do SPB (https://softwarepublico.gov.br/social/search/software_infos).

O acervo é mantido como registro histórico. A presença de um software ou artefato neste repositório **não representa manutenção ativa, suporte, atualização tecnológica, validação de segurança ou recomendação para uso em ambiente de produção**.

## Acervo preservado

- **Softwares cadastrados:** 68
- **Softwares com conteúdos:** 66
- **Referências analisadas:** 465
- **Conteúdos digitais originais no inventário histórico:** 435
- **Downloads na distribuição vigente:** 431
- **Referências duplicadas:** 26
- **Referências históricas sem hash SHA-256:** 4

As referências duplicadas correspondem a diferentes registros históricos que apontam para conteúdos digitais já representados no acervo e, portanto, não resultam em novos artefatos.

As referências históricas sem hash permanecem registradas como parte do levantamento histórico, mesmo quando não foi possível associá-las a um conteúdo digital preservado identificado por SHA-256.

## Catálogo

A relação dos **66 softwares** e dos conteúdos preservados associados a cada um está disponível em:

**[Catálogo do Acervo](CATALOGO.md)**

Cada software possui um diretório próprio em `softwares/`, contendo um arquivo `METADADOS.md` com a relação dos conteúdos digitais preservados e seus respectivos SHA-256.

## Organização do repositório

```text
acervo-spb-legado/
├── README.md
├── CATALOGO.md
├── POLITICA-DO-ACERVO.md
├── SECURITY.md
└── softwares/
    ├── <software-1>/
    │   └── METADADOS.md
    ├── <software-2>/
    │   └── METADADOS.md
    └── ...
```

## Conteúdos digitais

Os conteúdos digitais preservados são tratados separadamente da documentação estrutural deste repositório.

Os artefatos digitais são disponibilizados como **assets de Releases**, evitando a inclusão de arquivos binários e de grande volume diretamente no histórico Git do repositório.

A relação entre cada conteúdo e seu respectivo software permanece registrada nos arquivos `METADADOS.md`.

## Integridade

Os SHA-256 do inventário histórico identificam os originais das bases consolidadas. Os SHA-256 da distribuição vigente identificam os downloads atuais, incluindo os derivados revisados.

## Natureza histórica do acervo

O acervo possui finalidade de **preservação e consulta histórica**.

Os conteúdos podem incluir código-fonte, pacotes e binários, arquivos compactados, documentação, scripts, cópias preservadas de repositórios, backups, conteúdos multimídia e páginas históricas relacionadas ao antigo ambiente do SPB.

A preservação de um artefato não implica que ele permaneça funcional, seguro, compatível com ambientes atuais ou adequado para implantação.

## Política do acervo

Os critérios adotados para organização, preservação e disponibilização do conteúdo são descritos em:

**[Política do Acervo](POLITICA-DO-ACERVO.md)**

## Segurança

Informações relacionadas à natureza histórica dos softwares e à comunicação de questões de segurança estão disponíveis em:

**[SECURITY.md](SECURITY.md)**

## Distribuição e integridade — atualização de 29/10/2026

O inventário histórico identifica 435 originais; a distribuição vigente contém 431 downloads em 66 Releases. Quatro conteúdos foram retirados em operação anterior. A substituição de 16 downloads por derivados revisados mantém a contagem em 431. Os nomes, tamanhos e SHA-256 vigentes estão nos metadados de cada software. Os hashes dos derivados podem diferir dos originais históricos.

As revisões são dirigidas e não constituem certificação de ausência de vulnerabilidades ou dados pessoais em todo o acervo.

As licenças que acompanham os softwares e as referências do [portal do Software Público](https://softwarepublico.dth.sisp.gov.br/) são preservadas. Não se atribui uma licença geral nova aos softwares de terceiros.
