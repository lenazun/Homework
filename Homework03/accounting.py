def accounting_report():
    f = open("orders_by_type.csv")
    melon_tallies = {"Musk": 0, "Hybrid": 0, "Watermelon": 0, "Winter": 0}
    for line in f:
        data = line.split(",")
        melon_type = data[1]
        melon_count = int(data[2])
        melon_tallies[melon_type] += melon_count
    f.close()
    return melon_tallies

def revenue_report():
    melon_prices = { "Musk": 1.15, "Hybrid": 1.30, "Watermelon": 1.75, "Winter": 4.00 }
    total_revenue = 0
    
    for melon_type in tallies:
        price = melon_prices[melon_type]
        revenue = price * tallies[melon_type]
        total_revenue += revenue
        print "We sold %d %s melons at %0.2f each for a total of %0.2f" % (tallies[melon_type], melon_type, price, revenue)

def sales_report():
    f = open("orders_with_sales.csv")
    sales = [0, 0]
    for line in f:
        data = line.split(",")
        if data[1] == "0":
            sales[0] += float(data[3])
        else:
            sales[1] += float(data[3])
    print "Salespeople generated %0.2f in revenue." % sales[1]
    print "Internet sales generated %0.2f in revenue." % sales[0]
    if sales[1] > sales[0]:
        print "Guess there's some value to those salespeople after all."
    else:
        print "Time to fire the sales team! Online sales rule all!"


def main():

    global tallies

    tallies = accounting_report()

    print "******************************************"

    revenue_report()

    print "******************************************"

    sales_report()

    print "******************************************"


if __name__ == "__main__":
    main()
