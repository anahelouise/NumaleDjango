from django.contrib import admin
from django.urls import path
from numale.views import my_view, root_view, user_view, inicio, contato

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', root_view),
    path('inicio/', inicio, name='inicio'),
    path('user/<str:username>/', user_view),
    path('contato/', contato, name='contato'),
]