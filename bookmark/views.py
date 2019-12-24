from django.views.generic.list import ListView
from django.views.generic.edit import CreateView
from django.views.generic.detail import DetailView

from .models import Bookmark
from django.urls import reverse_lazy
from django.shortcuts import render

# Create your views here.

class BookmarkCreateView(CreateView):
    model = Bookmark    # 어떤 모델의 입력을 받을 것인지 결정해야 하기 때문에..
    fields = ['site_name', 'url']   # 어떤 필드들을 입력받을 것인지 설정하는 부분
    success_url = reverse_lazy('list')  # success_url은 글쓰기를 완료하고 이동할 페이지. 보통은 상세 페이지로 이동하지만 success_url의 사용법을 알기 위해 목록 페이지로 설정
    template_name_suffix = '_create'    # 사용할 템플릿의 접미사만 변경하는 설정값. 기본으로 설정되어 이는 템플릿 이름들은 모델명 _xxx 형태임.
                                        # CreateView와 UpdateView는 form이 접미사인데 이걸 변경해서 bookmark_create라는 이름의 템플릿 파일을 사용하도록 설정한 것.

# ListView를 상속해 사용함
# Bookmark 모델을 임포트 하고 클래스 안에 model = Bookmark라는 구문을 이용해 모델을 설정함.
class BookmarkListView(ListView):
    model = Bookmark

# 확인 기능 화면
class BookmarkDetailView(DetailView):
    model = Bookmark