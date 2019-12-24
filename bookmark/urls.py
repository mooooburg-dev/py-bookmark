from django.urls import path
from .views import BookmarkListView
from .views import BookmarkCreateView

urlpatterns = [
    # 첫 번째 인수인 ''를 보면 bookmark/ 이하 부분이 없다라고 해석 할 수 있음.(루트페이지 역할)
    path('', BookmarkListView.as_view(), name="list"), #함수 형 뷰라면 뷰 이름만 써주면 되지만 클래스 형 뷰일 경우에는 뒤에 .as_view()라고 붙여줘야 정상작동 가능.
    path('add/', BookmarkCreateView.as_view(), name='add'),
]