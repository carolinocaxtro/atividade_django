from django.db import models

class Cliente(models.Model):
    nome = models.CharField(max_length=100)
    email = models.EmailField()
    telefone = models.CharField(max_length=20)
    endereco = models.TextField()

    def __str__(self):
        return self.nome

class Quarto(models.Model):
    apartamento = models.IntegerField()
    valor = models.FloatField()

    def __str__(self):
        return f"Quarto {self.apartamento}"

class Hospedagem(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    quarto = models.ForeignKey(Quarto, on_delete=models.CASCADE)
    data_entrada = models.DateField()
    data_saida = models.DateField()
    valor = models.FloatField()

    def __str__(self):
        return f"Hospedagem de {self.cliente.nome} - Quarto {self.quarto.apartamento}"

class Consumo(models.Model):
    nome = models.CharField(max_length=100)
    data = models.DateField()
    valor = models.DecimalField(max_digits=10, decimal_places=2)
    hospedagem = models.ForeignKey(Hospedagem, on_delete=models.CASCADE)

    def __str__(self):
        return f"Consumo de {self.nome} - Hospedagem: {self.hospedagem.id}"
