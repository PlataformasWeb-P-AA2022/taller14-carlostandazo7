from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import RequestContext
from django.shortcuts import render
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

# ejemplo de uso django-rest_framework
from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from rest_framework import permissions
from administrativo.serializers import UserSerializer, GroupSerializer, PropietarioSerializer, DepartamentoSerializer

# importar las clases de models.py
from administrativo.models import *


# crear vistas a través de viewsets
class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAuthenticated]


class PropietarioViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    This viewset automatically provides `list`, `create`, `retrieve`,
    `update` and `destroy` actions.
    """
    queryset = Propietario.objects.all()
    serializer_class = PropietarioSerializer
    # permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        """
        """
        valor = self.request.query_params
        print(valor)
        if 'nombre' in valor.keys():
            return Propietario.objects.filter(nombre=valor['nombre']).all()
        else:
            if 'apellido' in valor.keys():
                return Propietario.objects.filter(apellido__contains=valor['apellido']).all()
            else:
                return Propietario.objects.all()


class DepartamentoViewSet(viewsets.ModelViewSet):

    queryset = Departamento.objects.all()
    serializer_class = DepartamentoSerializer

