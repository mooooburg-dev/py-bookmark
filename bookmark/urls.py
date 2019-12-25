from django.urls import path
from .views import BookmarkListView
from .views import BookmarkCreateView
from .views import BookmarkDetailView
from .views import BookmarkUpdateView
from .views import BookmarkDeleteView

urlpatterns = [
    # 첫 번째 인수인 ''를 보면 bookmark/ 이하 부분이 없다라고 해석 할 수 있음.(루트페이지 역할)
    path('', BookmarkListView.as_view(), name="list"), #함수 형 뷰라면 뷰 이름만 써주면 되지만 클래스 형 뷰일 경우에는 뒤에 .as_view()라고 붙여줘야 정상작동 가능.
    path('add/', BookmarkCreateView.as_view(), name='add'),

    # [<int:pk>] 앞쪽 int는 타입(정확히는 컨버터)라고 부르는 기능이며 클래스 형태,
    # 뒤쪽은 컨버터를 통해 반환받은 값 혹은 패턴에 일치하는 값의 변수명.
    # 컨버터는 생략하거나 커스텀 컨버터를 만들어 넣을 수 있음.
    # 기본 제공 컨버터 : str, int, slug, uuid, path
    path('detail/<int:pk>/', BookmarkDetailView.as_view(), name='detail'),

    path('update/<int:pk>/', BookmarkUpdateView.as_view(), name='update'),

    path('delete/<int:pk>/', BookmarkDeleteView.as_view(), name='delete'),

]