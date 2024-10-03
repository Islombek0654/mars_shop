from django.urls import path
from .views import main_page, add_product_view, order_view, buy_product_view

urlpatterns = [
    path('', main_page, name='home'),
    path('order/<int:id>/', order_view, name='order'),
    path('buy/<int:id>/', buy_product_view, name='buy'),

]