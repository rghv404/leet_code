import numpy as np

# thi s


def get_max_product_contig_sub_array(lst):
    max_prod_at_i = [lst[-1]]
    max_prod = lst[-1]

    for a in lst[-2::-1]:
        max_prod_at_i.append(max(a * max_prod_at_i[-1], a))
        max_prod = max(max_prod, max_prod_at_i[-1])
    return max_prod


max_prod = get_max_product_contig_sub_array([-2, -3, -2, -4])
print(max_prod)


# my_array = np.ones(3, dtype=([('foo', int), ('bar', float)]))
my_array = np.ones(3)
print(my_array)
# Print the structured array
print(my_array['foo'])

# A record array
my_array2 = my_array.view(np.recarray)
# Print the record array
print(my_array2.foo)
