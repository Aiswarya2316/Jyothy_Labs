from django.urls import path
from .import views
from django.urls import path
from .views import AddItemView, ItemListView, SearchItemView, delete_item
urlpatterns = [
    path('',views.home,name='home'),
    path('add_item/', AddItemView.as_view(), name='add_item'),
    path('item_list/', ItemListView.as_view(), name='item_list'),
    path('search_item/', SearchItemView.as_view(), name='search_item'),
    path('delete_item/<int:item_id>/', delete_item, name='delete_item'),


]