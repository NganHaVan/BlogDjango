from blog.models import Comment, Post, UserProfile
from django import forms
from django.contrib.auth.models import User


class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ('username', 'email', 'password')


class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ('profile_pic',)


class PostForm(forms.ModelForm):

    # Metadata
    class Meta:
        model = Post
        fields = ('author', 'title', 'content')
        """ widgets = {
            "title": forms.TextInput(attrs={'class': 'textinputclass'}),
            "content": forms.Textarea(attrs={'class': 'editable medium-editor postcontent'})
        } """


class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ("content",)
        """ widgets = {
            "content": "editable medium-editor postcontent"} """
