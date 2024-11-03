from django.shortcuts import render


def career_list(request):
    return render(request, 'career/career_list.html', {'active':'career'})

def career_detail(request):
    return render(request, 'career/career_detail.html', {'active': 'career'})