from django import forms
from .models import TodoModel

class TodoForm(forms.ModelForm):
	class Meta:
		model = TodoModel
		fields = ["task","description"]
		widgets = {"description":forms.Textarea(attrs={"rows":4, "cols":21})}
