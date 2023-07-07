from django import forms
from .models import Question, Answer

class QuestionForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = ['title', 'text']
        labels = {
            'title': 'Title',
            'text': 'Text',
        }


class PostForm(forms.Form):
    title = forms.CharField(label='Title', max_length=128)
    text = forms.CharField(widget=forms.Textarea(attrs={'label': 'Text'}))

