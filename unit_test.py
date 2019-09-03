import unittest
import TelephoneOperator 
import TelephoneOperatorCollection
class TestTelephoneOperator(unittest.TestCase):
	def test_setPrefixPrice(self):
		prefix = '1234'
		price = 2.0
		telephone_operator = TelephoneOperator.TelephoneOperator()
		input_dic = {prefix:price}
		telephone_operator.setPrefixPrice(prefix, price)
		self.assertDictEqual(telephone_operator.prefix_price_dic,input_dic)

	def test_getPrefixPriceDic(self):
		prefix = 1234
		price = 1.2
		telephone_operator = TelephoneOperator.TelephoneOperator()
		input_dic = {prefix:price}
		telephone_operator.setPrefixPrice(prefix, price)
		output_dic = {'1234':1.2}
		self.assertDictEqual(telephone_operator.getPrefixPriceDic(),output_dic)

	def test_getPriceForPrefix(self):
		prefix = 1234
		price = 1.2
		telephone_operator = TelephoneOperator.TelephoneOperator()
		input_dic = {prefix:price}
		telephone_operator.setPrefixPrice(prefix, price)
		output_prefix = '1234'
		self.assertEqual(telephone_operator.getPriceForPrefix(output_prefix),price)

	def test_getPrefixesWithMaximumMatch_positive(self):
		telephone_number = '72234567'
		telephone_operator = TelephoneOperator.TelephoneOperator()
		telephone_operator.setPrefixPrice(722,0.5)
		telephone_operator.setPrefixPrice(7223,1.0)
		telephone_operator.setPrefixPrice(7221,2.0)
		output_prefix = '7223'
		self.assertEqual(telephone_operator.getPrefixesWithMaximumMatch(telephone_number),output_prefix)

	def test_getPrefixesWithMaximumMatch_negative(self):
		telephone_number = '12234567'
		telephone_operator = TelephoneOperator.TelephoneOperator()
		telephone_operator.setPrefixPrice(722,0.5)
		telephone_operator.setPrefixPrice(7223,1.0)
		telephone_operator.setPrefixPrice(7221,2.0)
		output_prefix = '-1'
		self.assertEqual(telephone_operator.getPrefixesWithMaximumMatch(telephone_number),output_prefix)

class TestTelephoneOperatorCollection(unittest.TestCase):
	def setUp(self):
		self.telephone_operator_one = TelephoneOperator.TelephoneOperator()
		self.telephone_operator_one.setPrefixPrice(722,0.5)
		self.telephone_operator_one.setPrefixPrice(7223,1.0)
		self.telephone_operator_one.setPrefixPrice(7221,2.0)
		self.telephone_operator_two = TelephoneOperator.TelephoneOperator()
		self.telephone_operator_two.setPrefixPrice(922,0.5)
		self.telephone_operator_two.setPrefixPrice(233,1.0)
		self.telephone_operator_two.setPrefixPrice(7221,2.0)		


	def test_setListOfOperators(self):
		telephone_operator_collection = TelephoneOperatorCollection.TelephoneOperatorCollection()
		telephone_operator_collection.setListOfOperators([self.telephone_operator_one,self.telephone_operator_two])
		self.assertListEqual(telephone_operator_collection.list_of_operators, [self.telephone_operator_one,self.telephone_operator_two])

	def test_updateOperator(self):
		telephone_operator_collection = TelephoneOperatorCollection.TelephoneOperatorCollection()
		telephone_operator_collection.setListOfOperators([self.telephone_operator_one,self.telephone_operator_two])
		telephone_operator_three = TelephoneOperator.TelephoneOperator()
		telephone_operator_three.setPrefixPrice(6789,0.5)
		telephone_operator_three.setPrefixPrice(1223,1.0)
		telephone_operator_three.setPrefixPrice(9876,2.0)
		telephone_operator_collection.updateOperator(telephone_operator_three)
		self.assertListEqual(telephone_operator_collection.list_of_operators, [self.telephone_operator_one,self.telephone_operator_two,
																				telephone_operator_three])

	def test_getEligibleOperators_positive(self):
		telephone_operator_collection = TelephoneOperatorCollection.TelephoneOperatorCollection()
		telephone_operator_collection.setListOfOperators([self.telephone_operator_one,self.telephone_operator_two])
		telephone_number = '72234567'
		output_list = ['7223','-1']
		self.assertListEqual(telephone_operator_collection.getEligibleOperators(telephone_number),output_list)

	def test_getEligibleOperators_negative(self):
		telephone_operator_collection = TelephoneOperatorCollection.TelephoneOperatorCollection()
		telephone_operator_collection.setListOfOperators([self.telephone_operator_one,self.telephone_operator_two])
		telephone_number = '82234567'
		output_list = ['-1','-1']
		self.assertListEqual(telephone_operator_collection.getEligibleOperators(telephone_number),output_list)
		
	def test_getOperatorWithMinimumCost_positive(self):
		telephone_operator_collection = TelephoneOperatorCollection.TelephoneOperatorCollection()
		telephone_operator_collection.setListOfOperators([self.telephone_operator_one,self.telephone_operator_two])
		telephone_number = '72234567'
		operator,cheapest_rate = telephone_operator_collection.getOperatorWithMinimumCost(['7223'])
		self.assertEqual(operator,0)
		self.assertEqual(cheapest_rate,1.0)

	def test_getOperatorWithMinimumCost_negative(self):
		telephone_operator_collection = TelephoneOperatorCollection.TelephoneOperatorCollection()
		telephone_operator_collection.setListOfOperators([self.telephone_operator_one,self.telephone_operator_two])
		telephone_number = '52234567'
		operator,cheapest_rate = telephone_operator_collection.getOperatorWithMinimumCost([])
		self.assertEqual(operator,-1)
		self.assertEqual(cheapest_rate,1000)
if __name__ == '__main__':
    unittest.main()