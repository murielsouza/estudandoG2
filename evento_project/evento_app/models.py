from django.db import models

class Evento(models.Model):
    nome = models.CharField(max_length=128)
    tema = models. CharField(max_length=30)

    def __str__(self):
        return self.nome + " - "+ self.tema

class Usuario(models.Model):
    nome = models.CharField(max_length=128)
    cpf = models. CharField(max_length=14)

    TIPO_CHOICES = (
        ('adm', 'ADMINISTRADOR'),
        ('aut', 'AUTOR'),
        ('avl', 'AVALIADOR'),
    )
    tipo = models.CharField(max_length=3, choices=TIPO_CHOICES, blank=False, null=False)
    evento = models.ForeignKey(Evento, null=True, blank=False)

    def __str__(self):
        return self.nome

class Artigo(models.Model):
    nome = models.CharField(max_length=128)
    tema= models. CharField(max_length=14)
    autor = models.ForeignKey(Usuario, null=True, blank=False)
    evento = models.ForeignKey(Evento, null=True, blank=False)

    def __str__(self):
        return self.nome + " - " + self.autor.nome

class Avaliacao(models.Model):
    quali_tec = models.IntegerField(max_length=1)
    inovacao = models.IntegerField(max_length=1)
    resultado = models.IntegerField(max_length=1)
    metodologia = models.IntegerField(max_length=1)
    adeq_evento = models.IntegerField(max_length=1)
    artigo = models.ForeignKey(Artigo, null=True, blank=False)
    avaliador= models.ForeignKey(Usuario, null=True, blank=False)

    def __str__(self):
        return "Avaliação X - " + self.artigo.nome + "( " + self.avaliador.nome + " )"
