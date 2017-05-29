from django.http import HttpResponse
from django.shortcuts import render
from django.utils import timezone
from blog.models import Post

# Create your views here.

def post_list(request):
    # return HttpResponse('<html><body>Post List</body></html>')
    posts = Post.objects.filter(
        published_date__lte=timezone.now())

    context = {
        'title': 'Postlist from post_list view',
        'posts': posts,
    }
    return render(request, 'blog/post_list.html', context=context)

