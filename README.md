# Sistema Bancário Simples
Um sistema bancário simples implementado em Python, utilizando comandos básicos de condição (if, elif e else) e definição de funções.

## Funcionalidades
* Realiza depósitos
* Realiza saques com limite de R$ 500,00 por saque
* Limita o número de saques por dia a 3

## Como funciona
O sistema bancário é implementado utilizando funções em Python. As principais funções são:
* `deposito()`: realiza um depósito na conta
* `saque()`: realiza um saque na conta, verificando o limite de saque e o número de saques por dia
* `verificar_saque()`: verifica se o saque pode ser realizado, considerando o limite de saque e o número de saques por dia

## Código
O código do sistema bancário está disponível no arquivo `Sistema_Banco.py`.

## Exemplos de uso
* Depositar R$ 100,00: `deposito(100.0)`
* Sacar R$ 200,00: `saque(200.0)`
* Verificar se o saque pode ser realizado: `verificar_saque(200.0)`

## Limitações
* O sistema bancário não armazena dados em um banco de dados, portanto, os dados são perdidos quando o programa é fechado.
* O sistema bancário não implementa segurança para proteger os dados da conta.

## Contribuições
Se você quiser contribuir para o desenvolvimento do sistema bancário, sinta-se à vontade para fazer um fork do repositório e enviar um pull request com suas alterações.

## Licença
O sistema bancário é distribuído sob a licença MIT.
