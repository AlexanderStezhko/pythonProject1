from django.db import models

# Create your models here.
class Contacts(models.Model):
    first_name=models.CharField('Имя',max_length=30)
    second_name=models.CharField('Фамилия',max_length=30)
    address=models.CharField('Адрес',max_length=250)
    tel_number=models.CharField('Номер телефона',max_length=30)
    registration_date=models.DateTimeField('Дата регистрации')


    def __str__(self):
        return f'Contacts: {self.first_name} {self.second_name} '

    def get_absolute_url(self):
        return f'/{self.id}'


    class Meta:
        verbose_name='Контакт'
        verbose_name_plural='Контакты'