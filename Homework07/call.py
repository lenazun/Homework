import datetime

"""
call.py - Telemarketing script that displays the next name 
          and phone number of a Customer to call.

          This script is used to drive promotions for 
          specific customers based on their order history.
          We only want to call customers that have placed
          an order of over 20 Watermelons.

"""

class Customer(object):

	def __init__(self, customers):

		self.customer_id = customers[customer['customer_id']]
		first = customers[customer['first']]
		self.last = customers[customer['last']]
		self.email = customers[customer['email']]
		self.telephone = customers[customer['telephone']]


	def called(self, called_mark):

		self.called = customers[customer['called']]



# Load the customers from the passed filename
# Return a dictionary containing the customer data
#    (key = customer_id)
def load_customers(filename):
	customers = {}
	f = open(filename)

	# First line of the file should be the header, 
	#   split that into a list
	header = f.readline().rstrip().split(',')

	# Process each line in a file, create a new
	#   dict for each customer
	for line in f:
		data = line.rstrip().split(',')
		customer = {}

		# Loop through each column, adding the data
		#   to the dictionary using the header keys
		for i in range(len(header)):
			customer[header[i]] = data[i]

		# Add the customer to our dictionary by customer id
		customers[customer['customer_id']] = customer

	# Close the file
	f.close()

	return customers

# Load the orders from the passed filename
# Return a list of all the orders
def load_orders(filename):
	orders = []
	f = open(filename)

	# First line of the file should be the header, 
	#   split that into a list
	header = f.readline().rstrip().split(',')

	# Process each line in a file, create a new
	#   dict for each order
	for line in f:
		data = line.rstrip().split(',')

		# Create a dictionary for the order by combining
		#   the header list and the data list
		order = dict(zip(header, data))

		# Add the order to our list of orders to return
		orders.append(order)

	# Close the file
	f.close()

	return orders

def display_customer(customer):
	print "---------------------"
	print "Next Customer to call"
	print "---------------------\n"
	print type(Customer)
	print Customer.first, Customer.last
#	print "Name: ", customer.get('first', ''), customer.get('last', '')	print "Phone: ", customer.get('telephone')
	print "\n"

def mark_as_called(customer):
	called_mark = raw_input("Have you successfully called this costumer? please enter Y or N")
	if called_mark == 'Y' or called_mark == 'y':
		customer['called'] = datetime.datetime.now().strftime("%y-%m-%d")


def write_to_file(customers):
	with open('customers2.csv', 'w') as f:
		f.write('customer_id,first,last,email,telephone,called')
		l = []
		for k, v in customers.iteritems():
			l.append( '%s, %s, %s') % customer(customer_id), customer(first), customer(last)
		f.write(', '.join(l))

def main():
	# Load data from our csv files
	customers = load_customers('customers.csv')
	orders    = load_orders('orders.csv')

	# Loop through each order
	for order in orders:
		# Is this order over 20 watermelon?
		if order.get('num_watermelons', 0) > 20:
			# Has this customer not been contacted yet?
			customer = customers.get(order.get('customer_id', 0), 0)
			if customer.get('called', '') == '':
				display_customer(customer)
				mark_as_called(customer)

				close_or_continue = raw_input("Would you like to call another costumer? please enter Y or N")
				if close_or_continue == 'N' or close_or_continue == 'n':
					write_to_file(customers)
					break
				else:
					continue

if __name__ == '__main__':
	main()