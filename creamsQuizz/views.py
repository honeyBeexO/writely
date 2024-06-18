from django.shortcuts import render, get_object_or_404 # type: ignore
from .models import Waffel,CookieDough,Crepe,Cake,Sauce,Topping,Icecream
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

from django.http import HttpResponseRedirect,Http404
from django.urls import reverse
from django.views import generic 
from django.utils import timezone
from django.db.models import F,Q 

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
    template_name = ''



def get_feedback(selected,correct):
    feedback = []
    print(selected)
    print(correct)
    for s in selected:
                if s in correct:
                    feedback.append({
                        'sauce':s,
                        'alert':'success',
                    })
                else:
                    feedback.append({
                        'sauce':s,
                        'alert':'danger',
                    })
    return feedback

def waffles_quizz(request, waffel_id):
    waffel = get_object_or_404(Waffel, pk=waffel_id)
    if request.method == 'POST':
        form = WaffleQuizForm(request.POST)
        if form.is_valid():
            selected_sauces = form.cleaned_data['sauces']
            selected_toppings = form.cleaned_data['toppings']
            selected_cakes = form.cleaned_data['cakes']
            selected_scoops = form.cleaned_data['scoops']

            correct_sauces = waffel.sauces.all()
            correct_toppings = waffel.toppings.all()
            print(correct_toppings)
            correct_cakes = waffel.cakes.all()
            correct_scoops = waffel.scoops.all()
            
            t_feedback = get_feedback(set(selected_toppings),set(correct_toppings))
            #s_feedback = get_feedback(selected_sauces,correct_sauces)
            #c_feedback = get_feedback(selected_cakes,correct_cakes)
            #sc_feedback = get_feedback(selected_scoops,correct_scoops)

                    
            context = {
                'waffel': waffel,
                'selected_sauces': selected_sauces,
                'selected_toppings': selected_toppings,
                'selected_cakes': selected_cakes,
                'selected_scoops':selected_scoops,
                'correct_sauces': correct_sauces,
                'correct_toppings': correct_toppings,
                'correct_scoops': correct_scoops,
                'is_correct': (set(selected_sauces) == set(correct_sauces) and
                               set(selected_toppings) == set(correct_toppings) and
                               set(selected_cakes) == set(correct_cakes)),
                't_feedback':t_feedback,
                #'s_feedback':s_feedback,
                #'c_feedback':c_feedback,
                #'sc_feedback':sc_feedback,
            }
            return render(request, 'creamsQuizz/result.html', context)
    else:
        form = WaffleQuizForm()

    context = {
        'waffel': waffel,
        'form': form,
    }
    return render(request, 'creamsQuizz/quiz.html', context)