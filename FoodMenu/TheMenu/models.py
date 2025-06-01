from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.
class Menu(models.Model):
    user_name = models.ForeignKey(User, on_delete=models.CASCADE, default=1) #associating each item posted to the user
    item = models.CharField(max_length=100)
    price = models.FloatField()
    description = models.TextField(max_length=255)
    item_image = models.CharField(max_length=500, default='https://cdn-icons-png.flaticon.com/512/2276/2276941.png', blank=True)
    # image = models.ImageField(upload_to='menu/images')
    # offer = models.BooleanField(default=False)

    def __str__(self):
        return self.item
    
    def get_absolute_url(self):
        return reverse("menu:detail_item", kwargs={"pk": self.pk})