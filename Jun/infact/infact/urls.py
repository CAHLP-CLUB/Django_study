"""infact URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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

urlpatterns = [
    path('admin/', admin.site.urls),
    # accountapp 내부에 있는 view에 들어가기 때문에 이름은 account/로 한다.
    # accountapp 내부에 있는 urls.py를 모두 포함해서 그 하위 디렉토리로 분기를 해라
    # 추후에 accountapp -> urls.py를 참고해서 그 안에서 다시 분기
    path('account/', include('accountapp.urls'))
]
