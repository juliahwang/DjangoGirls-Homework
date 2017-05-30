from django.contrib.auth import get_user_model
# from django.http import HttpResponse
from django.shortcuts import render, redirect
# from django.utils import timezone
from .models import Post
# from 다음의 .은 현재 디렉토리 또는 애플리케이션을 의미
# 동일한 디렉토리 내의 파일을 불러올 경우 .을 써준다


User = get_user_model()
# Create your views here.


def post_list(request):
    # return HttpResponse('<html><body>Post List</body></html>')
    posts = Post.objects.all().order_by('-created_date')

    context = {
        'title': 'Post list from post_list view',
        'posts': posts,
    }
    return render(request, 'blog/post_list.html', context=context)


def post_detail(request, pk):
    print('post_detail pk: ', pk)
    # post라는 키값으로 pk또는 id값이 매개변수로 주어진 pk변수와 같은 Post 객체를 전달
    context = {
        'post': Post.objects.get(id=pk)
        # pk는 테이블을 만들 때 자동으로 생성되는 id(primary key)를 장고에서 'pk='으로 작성해도 인식하게끔 해준다.
    }
    return render(request, 'blog/post_detail.html', context=context)


def post_create(request):
    if request.method == 'GET':
        context = {

        }
        return render(request, 'blog/post_create.html', context)
    elif request.method == 'POST':
        data = request.POST
        title = data['title']
        text = data['text']
        user = User.objects.first()
        post = Post.objects.create(
            author=user,
            title=title,
            text=text
        )
        return redirect('post_detail', pk=post.pk)