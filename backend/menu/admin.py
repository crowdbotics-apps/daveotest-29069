from django.contrib import admin
from .models import Review, Item, Category, Country, ItemVariant

admin.site.register(Review)
admin.site.register(Item)
admin.site.register(ItemVariant)
admin.site.register(Category)
admin.site.register(Country)

# Register your models here.
