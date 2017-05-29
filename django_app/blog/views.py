from django.http import HttpResponse
from django.shortcuts import render
from django.utils import timezone
from .models import Post
# from 다음의 .은 현재 디렉토리 또는 애플리케이션을 의미
# 동일한 디렉토리 내의 파일을 불러올 경우 .을 써준다

# Create your views here.

def post_list(request):
    # return HttpResponse('<html><body>Post List</body></html>')
    posts = Post.objects.filter(
        published_date__lte=timezone.now()).order_by('published_date')

    context = {
        'title': 'Post list from post_list view',
        'posts': posts,
    }
    return render(request, 'blog/post_list.html', context=context)

