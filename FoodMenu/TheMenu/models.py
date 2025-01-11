from django.db import models

# Create your models here.
class Menu(models.Model):
    item = models.CharField(max_length=100)
    price = models.FloatField()
    description = models.TextField(max_length=255)
    item_image = models.CharField(max_length=500, default='https://cdn-icons-png.flaticon.com/512/2276/2276941.png')
    # image = models.ImageField(upload_to='menu/images')
    # offer = models.BooleanField(default=False)

    def __str__(self):
        return self.item