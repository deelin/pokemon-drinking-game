from django.contrib import admin
from django.urls import include, path

from board import urls as board_urls

urlpatterns = [
    path('', include(board_urls)),
    path('admin/', admin.site.urls),
] 
