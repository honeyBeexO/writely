from django import forms # type: ignore
from .models import Sauce, Topping, Cake, Icecream

class WaffleQuizForm(forms.Form):
    sauces = forms.ModelMultipleChoiceField(
        queryset=Sauce.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=False,
        label="Sauces"
    )
    toppings = forms.ModelMultipleChoiceField(
        queryset=Topping.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=False,
        label="Toppings"
    )
    cakes = forms.ModelMultipleChoiceField(
        queryset=Cake.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=False,
        label="Cakes"
    )
    icecreams = forms.ModelMultipleChoiceField(
        queryset=Icecream.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=False,
        label="Gelato"
    )