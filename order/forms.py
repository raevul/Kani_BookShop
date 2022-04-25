from django import forms
# from main.models import Book   ->  Form
from .models import Order


""" Создание формочек с помощью Form """
# class CreateOrderForm(forms.Form):
#     book = forms.ModelChoiceField(Book.objects.all())
#     phone = forms.CharField(max_length=13)
#     address = forms.CharField(widget=forms.Textarea)
#     city = forms.CharField(max_length=100)
#     email = forms.EmailField()


""" Создание формочек с помощью ModelForm """


class CreateOrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = '__all__'

    def clean_phone(self):
        data = self.cleaned_data
        phone = data.get('phone')
        if not phone.startswith('+996'):
            raise forms.ValidationError('Number should start with +996')
        if len(phone) != 13:
            raise forms.ValidationError('Invalid phone number')
        return phone

