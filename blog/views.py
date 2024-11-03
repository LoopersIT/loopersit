from django.shortcuts import render



def blog_list(request):
    return render(request, 'blog/list.html', {'active':'blog'})


def blog_detail(request):
    return render(request, 'blog/detail.html', {'active':'blog'})