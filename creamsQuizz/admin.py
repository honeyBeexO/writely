from django.contrib import admin # type: ignore

# Register your models here.
from django.contrib import admin # type: ignore
from .models import Sauce,Cake,Topping,Icecream,Waffel,CookieDough,Crep
# Register your models here.
# admin.site.register(models.Sauce)
# admin.site.register(models.Topping)
# admin.site.register(models.Cake)
# admin.site.register(models.Icecream)
#admin.site.register(Crep)

class BaseDessertInline(admin.TabularInline):
    extra = 1
# Function to create inline classes dynamically
def create_inline(_model, related_field):
    class Inline(BaseDessertInline):
        model = getattr(_model, related_field).through
    return Inline

# Create inline classes for Waffel
WaffelSauceInline = create_inline(Waffel, 'sauces')
WaffelToppingInline = create_inline(Waffel, 'toppings')
WaffelCakeInline = create_inline(Waffel, 'cakes')
WaffelScoopsInline = create_inline(Waffel, 'scoops')

# Create inline classes for Crep
CrepSauceInline = create_inline(Crep, 'sauces')
CrepToppingInline = create_inline(Crep, 'toppings')
CrepCakeInline = create_inline(Crep, 'cakes')
CrepScoopsInline = create_inline(Crep, 'scoops')

# Create inline classes for CookieDough
CookieDoughSauceInline = create_inline(CookieDough, 'sauces')
CookieDoughToppingInline = create_inline(CookieDough, 'toppings')
CookieDoughCakeInline = create_inline(CookieDough, 'cakes')
CookieDoughScoopsInline = create_inline(CookieDough, 'scoops')

@admin.register(Waffel)
class WaffelAdmin(admin.ModelAdmin):
    inlines = [WaffelSauceInline, WaffelToppingInline, WaffelCakeInline, WaffelScoopsInline]
    list_display = ('name', 'type', 'description')
    list_filter = ('type',)
    search_fields = ('name', 'description')
    exclude = ('sauces', 'toppings', 'cakes', 'scoops')

@admin.register(Crep)
class CrepAdmin(admin.ModelAdmin):
    inlines = [CrepSauceInline, CrepToppingInline, CrepCakeInline, CrepScoopsInline]
    list_display = ('name', 'type', 'description')
    list_filter = ('type',)
    search_fields = ('name', 'description')
    exclude = ('sauces', 'toppings', 'cakes', 'scoops')   

@admin.register(CookieDough)
class CookieDoughAdmin(admin.ModelAdmin):
    inlines = [CookieDoughSauceInline, CookieDoughToppingInline, 
               CookieDoughCakeInline, CookieDoughScoopsInline
            ]
    list_display = ('name', 'type', 'description')
    list_filter = ('type',)
    search_fields = ('name', 'description')
    exclude = ('sauces', 'toppings', 'cakes','scoops')

@admin.register(Sauce)
class SauceAdmin(admin.ModelAdmin):
    list_display = ('name',)

@admin.register(Topping)
class ToppingAdmin(admin.ModelAdmin):
    list_display = ('name',)

@admin.register(Cake)
class CakeAdmin(admin.ModelAdmin):
    list_display = ('name',)

@admin.register(Icecream)
class IcecreamAdmin(admin.ModelAdmin):
    list_display = ('name', 'type')
    list_filter = ('type',)
    search_fields = ('name',)

