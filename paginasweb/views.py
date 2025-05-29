from django.views.generic import TemplateView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import TipoSensor, Controlador, Sensor, Regra, Leitura, Cadastro

# Página inicial
class IndexView(TemplateView):
    template_name = 'paginasweb/index.html'

# Página "sobre"
class SobreView(TemplateView):
    template_name = 'paginasweb/sobre.html'

# Página "Tipo de Sensor"
class TipoSensorView(TemplateView):
    template_name = 'paginasweb/cadastrar/form.html'

# Página "Cadastro"
class CadastroView(TemplateView):
     template_name = 'paginasweb/cadastrar/form.html'

#Página "Controlador"
class ControladorView(TemplateView):
     template_name = 'paginasweb/cadastrar/form.html'

# Views de cadastro (CreateView)

class CadastroCreate(CreateView):
     model = Cadastro
     fields = ['nome', 'email', 'senha']
     template_name = 'paginasweb/form.html'
     success_url = reverse_lazy('index')
     extra_context = {
          'titulo': 'Cadastro de cliente',
          'botao': 'Cadastrar'
     }

class TipoSensorCreate(CreateView):
    model = TipoSensor
    fields = ['numero_serial', 'descricao']
    template_name = 'paginasweb/form.html'
    success_url = reverse_lazy('index')
    extra_context = {
        'titulo': 'Cadastro de tipo de sensor',
        'botao': 'Cadastrar'
    }

class ControladorCreate(CreateView):
    model = Controlador
    fields = ['cadastro_cliente', 'nome', 'descricao']
    template_name = 'paginasweb/form.html'
    success_url = reverse_lazy('index')
    extra_context = {
        'titulo': 'Cadastro de controlador',
        'botao': 'Cadastrar'
    }

class SensorCreate(CreateView):
    model = Sensor
    fields = ['descricao', 'controlador', 'tipo_sensor']
    template_name = 'paginasweb/form.html'
    success_url = reverse_lazy('index')
    extra_context = {
        'titulo': 'Cadastro de sensor',
        'botao': 'Cadastrar'
    }


class RegraCreate(CreateView):
    model = Regra
    fields = ['descricao', 'horario_inicio', 'horario_fim', 'valor_minimo', 'valor_maximo', 'tipo_sensor']
    template_name = 'paginasweb/form.html'
    success_url = reverse_lazy('index')
    extra_context = {
        'titulo': 'Cadastro regra',
        'botao': 'Cadastrar'
    }

class LeituraCreate(CreateView):
    model = Leitura
    fields = ['tipo_sensor', 'valor', 'data', 'sensor', 'alerta']
    template_name = 'paginasweb/form.html'
    success_url = reverse_lazy('index')
    extra_context = {
    'titulo': 'Cadastro de leitura',
    'botao': 'Cadastrar'
    }

################################################################################

class CadastroUpdate(UpdateView):
     model = Cadastro
     fields = ['nome', 'email', 'senha']
     template_name = 'paginasweb/form.html'
     success_url = reverse_lazy('index')
     extra_context = {
          'titulo': 'Cadastro de cliente',
          'botao': 'Cadastrar'
     }

class TipoSensorUpdate(UpdateView):
    model = TipoSensor
    fields = ['numero_serial', 'descricao']
    template_name = 'paginasweb/form.html'
    success_url = reverse_lazy('index')
    extra_context = {
        'titulo': 'Cadastro de tipo de sensor',
        'botao': 'Cadastrar'
    }

class ControladorUpdate(UpdateView):
    model = Controlador
    fields = ['cadastro_cliente', 'nome', 'descricao']
    template_name = 'paginasweb/form.html'
    success_url = reverse_lazy('index')
    extra_context = {
    'titulo': 'Cadastro de controlador',
    'botao': 'Cadastrar'
    }

class SensorUpdate(UpdateView):
    model = Sensor
    fields = ['descricao', 'controlador', 'tipo_sensor']
    template_name = 'paginasweb/form.html'
    success_url = reverse_lazy('index')

class RegraUpdate(UpdateView):
    model = Regra
    fields = ['descricao', 'horario_inicio', 'horario_fim', 'valor_minimo', 'valor_maximo', 'tipo_sensor']
    template_name = 'paginasweb/form.html'
    success_url = reverse_lazy('index')
    extra_context = {
    'titulo': 'Cadastro regra',
    'botao': 'Cadastrar'
    }

class LeituraUpdate(UpdateView):
    model = Leitura
    fields = ['tipo_sensor', 'valor', 'data', 'sensor', 'alerta']
    template_name = 'paginasweb/form.html'
    success_url = reverse_lazy('index')
    extra_context = {
    'titulo': 'Cadastro de leitura',
    'botao': 'Cadastrar'
    }

    ####################################################################################

class CadastroDelete(DeleteView):
     model = Cadastro
     template_name = 'paginasweb/form.html'
     success_url = reverse_lazy('index')
     extra_context = {
          'titulo': 'Excluir cadastro de cliente',
          'botao': 'Excluir'
     }

class TipoSensorDelete(DeleteView):
        model = TipoSensor
        template_name = 'paginasweb/form.html'
        success_url = reverse_lazy('index')
        extra_context = {
        'titulo': 'Excluir tipo de sensor',
        'botao': 'Excluir'
        }

class ControladorDelete(DeleteView):
        model = Controlador
        template_name = 'paginasweb/form.html'
        success_url = reverse_lazy('index')
        extra_context = {
        'titulo': 'Excluir controlador',
        'botao': 'Excluir',
        }

class SensorDelete(DeleteView):
        model = Sensor
        template_name = 'paginasweb/form.html'
        success_url = reverse_lazy('index')
        extra_context = {
        'titulo': 'Excluir sensor',
        'botao': 'Excluir sensor'
        }

class RegraDelete(DeleteView):
        model = Regra
        template_name = 'paginasweb/form.html'
        success_url = reverse_lazy('index')
        extra_context = {
        'titulo': 'Excluir regra',
        'botao': 'Excluir'
        }

class LeituraDelete(DeleteView):
        model = Leitura
        template_name = 'paginasweb/form.html'
        success_url = reverse_lazy('index')
        extra_context = {
        'titulo': 'Excluir leitura',
        'botao': 'Excluir'
            }
        