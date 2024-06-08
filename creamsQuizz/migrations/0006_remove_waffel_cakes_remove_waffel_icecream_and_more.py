# Generated by Django 5.0.4 on 2024-06-04 22:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('creamsQuizz', '0005_waffel_icecream'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='waffel',
            name='cakes',
        ),
        migrations.RemoveField(
            model_name='waffel',
            name='icecream',
        ),
        migrations.RemoveField(
            model_name='waffel',
            name='sauces',
        ),
        migrations.RemoveField(
            model_name='waffel',
            name='toppings',
        ),
        migrations.AddField(
            model_name='waffel',
            name='cakes',
            field=models.ManyToManyField(blank=True, null=True, to='creamsQuizz.cake'),
        ),
        migrations.AddField(
            model_name='waffel',
            name='icecream',
            field=models.ManyToManyField(blank=True, null=True, to='creamsQuizz.icecream'),
        ),
        migrations.AddField(
            model_name='waffel',
            name='sauces',
            field=models.ManyToManyField(blank=True, null=True, to='creamsQuizz.sauce'),
        ),
        migrations.AddField(
            model_name='waffel',
            name='toppings',
            field=models.ManyToManyField(blank=True, null=True, to='creamsQuizz.topping'),
        ),
    ]