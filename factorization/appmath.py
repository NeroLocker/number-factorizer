from math import sqrt


class AppMath:
    '''Represents mathematics class for application'''

    @staticmethod
    def decomposeNumber(value):
        '''Decompose input number into prime factors
        Return 1 if number is a prime factor'''

        # List of primes limited by range from 2 to value
        limited_primes_by_value = []

        # Output list
        prime_factors_list = []

        # Search for primes
        for i in range(2, value + 1):
            for j in limited_primes_by_value:
                if (j > int(sqrt(i) + 1)):
                    limited_primes_by_value.append(i)
                    break
                if (i % j == 0):
                    break
            else:
                limited_primes_by_value.append(i)

        # If value is a prime factor
        if (value in limited_primes_by_value):

            return 1

        # Decomposing value into primes factors
        index = 0
        while index < len(limited_primes_by_value):

            # Check for dividing by number from primes factors list
            if (value % limited_primes_by_value[index] == 0):

                # If goal add number to list
                prime_factors_list.append(limited_primes_by_value[index])

                # Divide value by found prime factor
                value //= limited_primes_by_value[index]

                # Start cycle again
                index = 0

            elif (value % limited_primes_by_value[index] != 0):
                index += 1

            # If value become 1 - break
            elif (value == 1):
                break

        return prime_factors_list
