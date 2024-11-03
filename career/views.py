from django.shortcuts import render


def career_list(request):
    return render(request, 'career/list.html', {'active':'career'})

def career_detail(request):
    return render(request, 'career/detail.html', {'active': 'career'})