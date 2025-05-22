from django.db import models

# Todas as classes DEVEM ter a herança para a classe Model que está dentro de "models"
# class SuaClasse(models.Model):
#   atributo = models.TipoDeAtributo(propriedade1=valor1, p2="v2", p3=v3)

# Depois de criar as classes, defina os atributos e seus tipos
# https://docs.djangoproject.com/pt-br/4.2/ref/models/fields/#field-types

# Cada campo tem suas propriedades, que estão disponíveis em
# https://docs.djangoproject.com/pt-br/4.2/ref/models/fields/#field-options

class TipoSensor(models.Model):
    descricao = models.CharField(max_length=255, verbose_name="Descrição")


class Controlador(models.Model):
    descricao = models.CharField(max_length=255, verbose_name="Descrição")


class Sensor(models.Model):
    descricao = models.CharField(max_length=255, verbose_name="Descrição")
    controlador = models.ForeignKey(Controlador, on_delete=models.PROTECT)
    tipo_sensor = models.ForeignKey(TipoSensor, on_delete=models.PROTECT)


class Regra(models.Model):
    descricao = models.CharField(max_length=255, verbose_name="Descrição")
    horario_inicio = models.CharField(
        max_length=10,
        verbose_name="Horário de Início"
    )
    horario_fim = models.CharField(
        max_length=10,
        verbose_name="Horário de Fim"
    )
    valor_minimo = models.FloatField()
    valor_maximo = models.FloatField()
    tipo_sensor = models.ForeignKey(
        TipoSensor, on_delete=models.PROTECT, null=True, blank=True
    )


class Leitura(models.Model):
    tipo_sensor = models.ForeignKey(TipoSensor, on_delete=models.PROTECT)
    valor = models.FloatField()
    data = models.DateTimeField()
    sensor = models.ForeignKey(Sensor, on_delete=models.PROTECT)
    alerta = models.ForeignKey(
        Regra, on_delete=models.SET_NULL, null=True, blank=True
    )
