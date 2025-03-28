from django.contrib import admin
from .models import Deck
class DeckAdmin(admin.ModelAdmin):
        list_display = [ "id", "name", "year"]
# Register your models here.
admin.site.register(Deck, DeckAdmin)