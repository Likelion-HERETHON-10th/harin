from django.shortcuts import render, redirect, get_object_or_404
from .models import Review_Post, Review_Comment
from urllib import user
from django.utils import timezone

# 게시글 목록 보여줌
def show(request):
    posts = Review_Post.objects.filter().order_by('-date')
    return render(request, 'review_board.html', {'posts':posts})


def create(request):
    if request.method == 'POST' or request.method == 'FILES':
        # 입력 내용을 DB에 저장
        # 주황색 name 통일!!
        post = Review_Post()
        post.title = request.POST['title']
        post.body = request.POST['body']
        post.date = timezone.now()
        post.author = request.user
        post.score = request.POST['score']
        post.photo = request.FILES['review_photo']
        post.save()
    # 입력을 받을 수 있는 html을 갖다 주기
    return render(request, 'create.html')


def delete(request, post_id):
    post = get_object_or_404(Review_Post, pk=post_id)
    post.delete()
    return redirect('review_boards')


def update(request, post_id):
    post = get_object_or_404(Review_Post, pk=post_id)
    if request.method == 'POST' or request.method == 'FILES':
        # 입력 내용을 DB에 저장
        post.title = request.POST['title']
        post.body = request.POST['body']
        post.date = timezone()
        post.author = request.user
        post.score = request.POST['score']
        post.photo = request.FILES['review_photo']
        post.save()
    else:
        return render(request, 'update.html', {'post':post})


def detail(request, post_id):
    post_detail = get_object_or_404(Review_Post, pk=post_id)
    comment_form = Review_Comment()
    return render(request, 'detail.html', {'post_detail':post_detail, 'comment_form':comment_form})


def create_comment(request, post_id):
    if request.method == 'POST':
        com = Review_Comment()
        com.comment = request.POST['comment']
        com.post = request.user
        com.date = timezone.now()
        com.save()
    return redirect('detail', post_id)


def delete_comment(request, post_id, com_id):
    com = get_object_or_404(Review_Comment, pk=com_id)
    com.delete()
    return redirect('detail', post_id)


def update_comment(request, post_id, com_id):
    com = get_object_or_404(Review_Comment, pk=com_id)
    if request.method == "POST":
        com.comment = request.POST['comment']
        com.post = request.user
        com.date = timezone.now()
        com.save()
    else:
        return render(request, 'detail.html', {'com':com})