from django.urls import path
from .views import (
    IndexView, SobreView, TipoSensorView,
    TipoSensorCreate, ControladorCreate, SensorCreate,
    RegraCreate, LeituraCreate
)

from .views import TipoSensorUpdate, ControladorUpdate, SensorUpdate, RegraUpdate, LeituraUpdate

urlpatterns = [
    path('', IndexView.as_view(), name='index'),  # Página inicial
    path('sobre/', SobreView.as_view(), name='sobre'),  # Página sobre
    path('tiposensor/', TipoSensorView.as_view(), name='tiposensor'), #Página tipo de sensor

    path('cadastrar/tiposensor/', TipoSensorCreate.as_view(), name='cadastrar-tipo-sensor'),
    path('cadastrar/controlador/', ControladorCreate.as_view(), name='cadastrar-controlador'),
    path('cadastrar/sensor/', SensorCreate.as_view(), name='cadastrar-sensor'),
    path('cadastrar/regra/', RegraCreate.as_view(), name='cadastrar-regra'),
    path('cadastrar/leitura/', LeituraCreate.as_view(), name='cadastrar-leitura'),

    path ('editar/tiposensor/<int:pk>/', TipoSensorUpdate.as_view(), name='editar-tipo-sensor'),
    path('editar/controlador/<int:pk>/', ControladorUpdate.as_view(), name='editar-controlador'),
    path('editar/sensor/<int:pk>/', SensorUpdate.as_view(), name='editar-sensor'),
    path('editar/regra/<int:pk>/', RegraUpdate.as_view(), name='editar-regra'),
    path('editar/leitura/<int:pk>/', LeituraUpdate.as_view(), name='editar-leitura')

]
