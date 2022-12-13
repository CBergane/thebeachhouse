from django import forms


class AvailableForm(forms.Form):

    check_in = forms.DateTimeField(
        required=True, input_formats=['%Y-%m-%d', ])
    check_out = forms.DateTimeField(
        required=True, input_formats=['%Y-%m-%d', ])
