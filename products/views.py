
import json

from django.http import JsonResponse
from django.views import View

from . models import *

class DrinksView(View):
    def post(self, request):
        data           = json.loads(request.body)
        drink_category = Category.objects.get(name=data["drink_category"])
        
        Drink.objects.create(
            korean_name  = data["drink_kr"], 
            english_name = data["drink_en"], 
            description  = data["description"], 
            category     = drink_category
        )

        return JsonResponse({"message": "created"}, status = 201)
        
    def get(self, request):
        drinks = Drink.objects.all()
        result = []

        for drink in drinks:
            result.append(
                {
                    "menu" : drink.category.menu.name,
                    "category" : drink.category.name,
                    "drink_name" : drink.korean_name

                }
            )

        return JsonResponse({"results": result}, status=200)

    
