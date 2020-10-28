from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.views.decorators.http import require_POST

from .forms import PostForm
from .models import BlogPost


def index(request):
    return render(request, 'contact/base.html')

def timeline_view(request, username):
    post_form = PostForm()
    user = get_object_or_404(User, username=username)
    posts = BlogPost.objects.filter(user=user).order_by('-created_at')
    return render(request, 'contact/timeline.html', {'posts': posts, 'post_form': post_form, 'user': user})

@login_required
@require_POST
def create_post_view(request):
    post_form = PostForm(request.POST)
    if post_form.is_valid():
        post = post_form.save(commit=False)
        post.user = request.user
        post.save()
    return HttpResponseRedirect(reverse('contact:timeline', kwargs={'username': request.user.username}))


@login_required
@require_POST
def delete_post_view(request, post_id):
    post = get_object_or_404(BlogPost, id=post_id, user=request.user)
    post.delete()
    return HttpResponseRedirect(reverse('contact:timeline', kwargs={'username': request.user.username}))


def post_view(request, post_id):
    post = get_object_or_404(BlogPost, id=post_id)
    return render(request, 'contact/post.html', {'post': post})