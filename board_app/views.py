from django.shortcuts import render
from django.http import HttpResponseRedirect

from .form import PostForm
from .models import *
from django.utils import timezone

from django.http import JsonResponse
from django.http import HttpResponse

# Create your views here.

# 메인페이지 이동
def index(request):
    boards = Board.objects.all().order_by("-pub_date")
    context = {'boards':boards}
    return render(request, 'list.html', context)

# 게시글 상세페이지 이동
def detail(request, board_id):
    board = Board.objects.get(id=board_id)
    context = {'board':board,'mode':'detail'}
    return render(request, 'detail.html', context)

# 게시글 수정페이지 이동
def modify(request, board_id):
    board = Board.objects.get(id=board_id)
    context = {'board':board,'mode':'modify'}
    return render(request, 'detail.html', context)

# 게시글 삭제
def delete(reuqest, board_id):
    #result = ""
    #return HttpResponse(result, content_type="text/plain")

    return JsonResponse({"result":"success"})

# 글작성 페이지 이동
def post(request):
    if request.method == "POST":
        # author = request.POST['author']
        # title = request.POST['title']
        # content = request.POST['content']
        # pub_date = timezone.now()
        # board = Board(author=author, title=title, content=content, pub_date=pub_date)
        # board.save()
        # return HttpResponseRedirect('/')

        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            # 그냥 Form 사용
            # board = Board(**form.cleaned_data)
            # board.pub_date = timezone.now()
            # board.save()

            # ModelForm 사용
            board = form.save(commit=False) # 중복 DB save 방지
            board.pub_date = timezone.now()

            board.save()
            return HttpResponseRedirect('/')
    else:
        form = PostForm()
        context = {
            'form' : form
        }
        return render(request, 'post.html', context)