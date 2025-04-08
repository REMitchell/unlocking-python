from django.shortcuts import render
from posts.models import Post
from django.contrib.auth.models import User
from django.http import HttpResponseNotFound


def all_posts(request):
    posts = Post.objects.all()
    post_type = str(type(Post.objects))
    return render(request, 'posts.html', {'posts': posts, 'post_type': post_type})


def profile(request):
    posts = Post.objects.filter(user=request.user)
    return render(request, 'profile.html', {'posts': posts, 'user': request.user})


def profile_by_id(request, user_id):
    posts = Post.objects.filter(user=user_id)

    try:
        user = User.objects.get(id=user_id)
    except User.DoesNotExist as e:
        return HttpResponseNotFound(f'User not found')

    return render(request, 'profile.html', {'posts': posts, 'user': user})


'''
def profile_by_id(request, user_id):
    posts = Post.objects.filter(user=user_id)
    return render(request, 'profile.html', {
        'posts': posts,
        'user': request.user
        })
'''
