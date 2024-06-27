from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

from .models import Profile, Post

# I wrote this code 

# Define a custom registration form, based on UserCreationForm.
class RegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]
    
    
    def __init__(self, *args, **kwargs):
        super(RegisterForm, self).__init__(*args, **kwargs)
        
        # Add bootstrap classes for the input and label tags in form
        self.fields["username"].widget.attrs["class"] = "form-control"
        self.fields["email"].widget.attrs["class"] = "form-control"
        self.fields["password1"].widget.attrs["class"] = "form-control"
        self.fields["password2"].widget.attrs["class"] = "form-control"

# Define a form for editing user profiles, based on ModelForm.
class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ["bio", "location", "image"]
        
        
    def __init__(self, *args, **kwargs):
        super(ProfileForm, self).__init__(*args, **kwargs)
        
        # Add bootstrap classes for the input and label tags in form
        self.fields["bio"].widget.attrs["class"] = "form-control"
        self.fields["location"].widget.attrs["class"] = "form-control"
        self.fields["image"].widget.attrs["class"] = "form-control"

# Define a form for creating and editing posts, based on ModelForm.
class PostForm(forms.ModelForm):
    caption = forms.CharField(required=True, 
                           widget=forms.widgets.Textarea(attrs={"class":"form-control"}))
    class Meta:
        model = Post
        exclude = ["user"]
        
    def __init__(self, *args, **kwargs):
        super(PostForm, self).__init__(*args, **kwargs)
        self.fields["image"].widget.attrs["class"] = "form-control"
# end of code I wrote




        