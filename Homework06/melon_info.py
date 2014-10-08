"""
melon_info.py - Prints out all the melons in our inventory

"""

from collections import defaultdict
from melons import melon_name, melon_seedless, melon_price, melon_fleshcolor, melon_rindcolor, melon_weight

def make_a_dict(name, seedless, price, flesh, rind, weight):

	all_melons = defaultdict(list)

	for d in (name, seedless, price, flesh, rind, weight):
		for key, value in d.iteritems():
			all_melons[key].append(value)

	return all_melons


def print_melon(all_melons):

	print "TYPE          SEEDS          PRICE    FLESH COLOR    RIND COLOR     AVG WEIGHT"

	for a, b in all_melons.iteritems():
		name, seeds, price, flesh, rind, weight = b
		
		price = float(price)
		weight = float(weight)

		if seeds == True:
			seeds = 'Seedless'
		else:
			seeds = 'Has seeds'
		
		print "%10s     %10s     %.2f     %10s     %10s     %.2f   " % (name, seeds, price, flesh, rind, weight) 


def main():
	melon_inventory = make_a_dict(melon_name, melon_seedless, melon_price, melon_fleshcolor, melon_rindcolor, melon_weight)
	print_melon(melon_inventory)


if __name__ == '__main__':
	main()