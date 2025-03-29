from django.urls import path
from .import views
from django.urls import path
from .views import AddItemView, ItemListView, SearchItemView
urlpatterns = [
    path('',views.home,name='home'),
    path('add/', AddItemView.as_view(), name='add_item'),
    path('items/', ItemListView.as_view(), name='item_list'),
    path('search/', SearchItemView.as_view(), name='search_item'),


]