# Create your views here.
from django.http import HttpResponse,HttpResponseRedirect
from myApp.models import Recipe
from myApp.forms import RecipeForm
from django.template import loader, Context
from django.core.context_processors import csrf

def index(request):
	list_of_recipes = Recipe.objects.order_by('id')[:5]
	template = loader.get_template('myApp/index.html')
	context = Context({'list_of_recipes': list_of_recipes,})
	
	return HttpResponse(template.render(context))

def detail(request,rec_id):
	detail = Recipe.objects.get(id=rec_id)
	instruct = detail.instructions
	ingred = detail.ingredients
	template = loader.get_template('myApp/details.html')
	context = Context({'instruct': instruct,'ingred':ingred,})
	return HttpResponse(template.render(context))	

def add(request):
	if request.method == 'POST':
		form = RecipeForm(request.POST)
		if form.is_valid():
		#	title = request.POST.get('title','')
		#	ingredients = request.POST.get('ingredients','')
		#	instructions = request.POST.get('instructions','')
		#	recipe_obj = Recipe(title=title,instruction=instruction,ingredients=ingredients)
			form.save()
			#redirect
			return HttpResponse("Thank you")
		else:
			return HttpResponse("Form Not Valid")
	else:
		form = RecipeForm()
	        
		context = Context({'form':form,})
		context.update(csrf(request))
		template = loader.get_template('myApp/add.html')
		return HttpResponse(template.render(context))
	
