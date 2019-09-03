import traceback
import sys
class TelephoneOperatorCollection:
	"""
	 Class to hold data of all the operators
	"""

	def __init__(self):
		self.list_of_operators = []
		self.number_of_operators = len(self.list_of_operators)

	def setListOfOperators(self,operators):
		self.list_of_operators = operators
		self.number_of_operators = len(self.list_of_operators)

	def updateOperator(self,operator):
		self.list_of_operators.append(operator)
		self.number_of_operators = len(self.list_of_operators)

	def removeOperator(self,operator):
		self.list_of_operators.remove(operator)
		self.number_of_operators = len(self.list_of_operators)

	def getNumberOfOperators(self):
		return len(self.list_of_operators)
		
	def getEligibleOperators(self,telephone_number):
		"""
			Method to find the operators who can support dialing the telephone_number.
			Returns a list of prefixes with maximum matching digits with the telephone_number, -1 in 
			case an operator does not support the telephone_number.
		"""
	
		list_of_eligible_operators = []
		for index_of_unit,item in enumerate(self.list_of_operators):
			list_of_eligible_operators.append(item.getPrefixesWithMaximumMatch(telephone_number))
		return list_of_eligible_operators

	def getOperatorWithMinimumCost(self,list_of_eligible_operators):
		"""
			Method to find the operator with least cost.
		"""
		if self.number_of_operators == 0:
			print "No operators data available!"
			sys.exit()
		else:
			cheapest_rate = 1000
			operator = -1
			for index,item in enumerate(list_of_eligible_operators):
				if item == '-1':
					print "Operator {} does not support the telephone number."
				else:
						if cheapest_rate > self.list_of_operators[index].getPriceForPrefix(item):
							cheapest_rate = self.list_of_operators[index].getPriceForPrefix(item)
							operator = index
		return operator,cheapest_rate
			

