from django import forms
from .models import *

class AddPostForm(forms.Form):
    title = forms.CharField(max_length=250, label='Заголовок')
    slug = forms.SlugField(max_length=250)
    content = forms.CharField(widget=forms.Textarea(attrs={'cols':60,'rows':10}))
    is_published = forms.BooleanField(required=False, initial=True)
    cat = forms.ModelChoiceField(queryset=Category.objects.all(),empty_label='Категория не выбрана')