from django.contrib import admin # type: ignore

# Register your models here.
from django.contrib import admin # type: ignore
from .models import Sauce,Cake,Topping,Icecream,Waffel
# Register your models here.
# admin.site.register(models.Sauce)
# admin.site.register(models.Topping)
# admin.site.register(models.Cake)
# admin.site.register(models.Icecream)
# admin.site.register(models.Waffel)

class SauceInline(admin.TabularInline):
    model = Waffel.sauces.through
    extra = 1

class ToppingInline(admin.TabularInline):
    model = Waffel.toppings.through
    extra = 1

class CakeInline(admin.TabularInline):
    model = Waffel.cakes.through
    extra = 1
    
class ScoopsInline(admin.TabularInline):
    model = Waffel.scoops.through
    extra = 1

@admin.register(Waffel)
class WaffelAdmin(admin.ModelAdmin):
    inlines = [SauceInline, ToppingInline, CakeInline,ScoopsInline]
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