from django import forms
from wiki.models import Page


class PageForm(forms.ModelForm):
     class Meta:
    # """ Render and process a form based on the Page model. """
        model = Page
        fields = ("title", "content", "author")
