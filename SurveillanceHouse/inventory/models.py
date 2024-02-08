# inventory/models.py
from email.policy import default
from django.db import models

class Model(models.Model):
    model_name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.model_name

class Item(models.Model):
    ITEM_TYPE_CHOICES = [
        ('wire', 'Wire'),
        ('indoor', 'Indoor'),
        ('outdoor', 'Outdoor'),
        # Add more choices as needed
    ]

    item_name = models.CharField(max_length=100)
    details = models.TextField()
    item_type = models.CharField(max_length=100, choices=ITEM_TYPE_CHOICES, default='wire')
    Item_model = models.ForeignKey(Model, on_delete=models.CASCADE, null=True, blank=True)
    model_image = models.ImageField(upload_to='model_images/', null=True, blank=True)

    def __str__(self):
        return self.item_name

class Camera(models.Model):
    model = models.ForeignKey(Model, on_delete=models.CASCADE)
    image_sensor = models.CharField(max_length=100, blank=True)
    minimum_illumination = models.CharField(max_length=100, blank=True)
    shutter_speed = models.CharField(max_length=100, blank=True)
    lens = models.CharField(max_length=100, blank=True)
    battery_capacity = models.CharField(max_length=100, blank=True)
    day_night = models.CharField(max_length=100, blank=True)
    dnr = models.CharField(max_length=100, blank=True)
    night_vision = models.CharField(max_length=100, blank=True)
    local_storage = models.CharField(max_length=100,  blank=True)
    cloud_storage = models.CharField(max_length=100,blank=True)
    power_supply_camera = models.CharField(max_length=100, blank=True)
    power_supply_base = models.CharField(max_length=100, blank=True)
    power_consumption = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return f"{self.model.model_name} - Camera"

class VideoAudio(models.Model):
    model = models.ForeignKey(Model, on_delete=models.CASCADE)
    max_resolution = models.CharField(max_length=100, blank=True)
    frame_rate = models.CharField(max_length=100, blank=True)
    video_compression = models.CharField(max_length=100, blank=True)
    video_bit_rate = models.CharField(max_length=100, blank=True)
    audio_bit_rate = models.CharField(max_length=100, blank=True)
    max_bitrate = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return f"{self.model.model_name} - Video & Audio"

class Network(models.Model):
    model = models.ForeignKey(Model, on_delete=models.CASCADE)
    wifi_standard = models.CharField(max_length=100, blank=True)
    frequency_range_us = models.CharField(max_length=100, blank=True)
    frequency_range_eu = models.CharField(max_length=100, blank=True)
    channel_bandwidth_us = models.CharField(max_length=100, blank=True)
    channel_bandwidth_eu = models.CharField(max_length=100, blank=True)
    security = models.CharField(max_length=100, blank=True)
    wifi_ha_low_pairing = models.CharField(max_length=100, blank=True)
    protocol = models.CharField(max_length=100, blank=True)
    interface_protocol = models.CharField(max_length=100, blank=True)
    minimum_network_requirement = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return f"{self.model.model_name} - Network"

class General(models.Model):
    camera = models.OneToOneField(
        Camera, on_delete=models.CASCADE, related_name='general_camera')
    operating_conditions_temperature = models.CharField(max_length=100, blank=True)
    operating_conditions_humidity = models.CharField(max_length=100, blank=True)
    ip_grade = models.CharField(max_length=10, blank=True)
    package_dimensions = models.CharField(max_length=100, blank=True)
    weight_camera = models.CharField(max_length=100, blank=True)
    weight_base = models.CharField(max_length=100, blank=True)
    weight_with_package = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return f"{self.camera.model.model_name} - General Specifications"

class InTheBox(models.Model):
    model = models.ForeignKey(Model, on_delete=models.CASCADE)
    items = models.ManyToManyField(Item)

    def __str__(self):
        return f"{self.model.model_name} - In the Box"
