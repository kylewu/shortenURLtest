from django import forms


class URLForm(forms.Form):

    originURL = forms.URLField(max_length=256)
