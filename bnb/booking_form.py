from django import forms


class AvailableForm(forms.Form):
    HOUSE_CATEGORIES = (
        ('BAS', 'BASIC'),
        ('LUX', 'LUXURIUS'),
        ('KIN', 'KING'),
        ('QUE', 'QUEEN'),
    )
    house_category = forms.ChoiceField(choices=HOUSE_CATEGORIES, required=True)
    check_in = forms.DateTimeField(required=True, input_formats=['%Y-%m-%dT%H:%M'])
    check_out = forms.DateTimeField(required=True, input_formats=['%Y-%m-%dT%H:%M'])
