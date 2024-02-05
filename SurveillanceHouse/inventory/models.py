# inventory/models.py
from django.db import models


class Certification(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Model(models.Model):
    model_name = models.CharField(max_length=100)
    model_image = models.ImageField(upload_to='model_images/', null=True, blank=True)


    def __str__(self):
        return self.model_name


class Item(models.Model):
    item_name = models.CharField(max_length=100)
    details = models.TextField()
    specifications = models.ForeignKey(Model, on_delete=models.CASCADE, null=True, blank=True)
    

    def __str__(self):
        return self.item_name


class Camera(models.Model):
    model = models.ForeignKey(Model, on_delete=models.CASCADE)
    image_sensor = models.CharField(max_length=100)
    minimum_illumination = models.CharField(max_length=100)
    shutter_speed = models.CharField(max_length=100)
    lens = models.CharField(max_length=100)
    battery_capacity = models.CharField(max_length=100)
    day_night = models.CharField(max_length=100)
    dnr = models.CharField(max_length=100)
    night_vision = models.CharField(max_length=100)

    # Storage Details
    local_storage = models.CharField(
        max_length=100, help_text="Supports microSD card (Up to 256G) on the pairing base station")
    cloud_storage = models.CharField(
        max_length=100, help_text="Supports EZVIZ CloudPlay storage (subscription required)")

    # Power-related fields
    power_supply_camera = models.CharField(max_length=100)
    power_supply_base = models.CharField(max_length=100)
    power_consumption = models.CharField(max_length=100)

    # Certifications
    certifications = models.ManyToManyField(Certification)

    def __str__(self):
        return f"{self.model.model_name} - Camera"


class VideoAudio(models.Model):
    model = models.ForeignKey(Model, on_delete=models.CASCADE)
    max_resolution = models.CharField(max_length=100)
    frame_rate = models.CharField(max_length=100)
    video_compression = models.CharField(max_length=100)
    video_bit_rate = models.CharField(max_length=100)
    audio_bit_rate = models.CharField(max_length=100)
    max_bitrate = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.model.model_name} - Video & Audio"


class Network(models.Model):
    model = models.ForeignKey(Model, on_delete=models.CASCADE)
    wifi_standard = models.CharField(max_length=100)
    frequency_range_us = models.CharField(max_length=100)
    frequency_range_eu = models.CharField(max_length=100)
    channel_bandwidth_us = models.CharField(max_length=100)
    channel_bandwidth_eu = models.CharField(max_length=100)
    security = models.CharField(max_length=100)
    wifi_ha_low_pairing = models.CharField(max_length=100)
    protocol = models.CharField(max_length=100)
    interface_protocol = models.CharField(max_length=100)
    minimum_network_requirement = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.model.model_name} - Network"


class General(models.Model):
    camera = models.OneToOneField(
        Camera, on_delete=models.CASCADE, related_name='general')
    operating_conditions_temperature = models.CharField(max_length=100)
    operating_conditions_humidity = models.CharField(max_length=100)
    ip_grade = models.CharField(max_length=10)
    package_dimensions = models.CharField(max_length=100)
    weight_camera = models.CharField(max_length=100)
    weight_base = models.CharField(max_length=100)
    weight_with_package = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.camera.model.model_name} - General Specifications"


class InTheBox(models.Model):
    model = models.ForeignKey(Model, on_delete=models.CASCADE)
    items = models.ManyToManyField(Item)

    def __str__(self):
        return f"{self.model.model_name} - In the Box"
