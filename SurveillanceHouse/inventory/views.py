# inventory/views.py
from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Item, Model

class ItemListView(ListView):
    model = Item
    template_name = 'inventory/item_list.html'

class ItemDetailView(DetailView):
    model = Item
    template_name = 'inventory/item_detail.html'

class ItemCreateView(CreateView):
    model = Item
    template_name = 'inventory/item_form.html'
    fields = ['item_name', 'details', 'specifications']

class ItemUpdateView(UpdateView):
    model = Item
    template_name = 'inventory/item_form.html'
    fields = ['item_name', 'details', 'specifications']

class ItemDeleteView(DeleteView):
    model = Item
    template_name = 'inventory/item_confirm_delete.html'
    success_url = reverse_lazy('item_list')

def get_item_details(request, model_id):
    model = get_object_or_404(Model, id=model_id)
    item = get_object_or_404(Item, specifications=model)
    camera = model.camera_set.first()  # Assuming a related_name of 'camera' in Model
    video_audio = model.videoaudio_set.first()  # Assuming a related_name of 'videoaudio' in Model
    network = model.network_set.first()  # Assuming a related_name of 'network' in Model
    general = camera.general  # Assuming a related_name of 'general' in Camera model

    return render(request, 'inventory/item_details.html', {
        'model': model,
        'item': item,
        'camera': camera,
        'video_audio': video_audio,
        'network': network,
        'general': general,
    })
