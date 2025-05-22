from django.views.generic import TemplateView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import TipoSensor, Controlador, Sensor, Regra, Leitura

# Página inicial
class IndexView(TemplateView):
    template_name = 'paginasweb/index.html'

# Página "sobre"
class SobreView(TemplateView):
    template_name = 'paginasweb/sobre.html'

# Página "Tipo de Sensor"
class TipoSensorView(TemplateView):
    template_name = 'paginasweb/tiposensor.html'

# Views de cadastro (CreateView)

class TipoSensorCreate(CreateView):
    model = TipoSensor
    fields = ['descricao']
    template_name = 'paginasweb/tiposensor.html'
    success_url = reverse_lazy('tiposensor')
    extra_context = {
    'titulo': 'Cadastro de tipo de sensor',
    'botao': 'Cadastrar'
    }

class ControladorCreate(CreateView):
    model = Controlador
    fields = ['descricao']
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

class TipoSensorUpdate(UpdateView):
       model = TipoSensor
fields = ['descricao']
template_name = 'paginasweb/form.html'
success_url = reverse_lazy('index')
extra_context = {
    'titulo': 'Cadastro de tipo de sensor',
    'botao': 'Cadastrar'
}

class ControladorUpdate(UpdateView):
    model = Controlador
    fields = ['descricao']
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

    class TipoSensorDelete(DeleteView):
       model = TipoSensor
    fields = ['descricao']
    template_name = 'paginasweb/form.html'
    success_url = reverse_lazy('index')
    extra_context = {
    'titulo': 'Excluir tipo de sensor',
    'botao': 'Excluir'
}