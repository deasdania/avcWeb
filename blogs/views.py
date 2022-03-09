from django.shortcuts import render
from django.http import HttpResponse
from django.views import generic
from .models import Post
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage

def index(request):
    return HttpResponse("Hallo")

def PostList(request):
    object_list = Post.objects.filter(status=1).order_by('-created_on')
    paginator = Paginator(object_list, 1)  # 3 posts in each page
    page = request.GET.get('page')
    try:
        post_list = paginator.page(page)
    except PageNotAnInteger:
            # If page is not an integer deliver the first page
        post_list = paginator.page(1)
    except EmptyPage:
        # If page is out of range deliver last page of results
        post_list = paginator.page(paginator.num_pages)
    return render(request,
                  'index.html',
                  {'page': page,
                   'post_list': post_list})


class PostDetail(generic.DetailView):
    model = Post
    template_name = 'post_detail.html'