from django.db import models
from django.utils.text import slugify


#service and subservice models----------------------------------------------
class Service(models.Model):
    name = models.CharField(max_length=250)
    slug = models.SlugField(blank=True, unique=True)
    description = models.TextField()
    image = models.ImageField(upload_to='service/%Y/%m', blank=True)
    home_icon = models.ImageField(upload_to='service_icon/%Y/%m', blank=True)
    order = models.PositiveIntegerField(default=1)

    class Meta:
        ordering = ['order']
        indexes = [models.Index(fields=['order'])]

    def __str__(self):
        return self.name


class ServiceOffer(models.Model):
    service = models.ForeignKey(Service, on_delete=models.CASCADE, related_name='offers')
    offer = models.CharField(max_length=250)
    order = models.PositiveIntegerField(default=1)
    class Meta:
        ordering = ['order']
        indexes = [models.Index(fields=['order'])]

    def __str__(self):
        return self.offer

class SubService(models.Model):
    service = models.ForeignKey(Service, on_delete=models.CASCADE, related_name='subservices')
    name = models.CharField(max_length=250)
    slug = models.SlugField(blank=True, help_text='if does not fill automatically, leave blank')
    description = models.TextField()
    image = models.ImageField(upload_to='service/%Y/%m', blank=True)
    order = models.PositiveIntegerField(default=1)

    class Meta:
        ordering = ['order']
        indexes = [models.Index(fields=['order'])]

    def __str__(self):
        return self.name
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)