from django import forms
# from homepage.models import Author


class AddRecipeForm(forms.Form):
    title = forms.CharField(max_length=40)
    # author = forms.ModelChoiceField(queryset=Author.objects.all())
    description = forms.CharField(max_length=100)
    instructions = forms.CharField(widget=forms.Textarea)


class AddAuthorForm(forms.Form):
    name = forms.CharField(max_length=150)
    bio = forms.CharField(max_length=100)


class SignupForm(forms.Form):
    name = forms.CharField(max_length=150)
    bio = forms.CharField(max_length=100)
    username = forms.CharField(max_length=36)
    password = forms.CharField(widget=forms.PasswordInput)


class LoginForm(forms.Form):
    username = forms.CharField(max_length=36)
    password = forms.CharField(widget=forms.PasswordInput)
