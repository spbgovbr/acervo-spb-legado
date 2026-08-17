# Política de Preservação e Organização do Acervo

## 1. Finalidade

Esta política estabelece os critérios adotados para preservação, organização, identificação e disponibilização do acervo histórico do Catálogo do Software Público Brasileiro (SPB).

O acervo tem finalidade histórica e de preservação digital. Sua disponibilização busca manter acessíveis registros e conteúdos associados aos softwares anteriormente disponibilizados no ambiente do SPB.

A presença de um software ou artefato neste acervo não representa manutenção ativa, suporte, atualização tecnológica, validação de segurança ou recomendação para uso em ambiente de produção.

## 2. Escopo do acervo

O levantamento consolidado compreende:

- **68 softwares cadastrados**;
- **465 referências analisadas**;
- **435 conteúdos digitais únicos preservados**;
- **26 referências duplicadas**;
- **4 referências históricas sem hash SHA-256**.

Os quantitativos refletem a consolidação realizada para organização do acervo histórico.

## 3. Princípios de preservação

A organização do acervo observa os seguintes princípios:

- preservação integral dos conteúdos coletados;
- manutenção da rastreabilidade dos conteúdos preservados;
- não exclusão de arquivos em razão de duplicidade;
- identificação lógica de conteúdos duplicados por SHA-256;
- não criação de informações técnicas sem evidência nas bases consolidadas;
- manutenção do caráter histórico dos conteúdos;
- transparência quanto às limitações do acervo.

## 4. Acervo original preservado

O diretório de quarentena utilizado durante o processo de coleta constitui a fonte preservada dos conteúdos recuperados.

Os arquivos existentes nesse ambiente não foram alterados, renomeados, excluídos ou substituídos como parte da preparação para publicação.

Operações de organização, classificação e preparação para o GitHub foram realizadas a partir dos registros consolidados do acervo, mantendo-se o conteúdo original preservado.

## 5. Identificação por SHA-256

O SHA-256 é utilizado como identificador de integridade dos conteúdos digitais preservados.

Os **435 valores SHA-256 utilizados neste repositório correspondem aos valores já registrados nas bases consolidadas que deram origem aos dados do dashboard do acervo**.

Os valores utilizados no processo de organização foram conferidos entre as bases consolidadas antes da geração dos metadados deste repositório.

## 6. Referências duplicadas

Das 465 referências analisadas, **26 correspondem a referências duplicadas**.

Uma referência duplicada ocorre quando diferentes registros históricos estão associados a um conteúdo digital já identificado pelo mesmo SHA-256.

A duplicidade é tratada de forma lógica.

Assim:

- a referência histórica não é considerada inexistente;
- o conteúdo não é contado novamente como novo conteúdo digital;
- arquivos preservados no acervo original não são excluídos em razão da duplicidade;

Dessa forma, as 26 referências duplicadas integram o levantamento histórico.

## 7. Referências históricas sem SHA-256

Foram identificadas **4 referências históricas sem SHA-256**.

Essas referências permanecem registradas por integrarem o levantamento histórico do SPB.

Não são atribuídos hashes artificiais ou estimados a esses registros.

A ausência de SHA-256 indica apenas que a referência histórica não está associada, no acervo consolidado, a um novo conteúdo digital identificado por esse mecanismo.

Uma referência sem hash também não implica necessariamente que o respectivo software não possua outros conteúdos preservados.

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

A estrutura principal do repositório contém documentação e metadados do acervo.

A organização prevista é:

```text
acervo-spb-legado/
├── README.md
├── CATALOGO.md
├── POLITICA-DO-ACERVO.md
├── SECURITY.md
└── softwares/
    └── <software>/
        └── METADADOS.md
