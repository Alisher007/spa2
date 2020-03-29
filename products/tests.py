from django.test import TestCase

# Create your tests here.
    # def get_total_item_price(self):
    #     return self.quantity * self.productid.price
    
    # def get_total_discount_item_price(self):
    #     return self.quantity * self.productid.price * ((100 - self.productid.categoryid.discount) / 100)
    
    # def get_amount_saved(self):
    #     return self.get_total_item_price() - self.get_total_discount_item_price()
    
    # def get_final_price(self):
    #     if self.productid.categoryid.discount:
    #         return self.get_total_discount_item_price()
    #     return self.get_total_item_price()