from django import forms
from .models import *

#class AddPostForm(forms.ModelForm):
#    title = forms.CharField(max_length=250, label='Заголовок')
#    slug = forms.SlugField(max_length=250)
#    content = forms.CharField(widget=forms.Textarea(attrs={'cols':60,'rows':10}))
#    is_published = forms.BooleanField(required=False, initial=True)
#    cat = forms.ModelChoiceField(queryset=Category.objects.all(),empty_label='Категория не выбрана')

class AddPostForm(forms.ModelForm):
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        self.fields['cat'].empty_label = 'Категория не выбрана'

    class Meta:
        model = Blog
        fields =['title', 'slug', 'content','is_published', 'cat']
        widgets={
            'title': forms.TextInput(attrs={'class': 'form-input'}),
            'content': forms.Textarea(attrs={'cols': 60,'rows': 10})
        }