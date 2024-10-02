from django.db import models

# Create your models here.
def Upload(instance,file_name):
    extention=file_name.split('.')[1]
    return f'Drink/{instance.drink_name}.{extention}'

class Menu(models.Model):
    drink_name=models.CharField(max_length=100)
    image=models.ImageField(upload_to=Upload,width_field=None,height_field=None)
    price_s=models.IntegerField(default=0)
    price_l=models.IntegerField(default=0)

    class Meta:
        verbose_name=("Menu")
        verbose_name_plural=("Menus")
    
    def __str__(self):
        return self.drink_name
#===============================iced==================================
    
def Upload_iced(instance,file_name):
    extention=file_name.split('.')[1]
    return f'Drink/{instance.drink_name}.{extention}'

class Menu_iced(models.Model):
    drink_name=models.CharField(max_length=100)
    image=models.ImageField(upload_to=Upload,width_field=None,height_field=None)
    price_s=models.IntegerField(default=0)
    price_l=models.IntegerField(default=0)

    class Meta:
        verbose_name=("Menu_iced")
        verbose_name_plural=("Menus_iced")
    
    def __str__(self):
        return self.drink_name
