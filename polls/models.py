from django.db import models

# Create your models here.
# 모델 생성
# 이 모델에 맞는 테이블을 만들기
# 모델을 테이블에 써주기 위한 마이그레이션을 만들다. 
# 질문: 여름에 놀러간다면 어디로?
#산
#강
#바다
#도심호캉스 

class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'제목:{self.question_text}, 날짜: {self.pub_date}'

    
class Choice(models.Model):   
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
    def __str__(self):
        return f'{self.choice_text}'

# choice에서는 question으로 바로 접근 가능, 하지만 반대는 불가