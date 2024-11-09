from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField
from django.urls import reverse
from .validators import validate_file_size


JOB_TYPE_CHOICES = (
    ('full_time', 'Full-time'),
    ('part_time', 'Part-time'),

)

JOB_MODE_CHOICES = (
    ('on_site', 'On-site'),
    ('remote', 'Remote'),
    ('hybrid', 'Hybrid'),

)


class Job(models.Model):
    title = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250)
    job_type = models.CharField(max_length=20, choices=JOB_TYPE_CHOICES)
    job_mode = models.CharField(max_length=20, choices=JOB_MODE_CHOICES)
    short_info = models.TextField()
    deadline = models.DateField(auto_now=False, auto_now_add=False)
    detail = RichTextUploadingField(blank=True, null=True)
    order = models.PositiveIntegerField(default=1)
    active = models.BooleanField(default=True)

    class Meta:
        ordering = ['order', 'deadline']
        indexes = [models.Index(fields=['order'])]
    
    def get_absolute_url(self):
        return reverse('career_detail', args=[self.slug])
   
    def __str__(self):
        return self.title


class Application(models.Model):
    role = models.CharField(max_length=250, choices=[], blank=False)
    name = models.CharField(max_length=250)
    email = models.EmailField( max_length=100)
    mobile_number = models.CharField(max_length=20)
    salary_expectation = models.CharField(max_length=10)
    cv = models.FileField(upload_to='cvs/%Y/%m', validators=[validate_file_size])
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created', ]
        indexes = [models.Index(fields=['-created'])]
   
    def __str__(self):
        return self.name



