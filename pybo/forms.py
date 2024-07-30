from django import forms
from pybo.models import Question


class QuestionForm(forms.ModelForm):
    class Meta:
        model = Question  # 사용할 모델
        fields = ['subject', 'content', 'public_method',
                  'issued_date', 'expiry_date', 'push']  # QuestionForm에서 사용할 Question 모델의 속성
        labels = {
            'subject': 'タイトル',
            'content': '내용',
        }
widgets = {
            'public_method': forms.RadioSelect,
            'push': forms.RadioSelect,
            'issued_date': forms.DateTimeInput(format='%Y-%m-%d %H:%M'),
            'expiry_date': forms.DateTimeInput(format='%Y-%m-%d %H:%M'),
        }




