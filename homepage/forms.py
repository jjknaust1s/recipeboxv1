from django import forms
from homepage.models import Author


class AddRecipeForm(forms.Form):
    title = forms.CharField(max_length=40)
    author = forms.ModelChoiceField(queryset=Author.objects.all())
    description = forms.CharField(max_length=100)
    instructions = forms.CharField(widget=forms.Textarea)


class AddAuthorForm(forms.ModelForm):
    class Meta:
        model = Author
        fields = [
            'name',
            'bio'
        ]
