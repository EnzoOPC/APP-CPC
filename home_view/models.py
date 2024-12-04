from django.db import models

class PessoaFisica(models.Model):
    name = models.CharField(max_length=255, verbose_name="Nome Completo", null=False, blank=False)
    rg = models.CharField(max_length=15, verbose_name="RG", null=False, blank=False)
    cpf = models.CharField(max_length=11, verbose_name="CPF", null=False, blank=False)
    birth_date = models.DateField(verbose_name="Data de Nascimento", null=False, blank=False)
    cep = models.IntegerField(verbose_name="CEP", null=False, blank=False)
    phone = models.CharField(max_length=16, verbose_name="Celular", null=False, blank=False)
    email = models.EmailField(verbose_name="E-mail", max_length=255, null=False, blank=False)
    password = models.CharField(max_length=255, verbose_name="Senha", null=False, blank=False)
    created_at = models.DateTimeField(auto_now_add=True, null=False, blank=False)

    
    
class PessoaJuridica(PessoaFisica):
    buisness_name = models.CharField(max_length=255, verbose_name="Nome do Empreendimento", null=False, blank=False)
    cnpj = models.IntegerField(verbose_name="CNPJ", null=False, blank=False)
    adress = models.CharField(max_length=255, verbose_name="Endereço", null=False, blank=False)
    region = models.CharField(max_length=255, verbose_name="Região", null=False, blank=False)
    buisness_phone = models.CharField(max_length=16, verbose_name="Telefone do Empreendimento", null=False, blank=False)
    buisness_email = models.CharField(max_length=255, verbose_name="E-mail do Empreendimento", null=True, blank=True)
    social_media = models.CharField(max_length=255, verbose_name="Redes Sociais", null=True, blank=True)

    

#lista parceiro
class Parceiro(models.Model):
    nome = models.CharField(max_length=200)  
    ativo = models.BooleanField(default=True) 

    def __str__(self):
        return self.nome




