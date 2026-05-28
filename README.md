# Sistema de Monitoramento de Eventos Ambientais
Sistema em Python para análise de eventos ambientais provenientes de monitoramento por satélites

## Descrição

Este projeto foi desenvolvido em Python com o objetivo de registrar, armazenar e analisar eventos ambientais, como queimadas, desmatamentos e outros desastres.

O sistema permite o cadastro de múltiplos eventos e realiza automaticamente cálculos estatísticos e análises relevantes, auxiliando no monitoramento dos impactos ambientais registrados.

---

## Funcionalidades

- Cadastro de eventos ambientais
- Validação de dados inseridos pelo usuário
- Armazenamento das informações em listas
- Cálculo da área total afetada
- Média das intensidades dos eventos
- Identificação da região com maior número de ocorrências
- Cálculo da densidade média de ocorrências
- Identificação do evento mais crítico
- Geração de relatório final

---

## Informações cadastradas

Para cada evento, o sistema solicita:

- Tipo de evento
- País
- Região
- Cidade
- Área afetada (km²)
- Intensidade do evento (1 a 10)
- Número de ocorrências

---

## Regras de validação

O sistema possui validações para evitar entradas inválidas:

- A área afetada deve ser maior que zero
- A intensidade deve estar entre 1 e 10
- Campos numéricos aceitam apenas números

