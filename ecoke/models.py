from django.db import models

# Create your models here.
class Brand(models.Model):

    DRINKS =(
        ('Cocacola', 'Coca-Cola'),
        ('Sprite', 'Sprite'),
        ('Fanta', 'Fanta'),
        ('Merinda', 'Merinda'),
        ('Pran Up', 'Pran Up'),
        ('Seven Up', 'Seven Up'),
        ('PW', 'Powerade'),
        ('PZ', 'Powerade Zero'),
        ('SO', 'Simply Orange'),
        ('FS', 'Fresca'),
        ('GV', 'Glaceau VitaminWater'),
        ('GS', 'Glaceau SmartWater'),
        ('DV', 'Del Valle'),
        ('MY', 'Mello Yello'),
        ('FZ', 'Fuze'),
        ('FA', 'Fuze Tea'),
        ('HT', 'Honest Tea'),
        ('OD', 'Odwalla'),
    )

    collector_name       = models.CharField(max_length=255)
    respondent_name      = models.CharField(max_length=255)
    respondent_city      = models.CharField(max_length=255)
    favourite_drink      = models.CharField(max_length=20, choices=DRINKS)
    date_of_collection   = models.DateField(auto_now_add=True)

    def __str__(self):
        return '%s-%s' % (self.respondent_name, self.favourite_drink)

    class Meta:
        ordering = ['-date_of_collection', 'favourite_drink']












