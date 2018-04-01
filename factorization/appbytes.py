class AppStrings:
    '''Represents methods for working with strings'''

    @staticmethod
    def getPrimeFactorsString(prime_factors_list):
        '''Return readable string of prime factors like "2*2*3*3" for sending'''

        prime_factors_string = ''

        # Compose comfortable string from list
        for index, number in enumerate(prime_factors_list):

            if ((index + 1) != len(prime_factors_list)):
                char = str(number)
                prime_factors_string += char + '*'
            else:
                last_char = str(number)
                prime_factors_string += last_char

        return prime_factors_string
