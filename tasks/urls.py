from django.urls import path
from . import views

urlpatterns = [
    path("", views.login_auth, name='login_auth'),
    path("logout_user", views.logout_user, name="logout_user"),
    path("home", views.home, name="home"),
    path("ciar_nova_task", views.ciar_nova_task, name="ciar_nova_task"),
    path("deletar_task/<int:id>", views.deletar_task, name="deletar_task"),
    path("marcar_task/<int:id>", views.marcar_task, name="marcar_task"),
]




