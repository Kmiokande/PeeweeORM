import peewee

db = peewee.SqliteDatabase('banco.db')


class BaseModel(peewee.Model):
    class Meta:
        database = db


class Cliente(BaseModel):
    nome = peewee.TextField()
    endereco = peewee.TextField()
    telefone = peewee.TextField()


class Animal(BaseModel):
    nome = peewee.TextField()
    especie = peewee.TextField()
    raca = peewee.TextField()
    dono = peewee.ForeignKeyField(Cliente, related_name='dono')


class Funcionario(BaseModel):
    nome = peewee.TextField()


class Servico(BaseModel):
    data = peewee.DateTimeField()
    tipoServico = peewee.TextField()
    aberto = peewee.BooleanField()
    codCliente = peewee.ForeignKeyField(Cliente, related_name='cliente')
    codAnimal = peewee.ForeignKeyField(Animal, related_name='animal')
    codFuncionario = peewee.ForeignKeyField(
        Funcionario, related_name='tecnico')
    valor = peewee.FloatField()
