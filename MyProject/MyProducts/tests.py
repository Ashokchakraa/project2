from django.test import TestCase

# Create your tests here.
from MyProducts.models import Product

class MyTest(TestCase):
	def test_insert_record(self):
		try:
			obj = Product(name="Test3",
				description="Test3",
				costPerItem=28,
				stockQuantity=56)
			obj.save()
			self.assertEquals(obj.stockQuantity, 56, "Quantity Mismatch")
			self.assertEquals(obj.costPerItem, 28, "Product cost Mismatch")
			self.assertEquals(obj.volume, 1568.00, "Volume Mismatch")
		except Exception as e:
			print("Unable to insert the record")

	def test_insert_record_with_invalid_quantity(self):
		try:
			obj = Product(name="Test3",
				description="Test3",
				costPerItem=28,
				stockQuantity='56')
			obj.save()
			print(obj.volume)
			self.assertEquals(obj.costPerItem, '', "Product cost Mismatch")
		except Exception as e:
			self.assertEquals(str(e), "[<class 'decimal.InvalidOperation'>]")
