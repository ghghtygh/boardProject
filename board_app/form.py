
from django import forms
from django_summernote.fields import SummernoteTextField

from board_app.models import Board

from django_summernote.widgets import SummernoteWidget

# class PostForm(forms.Form):
#     title = forms.CharField()
#     content = forms.CharField(widget=forms.Textarea)
#     author = forms.CharField()

class PostForm(forms.ModelForm):
    class Meta:
        model = Board
        # fields = '__all__'
        fields = ['title', 'content', 'author']  # '__all__' : 전체 필드
        widgets = {
            'content' : SummernoteWidget(),
            # 'content' : SummernoteTextField(),
        }