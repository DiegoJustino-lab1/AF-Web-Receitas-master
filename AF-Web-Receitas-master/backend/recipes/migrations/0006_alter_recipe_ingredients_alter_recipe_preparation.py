# Generated by Django 5.0.6 on 2024-06-19 00:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0005_alter_recipe_ingredients_alter_recipe_preparation'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipe',
            name='ingredients',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='recipe',
            name='preparation',
            field=models.TextField(),
        ),
    ]
