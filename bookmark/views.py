from django.views.generic.list import ListView
from .models import Bookmark
from django.shortcuts import render

# Create your views here.
# ListView를 상속해 사용함
# Bookmark 모델을 임포트 하고 클래스 안에 model = Bookmark라는 구문을 이용해 모델을 설정함.
class bookmarkListView(ListView):
    model = Bookmark