import peewee
from model import BaseModel, Cliente, Animal, Funcionario, Servico
from functions import *

if __name__ == '__main__':
    try:
        Cliente.create_table()
    except peewee.OperationalError:
        print('Tabela Cliente já existe!')

    try:
        Animal.create_table()
    except peewee.OperationalError:
        print('Tabela Animal já existe!')

    try:
        Funcionario.create_table()
    except peewee.OperationalError:
        print('Tabela Funcionario já existe!')

    try:
        Servico.create_table()
    except peewee.OperationalError:
        print('Tabela Servico já existe!')

while True:
    print('MENU DE CADASTRAMENTO')
    print('1 - Cadastrar cliente')
    print('2 - Cadastrar animal')
    print('3 - Cadastrar funcionário')
    print('4 - Cadastrar serviço')
    print('\nMENU DE LISTAGEM')
    print('5 - Listar clientes')
    print('6 - Listar animais')
    print('7 - Listar funcionários')
    print('8 - Listar serviços')
    print('\nMENU DE EXCLUSÃO')
    print('9 - Excluir cliente')
    print('10 - Excluir animal')
    print('11 - Excluir funcionário')
    print('12 - Excluir serviço')
    print('\nMENU DE ALTERAÇÃO')
    print('13 - Alterar cliente')
    print('14 - Alterar animal')
    print('15 - Alterar funcionário')
    print('16 - Alterar serviço')
    print('\n0 - Sair')
    op = input('Informe uma opção acima: ')

    if op == '1':
        cadastroCliente()
    elif op == '2':
        cadastroAnimal()
    elif op == '3':
        cadastroFuncionario()
    elif op == '4':
        cadastroServico()
    elif op == '5':
        listarClientes()
    elif op == '6':
        listarAnimais()
    elif op == '7':
        listarFuncionarios()
    elif op == '8':
        listarServicos()
    elif op == '9':
        listarClientes()
        deletar(Cliente, 'Cliente')
    elif op == '10':
        listarAnimais()
        deletar(Animal, 'Animal')
    elif op == '11':
        listarFuncionarios()
        deletar(Funcionario, 'Funcionario')
    elif op == '12':
        listarServicos()
        deletar(Servico, 'Serviço')
    elif op == '13':
        listarClientes()
        alterarCliente()
    elif op == '14':
        listarAnimais()
        alterarAnimal()
    elif op == '15':
        listarFuncionarios()
        alterarFuncionario()
    elif op == '16':
        listarServicos()
        alterarServico()
    elif op == '0':
        break
    else:
        print('\nOpção inválida!\n')