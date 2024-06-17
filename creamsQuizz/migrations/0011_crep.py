# Generated by Django 5.0.4 on 2024-06-17 15:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('creamsQuizz', '0010_alter_topping_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='Crep',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256)),
                ('type', models.CharField(choices=[('Signature Desserts continued & OLD SCHOOL CLASSICS', 'Signature Desserts continued & OLD SCHOOL CLASSICS'), ('Premium', 'Premium')], max_length=100)),
                ('description', models.TextField(blank=True, null=True)),
                ('cakes', models.ManyToManyField(blank=True, null=True, to='creamsQuizz.cake')),
                ('sauces', models.ManyToManyField(blank=True, null=True, to='creamsQuizz.sauce')),
                ('scoops', models.ManyToManyField(blank=True, null=True, to='creamsQuizz.icecream')),
                ('toppings', models.ManyToManyField(blank=True, null=True, to='creamsQuizz.topping')),
            ],
        ),
    ]