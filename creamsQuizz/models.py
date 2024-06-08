from django.db import models # type: ignore

# Create your models here.

class Sauce(models.Model):
    MILK_CHOCOLATE = 'Milk Chocolate Sauce'
    WHITE_CHOCOLATE = 'White Chocolate Sauce'
    WHITE_CHOCOLATE_HAZELNUT= 'White Chocolate Hazelnut Spread'
    CARAMEL = 'Caramel Sauce'
    CREAMSATELLA = 'Creams-a\'tella Sauce'
    TOFFEE = 'Toffee Sauce'
    MANGO = 'Mango Sauce'
    STRAWBERRY = 'Strawberry Sauce'
    LEMON_CURD = 'Lemon Curd Sauce'
    LOTUS_BISCOFF = 'Lotus Biscoff Sauce'
    BLUE_BUBBLEGUM = 'Blue Bubblegum Sauce'

    SAUCE_CHOICES = [
        (MILK_CHOCOLATE, 'Milk Chocolate Sauce'),
        (WHITE_CHOCOLATE, 'White Chocolate Sauce'),
        (WHITE_CHOCOLATE_HAZELNUT, 'White Chocolate Hazelnut Spread'),
        (CARAMEL, 'Caramel Sauce'),
        (CREAMSATELLA, 'Creams-a\'tella Sauce'),
        (TOFFEE, 'Toffee Sauce'),
        (MANGO, 'Mango Sauce'),
        (STRAWBERRY, 'Strawberry Sauce'),
        (LEMON_CURD, 'Lemon Curd Sauce'),
        (LOTUS_BISCOFF, 'Lotus Biscoff Sauce'),
        (BLUE_BUBBLEGUM, 'Blue Bubblegum Sauce')
    ]

    name = models.CharField(
        max_length=256,
        unique=True,
        choices=SAUCE_CHOICES,
        help_text="Enter a sauce name"
    )

    def __str__(self):
        return self.name

class Topping(models.Model):
    MILK_CHOCOLATE = 'Milk Chocolate Shavings'
    WHITE_CHOCOLATE = 'White Chocolate Shavings'
    STRAWBERRY = 'Strawberry Slices'
    BANANA = 'Banana Slices'
    LOTUSBISCOFF = 'Lotus Biscoff Crumbs'
    OREOCRUMBS = 'Oreo Crumbs'
    COOKIEDOUGHCRUMBS = 'Cookie Dough Crumbs'
    WHITEBUENO = 'White Kinder Bueno'
    MILKBUENO = 'Milk Kinder Bueno'
    OREO = 'Oreo Cookies'
    ROCHER = 'Ferrero Rocher'
    MERINGUE = 'Crushed Meringue'
    LOTUS_BISCOFF = 'Lotus Biscoff Sauce'
    SPRINKLES = '100 x 100 Sprinkles'
    FUDGECUBE = 'Fudge Cubes'
    MARSHMALLOWS = 'Mini Marshmallows'
    CUSTARD = 'Custard'
    APPLEFILLING = 'Apple Filling'
    BLACKCHERRY = 'Black Cherry'
    SMARTIES = 'Smarties'
    AERO_MINT_BUBBLE = 'Aero Mint Bubble'
    JAMMIE_DODGER = 'Jammie Dodger'
    ROLO = 'Rolo'
    NUTS = 'Chopped Nuts'
    WAFER = 'Cream\'s Wafer'
    SOFT_SERVE= 'Soft Serve'
    BUTTER = 'Butter'
    SUGAR = 'Sugar'
    ICE_SUGAR = 'Icing Sugar'

    TOPPINGS_CHOICES = [
        (STRAWBERRY, 'Strawberry Slices'),
        (BANANA, 'Banana Slices'),
        (LOTUSBISCOFF, 'Lotus Biscoff Crumbs'),
        (OREOCRUMBS, 'Oreo Crumbs'),
        (COOKIEDOUGHCRUMBS, 'Cookie Dough Crumbs'),
        (WHITEBUENO, 'White Kinder Bueno'),
        (MILKBUENO, 'Milk Kinder Bueno'),
        (OREO, 'Oreo Cookies'),
        (ROCHER, 'Ferrero Rocher'),
        (MERINGUE, 'Crushed Meringue'),
        (LOTUS_BISCOFF, 'Lotus Biscoff Sauce'),
        (SPRINKLES, '100 x 100 Sprinkles'),
        (FUDGECUBE, 'Fudge Cubes'),
        (MARSHMALLOWS, 'Mini Marshmallows'),
        (CUSTARD, 'Custard'),
        (APPLEFILLING, 'Apple Filling'),
        (BLACKCHERRY, 'Black Cherry'),
        (SMARTIES, 'Smarties'),
        (AERO_MINT_BUBBLE, 'Aero Mint Bubble'),
        (JAMMIE_DODGER, 'Jammie Dodger'),
        (ROLO, 'Rolo'),
        (WAFER,WAFER),
        (NUTS,NUTS),
        (SOFT_SERVE,SOFT_SERVE),
        (BUTTER,BUTTER),
        (SUGAR,SUGAR),
        (ICE_SUGAR,ICE_SUGAR),
        (MILK_CHOCOLATE,MILK_CHOCOLATE),
        (WHITE_CHOCOLATE,WHITE_CHOCOLATE)
    ]

    name = models.CharField(
        max_length=256,
        unique=True,
        choices=TOPPINGS_CHOICES,
        help_text="Enter a topping name"
    )

    def __str__(self):
        return self.name
    
