from django.db import models



class Campo(models.Model):
    nome = models.CharField('nome', max_length=100)
    descricao = models.CharField('descrição', max_length=100)

    def __str__(self):
        return self.nome


class Atividade(models.Model):
    numero = models.IntegerField()
    descricao = models.CharField('descrição', max_length=100)
    pontos = models.DecimalField(decimal_places=2, max_digits=8)
    detalhes = models.CharField('detalhes', max_length=100)

    campo = models.ForeignKey('Campo', on_delete=models.PROTECT)

    def __str__(self):
        return self.descricao 
