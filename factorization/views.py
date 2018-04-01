import os

from .appmath import AppMath
from .appbytes import AppStrings

from django.shortcuts import render
from .forms import UserNumberForm


def index(request):
    '''Render the main page'''

    # Path to html-page that django render when user open http://127.0.0.1:8000/ or main page
    path = 'for_factorization_app' + os.sep + 'includes' + os.sep + 'index.html'

    return render(request, path)


def getFactorizationPage(request):
    '''Render the factorization page
    At this page user can input integer number and send it to server'''

    path = 'for_factorization_app' + os.sep + 'includes' + os.sep + 'factorization.html'

    return render(request, path)


def getAnswerPage(request):
    '''Process validation and calculates the prime factors
    If user sent wrong data - render something_went_wrong page'''

    path = 'for_factorization_app' + os.sep + 'includes' + os.sep + 'something_went_wrong.html'

    # If POST request we need to process the form data
    if (request.method == 'POST'):

        # Path to answer page
        path = 'for_factorization_app' + os.sep + 'includes' + os.sep + 'answer.html'

        # Create a form instance and write data from the request
        form = UserNumberForm(request.POST)

        # Process validation
        if (form.is_valid()):

            # Get cleaned data
            dictionary = form.cleaned_data

            # Get user number from dictionary by key 'user_value'
            user_value = dictionary['user_value']

            # Transform user number into list of prime factors
            prime_factors_list = AppMath.decomposeNumber(user_value)

            # If value is a prime factor
            if (prime_factors_list == 1):

                # Create context(dictionary) for sending
                context = dict(answer_key=["It's", 'a', 'prime'])

                return render(request, path, context)

            # Transform this list to string for sending
            primes_factors_string = AppStrings.getPrimeFactorsString(prime_factors_list)

            # Create context(dictionary) for sending
            context = dict(answer_key=primes_factors_string)

            return render(request, path, context)

        else:

            path = 'for_factorization_app' + os.sep + 'includes' + os.sep + 'something_went_wrong.html'

            return render(request, path)

    # If a GET request or other we'll create a blank form
    else:
        form = UserNumberForm()

    return render(request, path, {'form': form})
