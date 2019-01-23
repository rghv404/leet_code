from math import sqrt


def func2(n):
    # first find the sum of the factors of the number
    # Aliquot sequence is the sum of perfect divisor of n and followed
    # by sum of the previous sum
    # e.g 12 --> 12, 16, 15, 9, 4, 3, 1, 0
    seq = list([n])
    while n > 0:
        n = get_sum(n)
        if seq[0] == n:
            print('WE\'ve got a perfect sequence')
            break
        seq.append(n)
        print(seq)
    return seq


def get_sum(n):
    sum = 0
    for i in range(1, int(sqrt(n)) + 1):
        if n % i == 0:
            # now since we're looping till sqrt(n)
            # we need to include botht the divisor and quotient as they come
            # in pairs for e.g. 10 --> 10%5 == 0 and 10/5 == 2 is also a prefect
            # divisor
            if n//i == i:
                # if both divisor and quotient are same
                # only add once
                sum += i
            else:
                # add both
                sum += i + (n//i)
        # we're subtracitng here cauise in case of division with 1
        # both 1 and n would have been added on the sum
    return sum - n


res = func2(220)
print(res)
