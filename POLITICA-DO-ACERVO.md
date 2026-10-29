# Política de Preservação e Organização do Acervo

## 1. Finalidade

Esta política estabelece os critérios adotados para preservação, organização, identificação e disponibilização do acervo histórico do Catálogo do Software Público Brasileiro (SPB).

O acervo tem finalidade histórica e de preservação digital. Sua disponibilização busca manter acessíveis registros e conteúdos associados aos softwares anteriormente disponibilizados no ambiente do SPB.

A presença de um software ou artefato neste acervo não representa manutenção ativa, suporte, atualização tecnológica, validação de segurança ou recomendação para uso em ambiente de produção.

## 2. Escopo do acervo

O levantamento consolidado compreende:

- **68 softwares cadastrados**;
- **66 softwares com conteúdos preservados:**;
- **465 referências analisadas**;
- **435 conteúdos digitais únicos preservados**;
- **26 referências duplicadas**;
- **4 referências históricas sem hash SHA-256 registrado**.

Os quantitativos refletem a consolidação realizada para organização do acervo histórico.

## 3. Princípios de preservação

A organização do acervo observa os seguintes princípios:

- preservação integral dos arquivos efetivamente recuperados e incorporados ao acervo;
- manutenção da rastreabilidade dos conteúdos preservados;
- não exclusão de arquivos em razão de duplicidade;
- identificação lógica de conteúdos duplicados por SHA-256;
- não criação de informações técnicas sem evidência nas bases consolidadas;
- manutenção do caráter histórico dos conteúdos;
- transparência quanto às limitações do acervo.

## 4. Acervo original preservado

Os conteúdos recuperados foram preservados em sua forma original durante o processo de consolidação do acervo.

As operações de organização, classificação e preparação para publicação no GitHub foram realizadas com base nos registros consolidados do acervo.

## 5. Identificação por SHA-256

O SHA-256 é utilizado como identificador técnico dos conteúdos digitais preservados e como mecanismo auxiliar de verificação de integridade.

Os 435 valores SHA-256 do inventário histórico original correspondem aos valores constantes das bases consolidadas do antigo ambiente web do SPB.

Esses valores foram conferidos entre as bases consolidadas antes da geração dos metadados do repositório.

O registro de um valor SHA-256 não constitui certificação de autenticidade, segurança, funcionamento ou ausência de código malicioso.

## 6. Referências duplicadas

Das 465 referências analisadas, **26 correspondem a referências duplicadas**.

Uma referência duplicada ocorre quando diferentes registros históricos estão associados a um conteúdo digital já identificado pelo mesmo SHA-256.

A duplicidade é tratada de forma lógica.

Assim:

- a referência histórica permanece registrada;
- o conteúdo não é contado novamente como novo conteúdo digital;
- arquivos preservados no acervo original não são excluídos em razão da duplicidade;

Dessa forma, as 26 referências duplicadas integram o levantamento histórico.

## 7. Referências históricas sem SHA-256

Foram identificadas **4 referências históricas sem SHA-256 registrado**.

Essas referências permanecem registradas por integrarem o levantamento histórico do SPB.

Não foram atribuídos valores substitutivos aos registros para os quais não havia SHA-256 nas bases consolidadas.

A ausência de SHA-256 indica apenas que a referência não dispõe desse identificador nas bases utilizadas para consolidação do acervo. Isso não significa, necessariamente, que o respectivo software não possua outros conteúdos preservados.

## 8. Associação entre softwares e conteúdos

Cada conteúdo digital preservado é associado ao software correspondente conforme os registros consolidados do acervo.

A base utilizada para organização da publicação contém os seguintes campos:

- software;
- arquivo;
- tipo de artefato;
- SHA-256.

Cada software possui um arquivo `METADADOS.md` próprio com a relação dos conteúdos preservados associados a ele.

## 9. Classificação dos artefatos

Os conteúdos foram organizados em categorias descritivas destinadas a facilitar a consulta ao acervo.

A classificação possui finalidade organizacional e não constitui avaliação sobre qualidade, segurança, funcionamento ou atualidade do conteúdo.

## 10. Conteúdos históricos de páginas

Determinados conteúdos preservados correspondem a páginas, respostas ou outros registros do antigo ambiente web do SPB.

Esses conteúdos são classificados como **conteúdo histórico** quando sua natureza puder ser determinada a partir das evidências registradas no acervo.

Sua preservação tem finalidade documental e não implica que o conteúdo represente um artefato executável ou uma versão utilizável do software.

## 11. Publicação no GitHub
A estrutura principal do repositório contém a documentação e os metadados do acervo:

acervo-spb-legado/
├── README.md
├── CATALOGO.md
├── POLITICA-DO-ACERVO.md
├── SECURITY.md
└── softwares/
    └── <software>/
        └── METADADOS.md

Os arquivos digitais preservados são disponibilizados por meio das Releases do GitHub, conforme a organização definida para cada software. Os respectivos arquivos METADADOS.md apresentam as informações de identificação e associação dos conteúdos.

## Distribuição e integridade — atualização de 29/10/2026

O inventário histórico identifica 435 originais; a distribuição vigente contém 431 downloads em 66 Releases. Quatro conteúdos foram retirados em operação anterior. A substituição de 16 downloads por derivados revisados mantém a contagem em 431. Os nomes, tamanhos e SHA-256 vigentes estão em [INVENTARIO-DISTRIBUICAO.json](INVENTARIO-DISTRIBUICAO.json) e nos metadados de cada software. Os hashes dos derivados podem diferir dos originais históricos.

A conferência de integridade é descrita em [INTEGRIDADE.md](INTEGRIDADE.md). As revisões são dirigidas e não constituem certificação de ausência de vulnerabilidades ou dados pessoais em todo o acervo.

As licenças que acompanham os softwares e as referências do [portal do Software Público](https://softwarepublico.dth.sisp.gov.br/) são preservadas. Não se atribui uma licença geral nova aos softwares de terceiros.
