import random

coin_sides = ['H', 'T']
flip_res = list(random.choice(coin_sides) for i in range(100))
print("Heads : {} \nTails : {}".format(flip_res.count('H'), flip_res.count('T')))
