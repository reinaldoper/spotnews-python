from .models import Category, News
from django import forms


class CreateCategoryModelForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = '__all__'


class CreateNewsModelForm(forms.ModelForm):
    class Meta:
        model = News
        fields = '__all__'
