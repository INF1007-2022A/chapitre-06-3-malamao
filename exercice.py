#!/usr/bin/env python
# -*- coding: utf-8 -*-


import math
import copy
import itertools


def get_maximums(numbers):
	maximums = []
	for liste in numbers:
		max = 0
		for element in liste:
			if element > max:
				max = element
		maximums.append(max)

	return maximums

def join_integers(numbers):
	return int("".join([str(element) for element in numbers]))

def generate_prime_numbers(limit):
	premiers = []
	nombre = list(range(2,(limit+1)))
	while len(nombre) != 0:
		premiers.append(nombre[0])
		premier = nombre[0]
		entiers_multiples = []
		for k in range(len(nombre)):
			if nombre[k] % premier == 0:
				entiers_multiples.append(nombre[k])
		for element in entiers_multiples:
			nombre.remove(element)
	return premiers

def combine_strings_and_numbers(strings, num_combinations, excluded_multiples):
	combinaison = []
	if excluded_multiples != None:
		for i in range(1, num_combinations+1):
			if i % excluded_multiples != 0:
				combinaison.append(i)
	else:
		combinaison = list(range(1, num_combinations+1))
	resultat = []
	for num in combinaison:
		for n in range(len(strings)):
			resultat.append(strings[n]+str(num))
	return resultat

if __name__ == "__main__":
	print(get_maximums([[1,2,3], [6,5,4], [10,11,12], [8,9,7]]))
	print("")
	print(join_integers([111, 222, 333]))
	print(join_integers([69, 420]))
	print("")
	print(generate_prime_numbers(17))
	print("")
	print(combine_strings_and_numbers(["A", "B"], 2, None))
	print(combine_strings_and_numbers(["A", "B"], 5, 2))
