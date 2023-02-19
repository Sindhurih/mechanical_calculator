from django.urls import path
from formula import views
urlpatterns = [
    path('',views.home_cards),
    path('show',views.show_cards, name='show_cards'),
    path('<card_name>/', views.detail, name='detail'),
    path('<card_name>/<detail>/', views.formula_page, name='formula_page'),
]