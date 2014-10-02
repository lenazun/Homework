def summary(file):
    for line in file:
        line = line.rstrip()
        words = line.split(',')
        
    	melon = words[0]
    	count = words[1]
    	amount = words[2]
        
    	str = "%s\t%ss\t$%s" % (count, melon, amount)
    	print str.upper()

    	print "\n",


def main():
	filenames = {'Day 1': 'um-deliveries-20140519.csv', 'Day 2': 'um-deliveries-20140520.csv', 'Day 3': 'um-deliveries-20140521.csv'}
	
	for key, value in filenames.iteritems():
		print "COUNT\tMELON\t\t\t\t\tAMOUNT"
		print key
		file = open(value)
		summary(file)
    	file.close()		
		
	
if __name__ == "__main__":
    main()
    
    