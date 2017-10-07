a_list = ['y1', 'y2', 'k1', 'ck1', 'ck5']

new_list = list(it.upper() for it in a_list if '1' in it)
print(new_list)
