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
        res=self.client.post(self.product_url, self.product_data, format='json')
        """Get product with id, it makes part of CRUD"""
        res=self.client.get(f"{self.product_url}/1")
        self.assertEqual(res.status_code, 200)