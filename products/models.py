from django.db import models

# Create your models here.
class Menu(models.Model):
    name = models.CharField(max_length=45)

    class Meta:
        db_table = "menus"


class Category(models.Model):
    name = models.CharField(max_length=45)
    menu = models.ForeignKey("Menu", on_delete=models.CASCADE)

    class Meta:
        db_table = "categories"

class Drink(models.Model):
    korean_name = models.CharField(max_length=45)
    english_name = models.CharField(max_length=45)
    description = models.TextField(default ="")
    category = models.ForeignKey("Category", on_delete=models.CASCADE)

    class Meta:
        db_table = "drinks"

class Image(models.Model):
    image_url = models.CharField(max_length=2000)
    drink = models.ForeignKey("Drink", on_delete=models.CASCADE)

    class Meta:
        db_table = "images"

class Allergy(models.Model):
    name = models.CharField(max_length=45)

    class Meta:
        db_table = "allergies"

class Allergydrink(models.Model):
    allergy = models.ForeignKey("Allergy", on_delete=models.CASCADE)
    drink = models.ForeignKey("Drink", on_delete=models.CASCADE)

    class Meta:
        db_table = "allergy_drinks"


class Size(models.Model):
    name = models.CharField(max_length=45)
    size_ml = models.CharField(max_length=45)
    size_fluid_ounce = models.CharField(max_length=45)

    class Meta:
        db_table = "sizes"
    


class Nutrition(models.Model):
    one_serving_kca = models.DecimalField(max_digits=10, decimal_places=2)
    sodium_mg = models.DecimalField(max_digits=10, decimal_places=2)
    saturated_fat_g = models.DecimalField(max_digits=10, decimal_places=2)
    sugars = models.DecimalField(max_digits=10, decimal_places=2)
    protein_g = models.DecimalField(max_digits=10, decimal_places=2)
    caffeine_mg = models.DecimalField(max_digits=10, decimal_places=2)
    drink = models.ForeignKey("Drink", on_delete=models.CASCADE)
    size = models.ForeignKey("Size", on_delete=models.CASCADE)
     
    class Meta:
        db_table = "nutritions"



