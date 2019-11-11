from django import forms
from .models import Review


class ReviewForm(forms.ModelForm):
    name = forms.CharField(widget=forms.Textarea, label='Имя')
    text = forms.CharField(widget=forms.Textarea, label='Отзыв')

    class Meta(object):
        model = Review
        exclude = ('id', 'product')
