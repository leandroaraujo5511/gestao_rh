from django.urls import path
from .views import (
    Departamentoslist,
    DepartamentosCreate,
    DepartamentoUpdate,
    DepartamentoDelete
)

urlpatterns = [
    path('list', Departamentoslist.as_view(), name='list_departamentos'),
    path('novo', DepartamentosCreate.as_view(), name='create_departamentos'),
    path('update/<int:pk>/', DepartamentoUpdate.as_view(), name='update_departamanto'),
    path('delete/<int:pk>/', DepartamentoDelete.as_view(), name='delete_departamento'),
]
