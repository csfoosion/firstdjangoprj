#form.py를 이용해 폼을 생성할때 반드시 아래 코드 작성
from django import forms
#Post 모델에 대한 폼을 생성하기 위해 Post 모델 코드
from .models import Post

#모델에서 models.Model을 괄호안에 넣었듯이
#폼 생성에서도 class 폼이름(forms.ModelForm): 으로 시작해야함
class PostForm(forms.ModelForm):
    
    #폼의 상세정보 설정을 위해 class PostFom 내부에
    #class Meta 를 다시 만들어야 함. Meta에 정으한 정보대로 폼이 작성됨
    class Meta:
        #이 폼의 타겟이 Post 모델(Post모델에 적재 예정)
        model = Post
        #실제로 사용자에게 입력받을 컬럼은 title과 text만
        #author은 자동으로 계정 연동, create_date는 서버시간
        #published_date 은 publishing할 때 추후입력
        #pk는 자동으로 글 하나 생성시마다 하나씩 부여
        fields = ('title', 'text',)