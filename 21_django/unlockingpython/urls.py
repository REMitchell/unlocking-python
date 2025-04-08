'''
URL configuration for unlockingpython project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
'''

from django.contrib import admin
from django.urls import path

import posts.views
import testapp
import posts
import testapp.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('hello', testapp.views.hello),
    path('hello_template', testapp.views.hello_template),
    path('hello_url_params', testapp.views.hello_url_params),
    path('hello_path_params/<str:name>', testapp.views.hello_path_params),
    path('hello_post', testapp.views.hello_post),
    path('hello', testapp.views.hello),
    path('posts', posts.views.all_posts),
    path('profile', posts.views.profile),
    path('profile/<int:user_id>', posts.views.profile_by_id),
]
