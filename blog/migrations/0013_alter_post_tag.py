# Generated by Django 5.0.4 on 2024-06-04 22:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0012_alter_post_tag'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='tag',
            field=models.CharField(blank=True, default='Culture', max_length=50, null=True),
        ),
    ]