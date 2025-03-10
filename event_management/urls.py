from django.contrib import admin
from django.urls import path,include
from debug_toolbar.toolbar import debug_toolbar_urls
from events.views import dashboard
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',dashboard,name='dashboard'),
    path('events/',include('events.urls'))
]+ debug_toolbar_urls()
