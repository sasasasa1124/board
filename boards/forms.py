from django import forms
from .models import Topic


class NewTopicForm(forms.ModelForm):
    message = forms.CharField(
        widget=forms.Textarea(
            attrs={'rows': 5, 'placeholder': 'ここには説明を書いてください'}
        ),
        max_length=4000,
    )

    tex = forms.CharField(
        widget=forms.Textarea(
            attrs={'rows': 5, 'placeholder': 'ここにはTeXコードを記入してください'}
        ),
        max_length=4000,
    )

    class Meta:
        model = Topic
        fields = ['subject', 'message', 'tex']