from django.urls import path # path 함수를 django.ulrs 모듈에서 가져온다. 'path' 함수는 URL 패턴을 정의하고 이를 처리할 뷰와 연결하는 데 사용한다. 
from . import views # 이 줄은 현재 디렉토리의 'views' 모듈을 가져온다. 'views' 모듈에는 URL 요청을 처리하는 뷰 함수들이 정의되어 있다. 

urlpatterns = [
    path('', views.index, name='index'),
    path('some_url', views.some_url)
]
# views.index 는 루트 URL로 요청이 들어올 때 호출될 뷰 함수를 지정한다. 여기서는 views 모듈의 index 함수가 호출된다.
# name='index'는 이 URL 패턴에 index 라는 이름을 부여한다. URL이름은 템플릿에서 URL을 참조하거나, 뷰 함수나 다른 곳에서 URL을 역으로 찾을 때 유용하다. 