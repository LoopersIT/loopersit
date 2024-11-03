from django.shortcuts import render


def career_list(request):
    return render(request, 'career/career_list.html', {'active':'career'})

