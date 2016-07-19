#!/usr/bin/python

import time

#####VARIABLES#####
"""
list of pokemon you which to evolve
format:
pokemon, # of pokemon, # of candies, candy needed to evolve
"""
pokemon_list =[
["Pidgey", 23, 99, 12],
["Rattata", 25, 87, 25]
]
#####FUNCTIONS#####
def pidgey_calc(pokemon_name, pokemon_amount,
				pokemon_candy, candy_needed):
					amount_of_evolutions = 0
					pokemon_transfered = 0
					a = pokemon_name
					b = pokemon_amount
					c = pokemon_candy
					d = candy_needed
					# as long as their are pokemon left
					while b > 0:
						# transfer 1 pokemon
						if c < d:
							b -= 1
							c += 1
							pokemon_transfered += 1
						# else, evolve 1 pokemon
						else:
							c -= d
							amount_of_evolutions += 1
							b -= 1
							#gain 1 candy from evolving
							c += 1
					return (amount_of_evolutions, pokemon_transfered)
						

#####MAIN FUNCTION#####					
def main():
	total_XP = 0
	approx_time = 0
	for i in pokemon_list:
		answer = (pidgey_calc(i[0], i[1], i[2], i[3]))
		total_XP += answer[0] * 500
		approx_time += (answer[0] * 30)
		print (
		"You need to transfer " + str(answer[1]) + " " +
		i[0] + ". Then you can evolve " +
		str(answer[0]) + " for a total of" +
		str(answer[0] *500) + " XP. \n"
		)
	print(
	"This grands a total of " + str(total_XP) + " XP" +
	" and takes roughly " + str(approx_time) + " seconds"
	)

if __name__ == "__main__":
	main()
