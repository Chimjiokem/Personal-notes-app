from django import forms
from .models import Title, Content

class TitleForm(forms.ModelForm):
    class Meta:
        model = Title
        fields = ('title',)

class ContentForm(forms.ModelForm):
    class Meta:
        model = Content
        fields = ('content',)