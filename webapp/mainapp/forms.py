from .models import Contacts
from django.forms import ModelForm, TextInput, DateTimeInput

class ContactsForm(ModelForm):
    class Meta:
        model=Contacts
        fields = ['first_name','second_name','address','tel_number','registration_date']

        widgets={
            'first_name': TextInput(attrs={
                'class':'form-control',
                'placeholder':'Имя'

            }),
            'second_name': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Фамилия'

            }),
            'address': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Адрес'

            }),
            'tel_number': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'tel'

            }),
            'registration_date': DateTimeInput(attrs={
                'class': 'form-control',


            }),
        }