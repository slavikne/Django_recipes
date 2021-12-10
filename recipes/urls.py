"""recipes URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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

from django.urls import path
from calculator.views import recipe
# from . import views

urlpatterns = [
    # здесь зарегистрируйте вашу view-функцию
    path('<dish>/', recipe),
    # Раскомментируйте код, чтобы данные урлы
    # обрабатывались Django
    # path('omlet/', omlet, name='omlet'),
    # path('workdir/', workdir_view, name='workdir'),
    # path('admin/', admin.site.urls),

]
