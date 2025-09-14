from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("buy/", views.buy_bike, name="buy_bike"),
    path("sell/", views.sell_bike, name="sell_bike"),
    path("about/", views.about, name="about"),
    path("contact/", views.contact, name="contact"),
    path("login/", views.login_view, name="login"),



    path("buybike/<int:pk>/", views.buybike_detail, name="buybike_detail"),
  
    path('payment/', views.payment_page, name='payment_page'),
]


