
import traceback
import sys
import TelephoneOperator
import TelephoneOperatorCollection

try:
	# Taking input for the number of operators
	number_of_operating_units = int(input("Please enter the number of operating units:"))
	operators = TelephoneOperatorCollection.TelephoneOperatorCollection()

	# Taking input for the prefix and price for each operator
	for index_of_unit in range(number_of_operating_units):
		prefix_price_list = TelephoneOperator.TelephoneOperator()
		print "\nPlease enter price list for {} operator:".format(index_of_unit + 1)
		number_of_prefixes = int(input("Please enter the number of prefixes for unit {}:".format(index_of_unit + 1)))
		for index_of_prefixes in range(number_of_prefixes):
			prefix_price_list.readPrefixPrice()
		operators.updateOperator(prefix_price_list)

	#Taking the telephone number input
 	telephone_number = raw_input("Please enter the telephone number:")

 	# Finding the list of operators that can support the above telephone number
 	# If an operator does not support, the list has -1 at its index
 	# Ex operator 0 does not support but operator 1 supports with prefix 722,
 	# then the list_of_operators_eligible_with_prefix = ['-1','722']
	list_of_operators_eligible_with_prefix = operators.getEligibleOperators(telephone_number)

	# Finding the operator that can provide the cheapest cost to dial the specified telephone_number
	operator_index, cheapest_rate = operators.getOperatorWithMinimumCost(list_of_operators_eligible_with_prefix)

	if operator_index == -1 and cheapest_rate == 1000:
		print "No operator available to dial the specified telephone number."
	else:
		print "Operator {} is available to dial the number at the rate of ${}/min.".format(operator_index + 1,cheapest_rate)
except Exception as e:
	print e
	traceback.print_exc()
	sys.exit(1)