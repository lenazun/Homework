

def payment_diferential(customer_orders):

    melon_cost = 1.00

    for line in customer_orders:
        data = line.split(",")
        customer_name = data[1]
        customer_melons = int(data[2])
        customer_paid = float(data[3])

        customer_expected = customer_melons * melon_cost

        if customer_expected != customer_paid:
            print customer_name, "paid %.2f, expected %.2f" % (customer_paid, customer_expected) 



def main():
    
    customer_orders = open("customer_orders.csv")

    payment_diferential(customer_orders)

    customer_orders.close()




if __name__ == "__main__":
    main()
