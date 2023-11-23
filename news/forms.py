from .models import Category
from django import forms


class CreateCategoryModelForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = '__all__'
