from django import forms
from .models import Person


class PersonForm(forms.ModelForm):

    class Meta:
        model = Person
        fields = ['photo', 'first_name', 'last_name',
                  'email', 'cpf', 'city', 'uf']
