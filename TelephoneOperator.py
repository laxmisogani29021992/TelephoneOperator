import traceback
import sys
class TelephoneOperator:
	"""
		Class to hold the data of one operator
		Members:
			prefix_price_dic - Dictionary to hold prefix:price key value pair
			length_of_price_list - Variable to hold the number of such pairs
	"""
	def __init__(self):
		self.prefix_price_dic = {}
		self.length_of_price_list = len(self.prefix_price_dic)

	def setPrefixPrice(self,prefix,price):
		"""
			Method to set the dictionary with specified parameters
		"""
		self.prefix_price_dic[str(prefix)] = price
		self.length_of_price_list = len(self.prefix_price_dic)

	def readPrefixPrice(self):
		"""
			Method to read the prefix, price from the user
			and set them to the member variable
		"""
		try:
			key = str(int(input("\nPlease enter the prefix:")))
			value = float(input("Please enter the price for the same:"))
			if key in self.prefix_price_dic.keys():
				raise DuplicatePrefixError()
			self.setPrefixPrice(key,value)
		except DuplicatePrefixError as e:
			traceback.print_exc()
			print "Similar prefixes cannot be entered for the same operator"
		except Exception as e:
			print e
			traceback.print_exc()
			sys.exit(1)

	def getPrefixPriceDic(self):
		return self.prefix_price_dic

	def getPriceForPrefix(self,prefix):
		"""
			Method to retrive the price for specified prefix 
		"""
		return self.prefix_price_dic[prefix]

	def getPrefixesWithMaximumMatch(self, telephone_number):
		"""
			Returns the prefix with maximum match to the telephone number.
			In case the prefix does not match with the telephone_number, -1
			is returned.
		"""

		number_of_matching_prefixes_dic = {}

		# Code to generate a temproary dictionary with
		# key as the prefix and value as the number of digits matched 
		# with the telephone number.
		for item in self.prefix_price_dic:			
			length_of_prefix = len(item)
			count = 0
			tmp_count = 0
			for index in range(length_of_prefix):
				tmp_count = count
				if item[index] != telephone_number[index]:
					count = 0
					if item in number_of_matching_prefixes_dic.keys():
						number_of_matching_prefixes_dic.pop(item)
					break
				else:
					
					count = count + 1
					if tmp_count < count:
						number_of_matching_prefixes_dic.update({item:count})
		
		# Code to find the prefix with maximum match
		prefix_with_maximum_match = -1
		if number_of_matching_prefixes_dic == {}:
			prefix_with_maximum_match = '-1'
		else:
			prefix_with_maximum_match = max(number_of_matching_prefixes_dic, key=number_of_matching_prefixes_dic.get)
		return prefix_with_maximum_match
