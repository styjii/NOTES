"""
URL configuration for webapp project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from .views import index_view, create_table_view, delete_table_view
from django.urls import path, include

urlpatterns = [
    path('', index_view, name="index"),
    path('create-table/', create_table_view, name="create-table"),
    path('delete-table-<str:table_name>/', delete_table_view, name="delete-table"),
    path('notes/', include('notes.urls')),
]
