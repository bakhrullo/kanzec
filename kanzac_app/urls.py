from django.urls import path

from .views import *

urlpatterns = [
    path('user/create/', UserCreateView.as_view()),
    path('user/get/<int:tg_id>', UserGetView.as_view()),
    path('category/', CategoryListView.as_view()),
    path('product/', ProductListView.as_view()),
    path('product/<int:id>', ProductGetView.as_view()),
    path('order/create/', OrderCreateView.as_view()),
    path('order/get/', OrderGetView.as_view()),
    path('video/<int:id>', VideoListView.as_view())
]
