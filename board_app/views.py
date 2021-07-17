from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import *
from django.utils import timezone
# Create your views here.
from django.http import HttpResponse

# Create your views here.

# 메인페이지 이동
def index(request):
    boards = Board.objects.all().order_by("-pub_date")
    context = {'boards':boards}
    return render(request, 'list.html', context)

# 게시글 상세 페이지 이동
def detail(request, board_id):
    board = Board.objects.get(id=board_id)
    context = {'board':board}
    return render(request, 'detail.html', context)

# 글작성 페이지 이동
def post(request):
    if request.method == "POST":
        author = request.POST['author']
        title = request.POST['title']
        content = request.POST['content']
        pub_date = timezone.now()
        board = Board(author=author, title=title, content=content, pub_date=pub_date)
        board.save()
        return HttpResponseRedirect('/')
    else:
        return render(request, 'post.html')