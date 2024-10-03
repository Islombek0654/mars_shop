from django.urls import path
from .views import main_pag, register_view, login_view, logout_view, profile_view, edit_profile_view, add_coins_view

app_name = 'users'

urlpatterns = [
    path('', main_pag, name='mainpag'),
    path('sighnup/', register_view, name='sighnup'),
    # path('sighin/',sighnin_view, name='sighnin' ),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('profile/', profile_view, name='profile'),
    path('edit/<int:pk>/', edit_profile_view, name='edit'),
    path('edit/<int:id>/', add_coins_view, name='add-coins'),
]