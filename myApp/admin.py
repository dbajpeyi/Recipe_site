from django.contrib import admin
from myApp.models import Recipe

class RecipeAdmin(admin.ModelAdmin):
	prepopulated_fields = {'slug': ['title']}

admin.site.register(Recipe,RecipeAdmin)
