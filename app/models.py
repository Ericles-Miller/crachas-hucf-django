from django.db import models

# Create your models here.
class Servidor(models.Model):
    nome = models.CharField(max_length = 100 , null=False, verbose_name='Nome')
    cpf  = models.CharField(max_length = 11, null = False, unique = True, verbose_name='Cpf')
    imagem = models.ImageField(upload_to = 'imagens/', null =False,default='imagens/None/no-img.jpg', verbose_name='Imagem Crachá')


def __str__(self):
    return self.nome