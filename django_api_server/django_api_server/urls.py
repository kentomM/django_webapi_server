"""django_api_server URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.conf.urls import url, include
from django.contrib import admin
from rest_framework_swagger.views import get_swagger_view

from tweets.router import router as tweets_router
from users.views import SignUp, UserInfo

API_TITLE = 'Tweet API'
schema_view = get_swagger_view(title=API_TITLE)

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r"^api/auth/", include("rest_auth.urls")),
    url(r"^api/v1/", include(tweets_router.urls), name='api'),
    url(r"^account/info", UserInfo.as_view(), name='userinfo'),
    url(r"^account/", SignUp.as_view(), name='singup'),
    url(r"swagger-docs/", schema_view),
]
