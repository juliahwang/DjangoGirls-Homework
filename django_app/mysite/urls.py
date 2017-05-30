"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from blog import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', views.post_list, name="post_list"),

    # /post/로 시작하고 중간에 숫자 1개 이상을 가지고, /로 끝나는 정규표현식.
    # *을 쓰면 숫자가 없는 것도 포함하므로 1개 이상 포함하는 +를 사용
    url(r'^(?P<pk>\d+)/$', views.post_detail, name="post_detail"),
    # name="post_detail" - url에 이름을 부여하여 동적으로 이후 수정을 용이하게 해준다.
    url(r'post/create/$', views.post_create, name='post_create')
]
