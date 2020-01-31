from django.shortcuts import render, get_object_or_404
from django.views import generic

from .models import Post


def post_detail(request, post_id):
    post_content = get_object_or_404(Post, pk=post_id)
    context = {'post': post_content}
    return render(request, 'posts/post_detail.html', context)


def posts_list(request):
    post_list = Post.objects.all()
    context = {'post_list': post_list}
    return render(request, 'posts/posts_list.html', context)


class PostListView(generic.ListView):
    template_name = 'posts/posts_list.html'
    context = 'latest_question_list'

    def get_queryset(self):
        return Post.objects.order_by('pub_date')[:10]


class PostDetailView(generic.DetailView):
    model = Post
    template_name = 'posts/post_detail.html'
