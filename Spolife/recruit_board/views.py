from django.shortcuts import render, redirect, get_object_or_404
from .models import Recruit_Post, Recruit_Comment
from urllib import user
from django.utils import timezone

# 게시글 목록 보여줌
def show(request):
    posts = Recruit_Post.objects.filter().order_by('-date')
    return render(request, 'recruit_board.html', {'posts':posts})


def create(request):
    if request.method == 'POST' or request.method == 'FILES':
        # 입력 내용을 DB에 저장
        # 주황색 name 통일!!
        post = Recruit_Post()
        post.title = request.POST['title']
        post.body = request.POST['body']
        post.date = timezone.now()
        post.author = request.user
        post.category = request.POST['category']
        post.local = request.POST['local']
        post.gender = request.POST['gender']
        post.activity_time = request.POST['activity_time']
        post.is_recruit = request.POST['is_recruit']
        post.save()
    # 입력을 받을 수 있는 html을 갖다 주기
    return render(request, 'create.html')


def delete(request, post_id):
    post = get_object_or_404(Recruit_Post, pk=post_id)
    post.delete()
    return redirect('recruit_boards')


def update(request, post_id):
    post = get_object_or_404(Recruit_Post, pk=post_id)
    if request.method == 'POST' or request.method == 'FILES':
        # 입력 내용을 DB에 저장
        post.title = request.POST['title']
        post.body = request.POST['body']
        post.date = timezone.now()
        post.author = request.user
        post.category = request.POST['category']
        post.local = request.POST['local']
        post.gender = request.POST['gender']
        post.activity_time = request.POST['activity_time']
        post.is_recruit = request.POST['is_recruit']
        post.save()
    else:
        return render(request, 'update.html', {'post':post})


def detail(request, post_id):
    post_detail = get_object_or_404(Recruit_Post, pk=post_id)
    comment_form = Recruit_Comment()
    return render(request, 'detail.html', {'post_detail':post_detail, 'comment_form':comment_form})


def create_comment(request, post_id):
    if request.method == 'POST':
        com = Recruit_Comment()
        com.comment = request.POST['comment']
        com.post = request.user
        com.date = timezone.now()
        com.save()
    return redirect('detail', post_id)


def delete_comment(request, post_id, com_id):
    com = get_object_or_404(Recruit_Comment, pk=com_id)
    com.delete()
    return redirect('detail', post_id)


def update_comment(request, post_id, com_id):
    com = get_object_or_404(Recruit_Comment, pk=com_id)
    if request.method == "POST":
        com.comment = request.POST['comment']
        com.post = request.user
        com.date = timezone.now()
        com.save()
    else:
        return render(request, 'detail.html', {'com':com})