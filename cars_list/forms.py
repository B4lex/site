from django import forms


class UpdateForm(forms.Form):
    start_page = forms.IntegerField(initial=1)
