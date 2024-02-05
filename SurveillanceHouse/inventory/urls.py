# inventory/urls.py
from django.urls import path
from .views import ItemListView, ItemDetailView, ItemCreateView, ItemUpdateView, ItemDeleteView, get_item_details

urlpatterns = [
    path('items/', ItemListView.as_view(), name='item_list'),
    path('items/<int:pk>/', ItemDetailView.as_view(), name='item_detail'),
    path('items/new/', ItemCreateView.as_view(), name='item_create'),
    path('items/<int:pk>/edit/', ItemUpdateView.as_view(), name='item_update'),
    path('items/<int:pk>/delete/', ItemDeleteView.as_view(), name='item_delete'),
    path('item-details/<int:model_id>/', get_item_details, name='get_item_details'),
]
