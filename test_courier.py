import unittest
from orders import Order
from datetime import datetime, timedelta

from mt_list import MTList

from cook import Cook
from courier import Courier

class Testing(unittest.TestCase):
    def setUp(self):
        self.o = Order({u'id' : u'a8cfcb76-7f24-4420-a5ba-d46dd77bdffd' , u'prepTime' : 4 , u'name' : u'Banana Split'})
        cooking = MTList()
        cooking.put(self.o)
        self.c = Cook(MTList() , cooking)
        self.courier=Courier(self.o)


    def test_arrival_time(self):
        self.assertEqual(self.courier.get_order_details(self.o)[0],self.o.order_wait_time)

if __name__ == '__main__':
    unittest.main()