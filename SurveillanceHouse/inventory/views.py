# inventory/views.py
from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import *

class ItemListView(ListView):
    model = Item
    template_name = 'inventory/item_list.html'

class ItemDetailView(DetailView):
    model = Item
    template_name = 'inventory/item_detail.html'

class ItemCreateView(CreateView):
    model = Item
    template_name = 'inventory/item_form.html'
    fields = ['item_name', 'details', 'model']

class ItemUpdateView(UpdateView):
    model = Item
    template_name = 'inventory/item_form.html'
    fields = ['item_name', 'details', 'model']

class ItemDeleteView(DeleteView):
    model = Item
    template_name = 'inventory/item_confirm_delete.html'
    success_url = reverse_lazy('item_list')

def get_item_details(request, model_id, item_id):
    model = get_object_or_404(Model, id=model_id)
    item = get_object_or_404(Item, id=item_id)
    camera = get_object_or_404(Camera, model=model_id)
    video_audio = get_object_or_404(VideoAudio, model=model_id)
    network = get_object_or_404(Network, model=model_id)
    general = get_object_or_404(General, camera=model_id)

    return render(request, 'inventory/item_detail.html', {
        'model': model,
        'item': item,
        'camera': camera,
        'video_audio': video_audio,
        'network': network,
        'general': general,
    })



