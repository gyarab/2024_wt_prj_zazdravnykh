from django.db import models
Class Deck(models.Deck):
    name = models.CharField(max_length=300)
    year = models.IntegerField(blank=True, null=False)
    
    def __str__(self):
        return f"Deck <(self):
            
