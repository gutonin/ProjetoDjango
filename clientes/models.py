from django.db import models


class Pessoa(models.Model):
    nome = models.CharField(max_length=30)
    sobrenome = models.CharField(max_length=50)
    idade = models.IntegerField()
    salario = models.DecimalField(max_digits=7,decimal_places=2)
    bio = models.TextField()
    foto = models.ImageField(upload_to='fotos_clientes', null=True, blank=True)

    def __str__(self):
        return '{} {}'.format(self.nome, self.sobrenome)