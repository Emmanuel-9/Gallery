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
        locations = Location.object.all()
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
        categories = Category.object.all()        
        self.assertTrue(len(categories) > 0)