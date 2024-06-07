from django.urls import path
from . import views


urlpatterns = [
    path("", views.inicio, name= "home"),
    path("museos/", views.museos, name="museos"),
    path("tramites/",views.tramites, name="tramites"),
    path("institutos/",views.institutos,name="institutos")

]
