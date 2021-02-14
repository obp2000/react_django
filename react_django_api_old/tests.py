# from rest_framework.test import APITestCase
# # from unittest.mock import patch
# from django.conf import settings
# from collections import ChainMap
# from django.test import override_settings
# from rest_framework.routers import DefaultRouter
# from rest_framework import status
# from django.urls import reverse
# from PIL import Image
# import tempfile

# from react_django_api.models import Product
# from react_django_api.views import ProductViewSet


# class ProductAPITestCase(APITestCase):
#     """
#     Test products API
#     """

#     # @classmethod
#     # def setUpClass(cls):
#     #     """
#     #     Create 2 test products
#     #     """
#     #     super().setUpClass()
#     #     cls.product1 = Product.objects.create(name='Product1', price=300)
#     #     cls.product2 = Product.objects.create(name='Product2', price=340)

#     def setUp(self):
#         """
#         Create 3 test products
#         """
#         self.product1 = Product.objects.create(name='Product1', price=300)
#         self.product2 = Product.objects.create(name='Product2', price=340)
#         self.product3 = Product.objects.create(name='Product3', price=350)

#     @override_settings(REST_FRAMEWORK=ChainMap({'PAGE_SIZE': 2}, settings.REST_FRAMEWORK))
#     def test_list_products(self):
#         """
#         Test that we can get a list of products
#         """
#         url = reverse('product-list')
#         response = self.client.get(url)
#         self.assertEqual(response.status_code, status.HTTP_200_OK)
#         data = response.data
#         self.assertEqual(data['totalCount'], Product.objects.count())
#         self.assertEqual(data['totalPages'], 2)
#         results = data['results']
#         self.assertEqual(len(results), 2)
#         first_result = results[0]
#         self.assertEqual(first_result['id'], self.product1.id)
#         self.assertEqual(first_result['name'], self.product1.name)
#         self.assertEqual(first_result['price'], self.product1.price)
#         second_result = results[1]
#         self.assertEqual(second_result['id'], self.product2.id)
#         self.assertEqual(second_result['name'], self.product2.name)
#         self.assertEqual(second_result['price'], self.product2.price)

#     def test_product_list_route(self):
#         """
#         Test that we've got routing set up for Products
#         """
#         view = ProductViewSet()
#         view.basename = DefaultRouter().get_default_basename(ProductViewSet)
#         view.request = None
#         self.assertEqual(view.reverse_action('list'), '/api/products/')

#     def test_product_create_route(self):
#         """
#         Test that we've got routing set up for create Product
#         """
#         # self.assertEqual(self.view.reverse_action('create'), '/api/products/')

#     def test_retrieve_product(self):
#         """
#         Test that we can retrieve a product
#         """
#         url = reverse('product-detail', args=[self.product2.id])
#         response = self.client.get(url)
#         self.assertEqual(response.status_code, status.HTTP_200_OK)
#         data = response.data
#         self.assertEqual(data['id'], self.product2.id)
#         self.assertEqual(data['name'], self.product2.name)
#         self.assertEqual(data['price'], self.product2.price)

#     def test_create_product(self):
#         """
#         Test that we can create a product
#         """
#         url = reverse('product-list')
#         image = Image.new('RGB', (100, 100))
#         tmp_file = tempfile.NamedTemporaryFile(suffix='.jpg')
#         image.save(tmp_file)
#         tmp_file.seek(0)
#         data = {
#             'name': 'Product3',
#             'price': 350,
#             'image': tmp_file,
#         }
#         products_count_before = Product.objects.count()
#         response = self.client.post(url, data)
#         self.assertEqual(response.status_code, status.HTTP_201_CREATED)
#         self.assertEqual(Product.objects.count(), products_count_before + 1)
#         self.assertEqual(response.data['id'], self.product3.id + 1)
#         self.assertEqual(response.data['name'], data['name'])
#         self.assertEqual(response.data['price'], data['price'])
#         self.assertIn('.jpg', response.data['image'])

#         new_product = Product.objects.latest('id')
#         self.assertEqual(new_product.id, self.product3.id + 1)
#         self.assertEqual(new_product.name, data['name'])
#         self.assertEqual(new_product.price, data['price'])
#         self.assertIn('.jpg', new_product.image.name)

#     def test_update_product(self):
#         """
#         Test that we can update a product
#         """
#         url = reverse('product-detail', args=[self.product2.id])
#         image = Image.new('RGB', (100, 100))
#         tmp_file = tempfile.NamedTemporaryFile(suffix='.jpg')
#         image.save(tmp_file)
#         tmp_file.seek(0)
#         data = {
#             'name': 'Product4',
#             'price': 380,
#             'image': tmp_file,
#         }
#         response = self.client.put(url, data, format='multipart')
#         self.assertEqual(response.status_code, status.HTTP_200_OK)
#         self.assertEqual(response.data['id'], self.product2.id)
#         self.assertEqual(response.data['name'], data['name'])
#         self.assertEqual(response.data['price'], data['price'])
#         self.assertIn('.jpg', response.data['image'])

#         updated_product = Product.objects.get(pk=self.product2.id)
#         self.assertEqual(updated_product.name, data['name'])
#         self.assertEqual(updated_product.price, data['price'])
#         self.assertIn('.jpg', updated_product.image.name)

#     def test_destroy_product(self):
#         """
#         Test that we can destroy a product
#         """
#         url = reverse('product-detail', args=[Product.objects.latest('id').id])
#         products_count_before = Product.objects.count()
#         response = self.client.delete(url)
#         self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
#         self.assertEqual(Product.objects.count(), products_count_before - 1)

#     def test_search_products(self):
#         """
#         Test that we can search products' names by term
#         """
#         url = reverse('product-list') + "?term=" + self.product2.name
#         response = self.client.get(url)
#         self.assertEqual(response.status_code, status.HTTP_200_OK)
#         results = response.data['results']
#         self.assertEqual(len(results), 1)
#         self.assertEqual(results[0]['id'], self.product2.id)
#         self.assertEqual(results[0]['name'], self.product2.name)
#         self.assertEqual(results[0]['price'], self.product2.price)

#     @override_settings(REST_FRAMEWORK=ChainMap({'PAGE_SIZE': 2}, settings.REST_FRAMEWORK))
#     def test_paginated_list_products(self):
#         """
#         Test that we can get a certian page of products
#         """
#         # mock_page_size.return_value = 2
#         url = reverse('product-list') + '?page=1'
#         response = self.client.get(url)
#         self.assertEqual(response.status_code, status.HTTP_200_OK)
#         data = response.data
#         self.assertEqual(data['totalCount'], Product.objects.count())
#         self.assertEqual(data['totalPages'], 2)
#         results = data['results']
#         self.assertEqual(len(results), 2)
#         first_result = results[0]
#         self.assertEqual(first_result['id'], self.product1.id)
#         self.assertEqual(first_result['name'], self.product1.name)
#         self.assertEqual(first_result['price'], self.product1.price)
#         second_result = results[1]
#         self.assertEqual(second_result['id'], self.product2.id)
#         self.assertEqual(second_result['name'], self.product2.name)
#         self.assertEqual(second_result['price'], self.product2.price)
