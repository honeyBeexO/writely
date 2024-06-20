from django.shortcuts import render, get_object_or_404, redirect # type: ignore
from .models import Waffel,CookieDough,Crepe,Cake,Sauce,Topping,Scoop
# Create your views here.

def index(request):
    waffels = Waffel.objects.all()
    creps = Crepe.objects.all()
    cookies = CookieDough.objects.all()
    context = {
        'waffels': waffels,
        'creps':creps,
        'cookies':cookies
        } 
    return render(request,'creamsQuizz/index.html',context)

from django.http import HttpResponseRedirect,Http404 # type: ignore
from django.urls import reverse # type: ignore
from django.views import generic  # type: ignore
from django.utils import timezone # type: ignore
from django.db.models import F,Q  # type: ignore

class WaffelListView(generic.ListView):
    model = Waffel
    template_name = 'creamsQuizz/waffels_list.html'
    context_object_name ='dessert'
    
class CrepesListView(generic.ListView):
    model = Crepe
    template_name = 'creamsQuizz/crepes_list.html'
    context_object_name ='dessert'
    
class CookieDoughsListView(generic.ListView):
    model = CookieDough
    template_name = 'creamsQuizz/cookies_list.html'
    context_object_name ='dessert'

class WaffelDetailView(generic.DetailView):
    model = Waffel
    template_name = 'creamsQuizz/waffel_detail.html'
    context_object_name = 'dessert'
    
# def waffel_detail(request, waffel_id):
#     try:
#         waffel = Waffel.objects.get(pk=waffel_id)
#     except Waffel.DoesNotExist:
#         raise Http404("Waffel not found")
#     context = {
#         'waffel': waffel,
#         'ingredient_categories':{
#             'toppings':Topping.objects.all(),
#             'sauces':Sauce.objects.all(),
#             'cakes':Cake.objects.all(),
#             'scoops':Scoop.objects.all() 
#             }, 
#         }
#     return render(request, 'creamsQuizz/waffel_detail.html', context=context)

# def waffel_vote(request, waffel_id):
        
#     if request.method=='POST':
#         try:
#             waffel = get_object_or_404(Waffel, pk=waffel_id)
#             #selected_toppings = waffel.choice_set.get(pk=request.POST["choice"])
#             selected_toppings = request.POST.getlist('Toppings')
#             selected_sauces = request.POST.getlist('Sauces')
#             selected_cakes = request.POST.getlist('Cakes')
#             selected_scoops = request.POST.getlist('Scoops')
#             # Ensure at least one ingredient is selected
#             print(selected_toppings)
#             print(selected_sauces)
#             print(selected_cakes)
#             print(selected_scoops)
#             if not (selected_toppings or selected_sauces or selected_cakes or selected_scoops):
#                 raise ValueError("You must select at least one ingredient.")

#         except (KeyError, ValueError, Waffel.DoesNotExist) as e:
#             # Redisplay the question voting form.
#             error_message = str(e)
#             return render(
#                 request,
#                 "creamsQuizz/waffel_detail.html",
#                 {
#                     "dessert": waffel,
#                     "error_message": e,
#                 },
#             )
#         else:
#             # selected_choice.votes = F("votes") + 1
#             # selected_choice.save()
#             # Always return an HttpResponseRedirect after successfully dealing
#             # with POST data. This prevents data from being posted twice if a
#             # user hits the Back button.
#             correct_toppings = waffel.toppings.values_list('id',flat=True)
#             correct_sauces = waffel.sauces.values_list('id',flat=True)
#             correct_cakes = waffel.cakes.values_list('id',flat=True)
#             correct_scoops = waffel.scoops.values_list('id',flat=True)
#             if(set(correct_toppings) == set(selected_toppings) and 
#                set(correct_sauces) == set(selected_sauces) and 
#                set(correct_cakes) == set(correct_cakes) and 
#                set(correct_scoops) == set(selected_scoops)
#                ):
#                 return HttpResponseRedirect(reverse("polls:results", args=(waffel.id,)))
#             else:
#                 return render(
#                 request,
#                 "creamsQuizz/waffel_detail.html",
#                 {
#                     "dessert": waffel,
#                     "error_message": 'Incorrect Choices',
#                 },
#             )
#     else:
#         return render(
#                 request,
#                 "creamsQuizz/waffel_detail.html",
#                 {
#                     "dessert": waffel,
#                     "error_message": 'Not a proper post request',
#                 },
#             )
    
def waffel_detail(request, waffel_id):
    waffel = get_object_or_404(Waffel, pk=waffel_id)
    context = {
        'waffel': waffel,
        'ingredient_categories': {
            'toppings': Topping.objects.all(),
            'sauces': Sauce.objects.all(),
            'cakes': Cake.objects.all(),
            'scoops': Scoop.objects.all()
        },
    }
    return render(request, 'creamsQuizz/waffel_detail.html', context=context)

def waffel_vote(request, waffel_id):
    if request.method == 'POST':
        try:
            waffel = get_object_or_404(Waffel, pk=waffel_id)

            selected_toppings = request.POST.getlist('toppings')
            selected_sauces = request.POST.getlist('sauces')
            selected_cakes = request.POST.getlist('cakes')
            selected_scoops = request.POST.getlist('scoops')

            if not (selected_toppings or selected_sauces or selected_cakes or selected_scoops):
                raise ValueError("You must select at least one ingredient.")

            correct_toppings = list(waffel.toppings.values_list('id', flat=True))
            correct_sauces = list(waffel.sauces.values_list('id', flat=True))
            correct_cakes = list(waffel.cakes.values_list('id', flat=True))
            correct_scoops = list(waffel.scoops.values_list('id', flat=True))

            if (set(map(int, selected_toppings)) == set(correct_toppings) and
                set(map(int, selected_sauces)) == set(correct_sauces) and
                set(map(int, selected_cakes)) == set(correct_cakes) and
                set(map(int, selected_scoops)) == set(correct_scoops)):
                return redirect(reverse("quizz:waffel-result", args=(waffel.id,)))
            else:
                error_message = "Incorrect choices. Please try again."
                return render(
                    request,
                    "creamsQuizz/waffel_detail.html",
                    {
                        "waffel": waffel,
                        "ingredient_categories": {
                            'toppings': Topping.objects.all(),
                            'sauces': Sauce.objects.all(),
                            'cakes': Cake.objects.all(),
                            'scoops': Scoop.objects.all()
                        },
                        "error_message": error_message,
                    },
                )
        except (KeyError, ValueError) as e:
            error_message = str(e)
            return render(
                request,
                "creamsQuizz/waffel_detail.html",
                {
                    "waffel": waffel,
                    "ingredient_categories": {
                        'toppings': Topping.objects.all(),
                        'sauces': Sauce.objects.all(),
                        'cakes': Cake.objects.all(),
                        'scoops': Scoop.objects.all()
                    },
                    "error_message": error_message,
                },
            )
    else:
        raise Http404("Invalid request method")

class WaffelResultView(generic.DetailView):
    model = Waffel
    template_name = 'creamsQuizz/waffel_result.html'
    context_object_name = 'waffel'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Additional context if needed
        return context