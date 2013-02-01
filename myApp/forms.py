from django.forms import ModelForm
from myApp.models import Recipe

class RecipeForm(ModelForm):
	class Meta:
		model = Recipe
