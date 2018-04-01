from django import forms


class UserNumberForm(forms.Form):
    '''Represents form for user number'''

    # We should limit range of number for safe process data
    user_value = forms.IntegerField(label='Your number', min_value=2, max_value=1000000)
