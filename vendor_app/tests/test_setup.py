from rest_framework.test import APITestCase
from django.urls import reverse

class TestSetUp(APITestCase):
    """ load initial config for test """
    def setUp(self):
        self.vendor_url=reverse('vendor-list')
        self.product_url=reverse('product-list')
        
        ##self.product_search_url= reverse('productSearch')

        self.vendor_data={
            "products": [
            {   
                "id": 3,
                "name": "Produto 3",
                "code": 5,
                "price": "17.58"
            }
        ],
        "name": "Jhony3",
        "cnpj": "30831928000137",
        "city": "Rio",
        "id":1,

        }

        self.product_data={
                "id": 1,
                "name": "Produto 1",
                "code": 10,
                "price": "25.45"
        }

        return super().setUp()
    
    def tearDown(self):
        return super().tearDown()