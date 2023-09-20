from django.db import models

# Create your models here.
# Model are actually used to create the database schema, here recipe is the table and recipe_name, recipe_description and recipe_image are the columns
class Recipe(models.Model):
    recipe_name = models.CharField(max_length=20)
    recipe_description = models.TextField()
    recipe_image = models.FileField()


