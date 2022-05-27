from django import forms


class ReviewForm(forms.Form):
    text = forms.CharField(label='text', max_length=255)