# Objetivo Geral

Separar as funções existentes de saque, deposito e extrato em funções. Criar duas novas funçoes: cadastrar usuario(cliente) e cadastrar conta bancaria.

Precisamos deixar o codigo mais modularizado, para isso vamos criar funções para as operações existentes: sacar, depositar e visualizar extrato. Além disso, para a versao 2 do nosso sistema precisamos criar duas novas funcoes: Criar usuario(cliente do banco) e criar conta corrente (vincular com usuario).

* Separação em funcoes
    
    Devemos criar funções para todos as operacoes do sistema. Para exercitar tudo o que aprendemos neste modulo, cada funcao vai ter um regra de passagem de argumentos, o retorno e a forma como serao chamadas, pode ser definida da forma que achar melhor.

* Saques: A funcão saque deve receber os argumentos apenas por nome(keyword only). Sugestao de argumento: saldo,valor,extrato,limite,numero_saques, limites_saques. Sugestao de retorno: saldo e extrato.

* Deposito: A função deposito deve receber os argumentos apenas por posicao(positional only). sugestao de argumento: saldo, valor, extrato. sugestao de retorno: saldo e extrato

* Extrato: a função extrato deve receber os argumentos por posicao e nome(positional only e keyword only). Argumentos posicionais: saldo, argumento nomeados: extrato.

* novas funções : precisamos criar duas novas funçoes: criar usuario e criar conta corrente. fique a vontade para adicionar mais funcoes, exemplo: lista de contas.

 - criar usuario(cliente) : o programa deve armazenar os usuarios em uma lista, um usuario e composto por: nome, data de nascimento, cpf e enderenço. O endereco e uma string com formato: logradouro,nro - bairro-cidade /sigla estado. Deve ser armazenado somente os numero de CPF. nao podemos cadastrar 2 usuarios como o mesmo cpf.

 - criar conta corrente: o programa deve armazenar contas em um lista, onde é composta por: agencia,numero da conta e usuario. O numero de conta e sequencial, iniciando em 1. o numero da agencia e fixo "0001". o usuario pode ter mais de uma conta, mas uma conta pertence a somente um usuario.

para vincular um usuario a uma conta, filtre a lista de usuarios buscando  o numero do cpf informado para cada usuario da lista.