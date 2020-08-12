from django.db import models


# Create your models here.
class Location(models.Model):
    name = models.CharField(max_length = 30)

    def __str__(self):
        return self.name 

    def save_location(self):
        self.save()  

    def del_location(self):
        self.delete() 

    @classmethod
    def get_location(cls):
        locations = Location.objects.all()
        return locations

    
class Category(models.Model):
    name = models.CharField(max_length = 30)

    def __str__(self):
        return self.name

    def save_category(self):
        self.save()   

    def del_category(self):
        self.delete()     

    @classmethod
    def get_category(cls):
        categories = Category.objects.all()
        return categories


      

class Image(models.Model):
    actual_image = models.ImageField(upload_to = 'media/')
    name = models.CharField(max_length = 30)
    description = models.CharField(max_length = 60)
    location = models.ForeignKey(Location,on_delete = models.CASCADE)
    category = models.ForeignKey(Category,on_delete = models.CASCADE)

    def __str__(self):
        return self.name

    def save_image(self):
        self.save()

    def del_image(self):
        self.delete()

               
    
    @classmethod
    def search_by_name(cls,search_term):
        images = cls.objects.filter(name__icontains = search_term)
        return images

    @classmethod
    def search_by_location(cls,location):
        image_location = cls.objects.filter(location__name = location)
        return image_location
