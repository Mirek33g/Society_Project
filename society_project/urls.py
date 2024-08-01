from django.contrib import admin
from django.urls import path, include
from debug_toolbar.toolbar import debug_toolbar_urls

admin.site.site_header = 'Society Admin'
admin.site.index_title = 'Administration'

urlpatterns = [
                  path('admin/', admin.site.urls),
                  path('playground/', include('playground.urls')),
              ] + debug_toolbar_urls()
