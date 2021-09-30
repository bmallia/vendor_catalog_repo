from django.urls import reverse
from .test_setup import TestSetUp


class TestView(TestSetUp):

    def test_product_cannot_save_with_no_data(self):
        """trying to save a product without data. It makes part of CRUD """
        res=self.client.post(self.product_url)
        self.assertEqual(res.status_code,400)

    def test_product_save_ok(self):
        """Save the product correctly. It makes part of CRUD"""
        res=self.client.post(self.product_url, self.product_data, format='json')
        
        self.assertEqual(res.data['name'], self.product_data['name'])
        self.assertEqual(res.data['code'], self.product_data['code'])
        self.assertEqual(res.data['price'], self.product_data['price'])
        self.assertEqual(res.status_code,201)

    def test_get_all_product_ok(self):
        """Get all products. It makes parte of CRUD"""
        res=self.client.get(self.product_url)
        self.assertEqual(res.status_code, 200)

    def test_get_id_product_ok(self):
        """Get product with id, it makes part of CRUD"""
        self.client.post(self.product_url, self.product_data, format='json')
        res=self.client.get(reverse('product-detail', args=[1]))
        self.assertEqual(res.status_code, 200)


    def test_get_id_product_not_found(self):
        """test get product id that doesnt exist"""
        res=self.client.get(reverse('product-detail', args=[1]))
        self.assertEqual(res.status_code, 404)

    """def test_get_cnpj_vendor_ok(self):
       
            test Get vendor with name parameters
            test the format "^vendorSearch/(?P<cnpj>\d{14})$
       
        self.client.post(self.vendor_url, self.vendor_data, format='json')
        url = reverse('vendorsearch-detail', args=[30831928000137])
        res=self.client.get(url)
        self.assertEqual(res.status_code, 200)
    """