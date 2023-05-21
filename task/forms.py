from django.forms import ModelForm
from .models import *
class CategoryForm(ModelForm):
    class Meta:
        model = Category
        fields = ['name', 'description']

class TaskForm(ModelForm):
    class Meta:
        model = Task
        fields = '__all__'

