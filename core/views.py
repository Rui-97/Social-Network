from django.shortcuts import render,redirect
from django.http import Http404
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.models import User

import os
from django.conf import settings

from .forms import RegisterForm, ProfileForm, PostForm
from .models import Profile, Post

# I wrote this code 

# The landing view renders the landing page of the application.
def landing(request):
    return render(request, "core/landing.html")

# The register view handles user registration.
def register(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get("username")
            messages.success(request, f"The user {username} has been successfully created. You can login now.")
            return redirect("/login/")
        else: 
            return render(request, "core/register.html", {"form": form})
            
    form = RegisterForm()
    return render(request, "core/register.html", {"form": form})

# The user_login view handles user login.
def user_login(request):
    if request.method == "POST":
        usernmae = request.POST["username"]
        password = request.POST["password"]
        
        user = authenticate(username=usernmae, password=password)
        print(user)
        if user is not None:
            login(request, user)
            return redirect(f"/home/{user.id}")
        else:
            messages.info(request, "Invalid login details supplied. Please try again")
            return redirect("/login")

    return render(request,"core/login.html")

# The user_logout view handles user logout.
@login_required(login_url="/login/")
def user_logout(request):
    logout(request)
    return redirect("/login")

# The home view displays posts from users the current user is following.    
@login_required(login_url="/login/")
def home(request, pk):
    #Display only the posts created by the users that the current login user is following
    current_user_profile = Profile.objects.get(user=request.user)
    following_profiles = current_user_profile.follows.all()
    following_user_ids = following_profiles.values_list("user", flat=True)
    posts = Post.objects.filter(user_id__in=following_user_ids).order_by("-created_time")
    
    if request.method == "POST":
        form = PostForm(request.POST,request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = request.user
            post.save()
            messages.success(request, "Your post have been successfully uploaded!")
    form = PostForm()        
    return render(request,"core/home.html", {"posts": posts, "form": form})


# The profile view displays a user's profile.
@login_required(login_url="/login/")   
def profile(request, pk):
    profile = Profile.objects.get(user_id=pk)
    posts = Post.objects.filter(user_id=pk).order_by("-created_time")
    if request.method == "POST":
        # Get the current user
        current_user_profile = request.user.profile
        action = request.POST["action"]
        if action == "follow":
            current_user_profile.follows.add(profile)
            success_message = f"You have successfully followed {profile.user}"
        elif action == "unfollow":
            current_user_profile.follows.remove(profile)
            success_message = f"You have successfully unfollowed {profile.user}"
  
        current_user_profile.save()
        messages.success(request, success_message)
    
    return render(request,"core/profile.html", {"profile": profile, "posts":posts}) 

# The profile_following view displays users that a user is following.
@login_required(login_url="/login/")   
def profile_following(request, pk):
    try:
        profile = Profile.objects.get(user_id=pk)
    except Profile.DoesNotExist:
        raise Http404("Profile not exist")
    
    return render(request,"core/profile_following.html", {"profile": profile})

# The profile_followers view displays users following a user.
@login_required(login_url="/login/")   
def profile_followers(request, pk):
    profile = Profile.objects.get(user_id=pk)
    return render(request,"core/profile_followers.html", {"profile": profile})        

# The profile_update view allows a user to update their profile.
@login_required(login_url="/login/")
def profile_update(request, pk):
    # Retirve the profile that needs to be updated
    profile = Profile.objects.get(user_id = pk)
    if request.method == "POST":
        form = ProfileForm(request.POST, request.FILES, instance = profile)
        if form.is_valid():
            form.save()
            messages.success(request, "Your profile has been uploaded!")
            return redirect(f"/profile/{pk}")
            
    form = ProfileForm(instance = profile)
    return render(request,"core/profile_update.html", {"form": form})   
    
# The search view allows users to search for other users.
@login_required(login_url="/login/")
def search(request):
    search_content = request.GET["search"]
    searched_users = User.objects.filter(username__contains = search_content)
    return render(request, "core/search.html", {"searched_users": searched_users, "search_content": search_content})

# The delete_post view allows a user to delete their own posts.
@login_required(login_url="/login/")
def delete_post(request,pk):
    post = Post.objects.get(id=pk)
    if request.method == "POST":
        # Delete the post from the database
        post.delete()
        if post.image:
            # Delete the image from the media directory
            img_abs_path = os.path.join(settings.MEDIA_ROOT, str(post.image))
            os.remove(img_abs_path)
            
            messages.success(request, "The post has been successfully deleted!")
        return redirect(f"/home/{request.user.id}")
        
        
@login_required(login_url="/login/")
def api_index(request):
    return render(request, "core/api_index.html")      

# end of code I wrote
