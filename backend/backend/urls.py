

from django.contrib import admin
from todo import views                            # add this
from rest_framework import routers                    # add this
from django.urls import path, include 

# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()                      # add this
router.register(r'tasks', views.TodoView, 'task') 


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls))                # add this
]

