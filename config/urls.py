"""config URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
    # 이렇게 연결을 하면 http://127.0.0.1:8000/bookmark/[이하URL] 같은 주소로 접속하면,
    # bookmark/까지의 URL을 잘라내고 나머지 부분을 bookmark.urls로 전달해 찾아봅니다
    path('bookmark/', include('bookmark.urls')),
    path('admin/', admin.site.urls),
]
