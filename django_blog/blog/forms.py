from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Profile, Post, Comment


class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(
        required=True, help_text="Required. Enter a valid email address."
    )

    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]

    def clean_email(self):
        email = self.cleaned_data.get("email")
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError("A user with that email already exists.")
        return email

    def save(self, commit=True):
        user = super().save(commit=False)
        user.email = self.cleaned_data["email"]
        if commit:
            user.save()
        return user


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ("username", "email")

    def clean_email(self):
        email = self.cleaned_data.get("email")
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError("A user with that email already exists.")
        return email

    def save(self, commit=True):
        user = super().save(commit=False)
        user.email = self.cleaned_data["email"]
        if commit:
            user.save()
        return user


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ("bio", "profile_picture")


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        exclude = ("published_date", "author")

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop("user", None)  # Get the user from kwargs
        super().__init__(*args, **kwargs)

    def save(self, commit=True):
        instance = super().save(commit=False)
        if self.user:
            instance.author = self.user  # Automatically assign the logged-in user
        if commit:
            instance.save()
        return instance


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ("content",)  # Only 'content' is editable by the user

    def __init__(self, *args, **kwargs):
        # Extract 'post' and 'user' from kwargs
        post = kwargs.pop(
            "post", None
        )  # Use pop to avoid passing them to the parent class
        user = kwargs.pop("user", None)

        # Initialize the form
        super().__init__(*args, **kwargs)

        # Set the initial values for 'post' and 'author' if provided
        if post:
            self.instance.post = (
                post  # Set the post instance directly on the form's model instance
            )
        if user:
            self.instance.author = (
                user  # Set the author instance directly on the form's model instance
            )
