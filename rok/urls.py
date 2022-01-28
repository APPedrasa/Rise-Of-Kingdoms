"""rok URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from django.contrib import admin
from django.urls import path
from rok.views.commander import CommanderGet
from rok.views.resource import ResourceGet
from rok.views.blacksmith import BlacksmithGet
from rok.views.profile import ProfileGet
from rok.views.speedup import SpeedupGet
from rok.views.boost import BoostGet
from rok.views.kill import KillGet

urlpatterns = [
    path('admin/', admin.site.urls),

    #ROK
    path('commanders/', CommanderGet.as_view()),
    path('resource/', ResourceGet.as_view()),
    path('blacksmith/', BlacksmithGet.as_view()),
    path('profile/', ProfileGet.as_view()),
    path('speedup/', SpeedupGet.as_view()),
    path('boost/', BoostGet.as_view()),
    path('kill/', KillGet.as_view()),
]
