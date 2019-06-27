import peewee
from datetime import date
from model import BaseModel, Cliente, Animal, Funcionario, Servico


def cadastroCliente():
    nome = input('Informe o nome: ')
    endereco = input('Informe o endereço: ')
    telefone = input('Informe o telefone: ')
    Cliente.create(nome=nome, endereco=endereco, telefone=telefone)


def cadastroAnimal():
    nome = input('Informe o nome: ')
    especie = input('Informe a espécie: ')
    raca = input('Informe a raça: ')
    listarClientes()
    dono = int(input('Informe o código do dono: '))
    Animal.create(nome=nome, especie=especie, raca=raca, dono=dono)


def cadastroFuncionario():
    nome = input('Informe o nome: ')
    Funcionario.create(nome=nome)


def cadastroServico():
    data = date.today()
    tipo = input('Informe o tipo de serviço: ')
    aberto = True
    listarClientes()
    codCli = int(input('Informe o código do dono: '))
    listarAnimais()
    codAni = int(input('Informe o código do animal: '))
    listarFuncionarios()
    codFun = int(input('Informe o código do funcionário: '))
    valor = float(input('Informe o valor total: '))
    Servico.create(data=data, tipoServico=tipo, aberto=aberto,
                   codCliente=codCli, codAnimal=codAni, codFuncionario=codFun, valor=valor)


def listarClientes():
    clientes = Cliente.select()
    if clientes.count() == 0:
        print('\nNão há clientes cadastrados.\n')
    else:
        for cliente in clientes:
            print('Cod: %d - Nome: %s - Endereço: %s - Telefone: %s' %
                  (cliente.id, cliente.nome, cliente.endereco, cliente.telefone))


def listarAnimais():
    # animais = Animal.select(Animal.id, Animal.nome, Animal.especie, Animal.raca, Cliente.nome).join(Cliente, on=(Animal.dono == Cliente.id))
    animais = Animal.select()
    if animais.count() == 0:
        print('\nNão há animais cadastrados.\n')
    else:
        for a in animais:
            print('Cod: %d - Nome: %s - Espécie: %s - Raça: %s - Dono: %s' %
                  (a.id, a.nome, a.especie, a.raca, a.dono))


def listarFuncionarios():
    funcionarios = Funcionario.select()
    if funcionarios.count() == 0:
        print('\nNão há funcionários cadastrados.\n')
    else:
        for f in funcionarios:
            print('Cod: %d - Nome: %s' % (f.id, f.nome))


def listarServicos():
    servicos = Servico.select()
    if servicos.count() == 0:
        print('\nNão há serviços cadastrados.\n')
    else:
        for s in servicos:
            if s.aberto:
                print('Cod: %d - Tipo de serviço: %s - Cliente: %s - Animal: %s - Funcionário: %s - Valor: %.2f - Status: Aberto' %
                      (s.id, s.tipoServico, s.codCliente, s.codAnimal, s.codFuncionario, s.valor))
            else:
                print('Cod: %d - Tipo de serviço: %s - Cliente: %s - Animal: %s - Funcionário: %s - Valor: %.2f - Status: Fechado' %
                      (s.id, s.tipoServico, s.codCliente, s.codAnimal, s.codFuncionario, s.valor))


def alterarCliente():
    idCliente = int(input('Informe o código do cliente que deseja alterar: '))
    try:
        cliente = Cliente.get(Cliente.id == idCliente)
        cliente.nome = input('Informe o novo nome: ')
        cliente.endereco = input('Informe o novo endereço: ')
        cliente.telefone = input('Informe o novo telefone:')
        cliente.save()
    except:
        print('Código inválido!')


def alterarAnimal():
    idAnimal = int(input('Informe o código do animal que deseja alterar: '))
    try:
        animal = Animal.get(Animal.id == idAnimal)
        animal.nome = input('Informe o novo nome: ')
        animal.especie = input('Informe a nova espécie: ')
        animal.raca = input('Informe a nova raça: ')
        listarClientes()
        animal.dono = int(input('Informe o novo código do dono: '))
        animal.save()
    except:
        print('Código inválido!')


def alterarFuncionario():
    idFuncionario = int(
        input('Informe o código do funcionário que deseja alterar: '))
    try:
        funcionario = Funcionario.get(Funcionario.id == idFuncionario)
        funcionario.nome = input('Informe o novo nome: ')
        funcionario.save()
    except:
        print('Código inválido!')


def alterarServico():
    idServico = int(input('Informe o código do serviço que deseja alterar: '))
    try:
        servico = Servico.get(Servico.id == idServico)
        servico.data = input('Informe uma nova data: AAAA-MM-DD ')
        servico.tipoServico = input('Informe um novo tipo de serviço: ')
        status = input('Informe um novo tipo de status: A=aberto/F=fechado ')
        if (status.upper()) == 'A':
            servico.tipo = True
        elif (status.upper()) == 'F':
            servico.tipo = False
        else:
            servico.tipo = True
        listarClientes()
        servico.codCliente = int('Informe um novo código de cliente: ')
        listarAnimais()
        servico.codAnimal = int('Informe um novo código de animal: ')
        listarFuncionarios()
        servico.codFuncionario = int('Informe um novo código de funcionário: ')
        servico.valor = float(input('Informe um novo valor: '))
        servico.save()
    except:
        print('Código inválido!')


def deletar(object, nome):
    id = int(input('Informe o código do %s: ' % (nome)))
    try:
        tabela = object.get(object.id == id)
        tabela.delete_instance()
    except:
        print('\nID inexistente!\n')
