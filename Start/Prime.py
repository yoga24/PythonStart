import time


def is_prime(num, loop_count):
    for x in range(2, num // 2 + 1):
        loop_count += 1
        if num % x == 0:
            return False
    return True


def regular_primes(num):
    prime_list = []
    loop_count = 0
    for x in range(2, num + 1):
        loop_count += 1
        if is_prime(x, loop_count):
            prime_list.append(x)
    return loop_count, prime_list


def find_primes_upto(num):
    prime_list = [2, 3, 5, 7, 11]
    loop_count = 0
    for i in range(13, num + 1, 2):
        loop_count += 1
        mod = i % 10
        if mod not in {0, 2, 4, 5, 6, 8}:
            if is_prime(i, loop_count):
                prime_list.append(i)
    return loop_count, prime_list


def SieveOfEratosthenes(n):
    # Create a boolean array "prime[0..n]" and initialize
    #  all entries it as true. A value in prime[i] will
    # finally be false if i is Not a prime, else true.
    prime = [True for _ in range(n + 1)]
    p = 2
    loop_count = 0
    while p * p <= n:
        loop_count += 1
        # If prime[p] is not changed, then it is a prime
        if prime[p]:

            # Update all multiples of p
            # for( i = p * 2 ; i < n+1 ; i=i+p)
            for i in range(p * 2, n + 1, p):
                loop_count += 1
                prime[i] = False
        p += 1

    # Print all prime numbers
    prime_list = []
    for p in range(2, n):
        if prime[p]:
            prime_list.append(p)
    return loop_count, prime_list


def current_milli_time():
    return int(round(time.time() * 1000))


start = current_milli_time()
loop_count, prime_list = regular_primes(100000)
print("------------------------w/o mod-------------------------")
print("LoopCount:{}\n{}".format(loop_count, prime_list))
print("-------------------------------------------------------")
end = current_milli_time()

start1 = current_milli_time()
loop_count, prime_list = find_primes_upto(100000)
print("------------------------w/ mod-------------------------")
print("LoopCount:{}\n{}".format(loop_count, prime_list))
print("-------------------------------------------------------")
end1 = current_milli_time()

start2 = current_milli_time()
loop_count, prime_list = SieveOfEratosthenes(100000)
print("-----------------SieveOfEratosthenes-------------------")
print("LoopCount:{}\n{}".format(loop_count, prime_list))
print("-------------------------------------------------------")
end2 = current_milli_time()

print("elapsed time w/ mod: {}".format(end1 - start1))
print("elapsed time w/o mod: {}".format(end - start))
print("elapsed time SieveOfEratosthenes: {}".format(end2 - start2))
