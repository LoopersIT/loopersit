from django.shortcuts import render, get_object_or_404
from .models import Job
from .forms import ApplicationForm


def job_list(request):
    jobs = Job.objects.filter(active=True)
    return render(request, 'career/list.html', {'active':'career', 'jobs':jobs})

def job_detail(request, slug):
    job = get_object_or_404(Job, slug=slug)
    return render(request, 'career/detail.html', {'active': 'career', 'job':job})