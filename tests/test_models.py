from django.contrib.auth.models import User
from django.test import TestCase

from store.models import Category, Product


class TestCatetogriesModel(TestCase):
    def setUp(self):
        self.data1 = Category.objects.create(name='salamander', address='salamander')

    def test_category_model_entry(self):
        # test Category model data 
        data = self.data1
        self.assertTrue(isinstance(data, Category))

    def test_category_model_entry(self):
        # test Category default name 
        data = self.data1
        self.assertEqual(str(data), 'salamander')


class TestCatetogriesModel(TestCase):
    def setUp(self):
        Category.objects.create(name='salamander', address='salamander')
        User.objects.create(username='admin')
        self.data1 = Product.objects.create(category_id=1, title='salamander', category_by_id=1, address='salamander', price='10', image='salamander')
 
    def test_category_model_entry(self):
        # test Category model data 
        data = self.data1
        self.assertTrue(isinstance(data, Product))
        self.assertEqual(str(data), 'salamander')

