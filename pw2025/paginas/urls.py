
from django.urls import path
from .views import IndexView, SobreView

urlpatterns = [
    path('', IndexView.as_view(), name='index'), #url pagina inicial
    path('sobre/', SobreView.as_view(), name='sobre'),
]