class Cake(models.Model):
    CAREMEL_APPLE='Caramel Apple Crumble Pie'
    CARROT='Carrot Cake'
    BELGIAN='Belgian Chocolate Cake (V)'
    RED_VELVET='Red Velvet Chocolate Fudge Cake'
    LEMON_CHEESECAKE='Lemon Meringue Cheesecake'
    VANILLA_CHEESECAKE='Madagascan Vanilla Cheesecake'
    WHITE_CHOC_CAKE='White Chocolate & Raspberry Cheesecake'
    RAINBOW='Rainbow Cake'
    TRIPLE_BROWNIE='Triple Choc Brownie'
    DOUGHNUT = 'Doughnut'
    

    CAKE_CHOICES = [
        (CAREMEL_APPLE,'Caramel Apple Crumble Pie'),
        (CARROT,'Carrot Cake'),
        (BELGIAN,'Belgian Chocolate Cake (V)'),
        (RED_VELVET,'Red Velvet Chocolate Fudge Cake'),
        (LEMON_CHEESECAKE,'Lemon Meringue Cheesecake'),
        (VANILLA_CHEESECAKE,'Madagascan Vanilla Cheesecake'),
        (WHITE_CHOC_CAKE,'White Chocolate & Raspberry Cheesecake'),
        (RAINBOW,'Rainbow Cake'),
        (TRIPLE_BROWNIE,'Triple Choc Brownie'),
        (DOUGHNUT ,'Doughnut'),
    ]

    name = models.CharField(
        max_length=256,
        unique=True,
        choices=CAKE_CHOICES,
        help_text="Enter a cake name"
    )

    def __str__(self):
        return self.name

class Icecream(models.Model):
    GELATO = 'Gelato'
    SORBET = 'Sorbet'
    types = [(GELATO, GELATO), (SORBET, SORBET)]
    name = models.CharField(max_length=200, default=GELATO)
    type = models.CharField(max_length=100, choices=types, default=GELATO)

    def __str__(self):
        return self.name

class Waffel(models.Model):
    CLASSIC = 'Signature Desserts continued & OLD SCHOOL CLASSICS'
    PREMIUM = 'Premium'
    types = [(CLASSIC,CLASSIC),(PREMIUM,PREMIUM)]
    name = models.CharField(max_length=256)
    type = models.CharField(max_length=100,choices=types)
    sauces = models.ManyToManyField(Sauce, blank=True, null=True)
    toppings = models.ManyToManyField(Topping, blank=True, null=True)
    cakes = models.ManyToManyField(Cake, blank=True, null=True)
    scoops = models.ManyToManyField(Icecream, blank=True, null=True)
    description = models.TextField(blank=True,null=True)
    
    def __str__(self):
        return self.name + ' ' + 'Waffle'
    