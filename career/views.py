from django.shortcuts import render


def job_list(request):
    return render(request, 'career/list.html', {'active':'career'})

def job_detail(request):
    return render(request, 'career/detail.html', {'active': 'career'})