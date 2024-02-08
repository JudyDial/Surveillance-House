# inventory/admin.py
from django.contrib import admin
from .models import  Model, Item, Camera, VideoAudio, Network, General, InTheBox

admin.site.register(Model)
admin.site.register(Network)
admin.site.register(General)
admin.site.register(InTheBox)
admin.site.register(Item)
admin.site.register(Camera)
admin.site.register(VideoAudio)
# Register other models as needed
