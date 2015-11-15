from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.utils import timezone
from django.core.urlresolvers import reverse

from .models import BlogPost


def index(request):
    all_blog_posts = BlogPost.objects.order_by('-pub_date')
    context = {
        'all_blog_posts': all_blog_posts,
    }
    return render(request, 'Blog/index.html', context)

def detail(request, post_id):
    post = get_object_or_404(BlogPost, pk=post_id)
    context = {
        'post': post
    }
    return render(request, 'Blog/detail.html', context)

def new(request):
    if request.method == 'GET':
        return render(request, 'Blog/new.html')
    else:
        new_post_text = request.POST['post_text']
        new_blog_post = BlogPost(post_text=new_post_text, pub_date=timezone.now())
        new_blog_post.save()
        return HttpResponseRedirect(reverse('blog:detail', args=(new_blog_post.id,)))
