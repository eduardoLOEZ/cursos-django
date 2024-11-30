"""
URL configuration for project_name project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.urls import path, include
from users.views import home, cursos, contacto, user_profile, upload_profile_picture # Importar la vista de inicio
from django.conf import settings
from django.conf.urls.static import static



urlpatterns = [
    path('admin/', admin.site.urls),
    path('users/', include('users.urls')), 
    path('', home, name='home'),  # Página de inicio
    path('contacto/', contacto, name='contacto'),  # Página de inicio
    path('profile/', user_profile, name='user_profile'),
    path('profile/upload-picture/', upload_profile_picture, name='upload_profile_picture'),
    path('cursos/', include('cursos.urls')),  # Incluir las rutas de la app "cursos"
    path('stripe/', include('stripe_payments.urls')),






]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

