from django.test import TestCase
from .models import Image,Location,Category

# Create your tests here.
class LocationTestClass(TestCase):
    # Set Up method
    def setUp(self):
        self.germany = Location(name = 'Germany')

    # Testing instance
    def test_instance(self):
        self.assertTrue(isinstance(self.germany,Location))

    # Testing save method
    def test_save_method(self):
        self.germany.save_location()
        locations = Location.objects.all()
        self.assertTrue(len(locations) > 0)

    def test_del_method(self):
        self.germany.save_location()
        test_location = Location(name = 'Paris')
        test_location.save_location()
        locations = Location.objects.all()
        self.assertTrue(len(locations) > 0)    

class CategoryTestClass(TestCase):
    # Set Up Method
    def setUp(self):
        self.saloon = Category(name = 'Saloon')

    # Testing instance
    def test_instance(self):
        self.assertTrue(isinstance(self.saloon,Category))

    # Testing save method
    def test_saving_method(self):
        self.saloon.save_category()
        categories = Category.objects.all()        
        self.assertTrue(len(categories) > 0)

    def test_delete_method(self):
        self.saloon.save_category()  
        test_category = Category(name = 'SUV')
        test_category.save_category()
        categories = Category.objects.all()
        self.saloon.del_category()
        self.assertTrue(len(categories) > 0)  

class ImageTestCase(TestCase):
    # Set Up Method
    def setUp(self):
        self.image = Image(actual_image = 'image.jpg', name = 'Fortuner', description = 'elegant')
    
    # Testing instance
    def test_instance(self):
        self.assertTrue(isinstance(self.image,Image))

     
        
