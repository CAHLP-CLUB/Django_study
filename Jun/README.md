## Python Django Study TIL 3월
중요, 확인
>참고 링크:https://www.youtube.com/watch?v=RWEZITw27Ts&list=PLQFurmxCuZ2RVfilzQB5rCGWuODBf4Qjo

------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
###  2023년 3월 7일 파이썬 스터디 공부

>django-admin, MVC

## django-admin

터미널에 입력

~~~
jango-admin.exe startproject 프로젝트이름
~~~

## MVC

MVC 개발 패턴이라는 개념을 변형해서 

**M**odel**V**iew**C**ontroller
<br>하지만 django에서는 <br>

**M**odel**V**iew**T**emplate

---

<h3>Model</h3><br>데이터베이스에 저장을 하는 과정을 편리하게 해주는 것이 model이다.<br>
<h3>View</h3><br>django에서 계산(인증, 연산)하는 대부분을 담당한다.<br>
<h3>Template</h3><br>HTML, JavaScript, CSS 같은 유저가 실제로 보는 부분에 관계가 있다.<br>

------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
###  2023년 3월 13일 파이썬 스터디 공부

 ~ 작정하고 장고 8강
 
>startapp, git, extends include

## startapp

~~~
python.exe .\manage.py startapp accountapp
~~~
<br>
accountapp 폴더에서 views.py 파일에 작성
~~~
from django.http import HttpResponse
def hello_world(request):
    return HttpResponse("hello world!")
~~~

infact 폴더에 settings.py 파일에서 installed_apps 리스트에 accountapp을 추가<br>
infact 안에 urls.py 에 urlpatterns리스트에 다음과 같이 추가

~~~
path('account/', include('accountapp.urls'))
~~~

## git

깃의 특징 - version control<br>
Rollback, Branch
<br><br>git에서 사용되는 명령어<br>

~~~
add
commit
push
pull
branch
checkout
~~~

우리는 영상과 다르게 github desktop을 사용한다<br>

## extends include

extends은 미리 만들어 놓은 템플릿을 가져와서 채워나가는 식으로 사용<br>
include는 만들고 있는 html 파일에 조그만 조각을 가져와서 박아 넣는  느낌으로 사용<br>
extends는 바탕을 깔아주는 느낌이고 include는 덩어리를 가져와서 붙이는 느낌으로 사용한다.<br><br>extends로 바탕을 만들고 include로 내용을 채우는 식으로 사용한다. 이렇게 만들어진 것이 최종적으로 요청을 받았을 때 보여주는 response view이다.