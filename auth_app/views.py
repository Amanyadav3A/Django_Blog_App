from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from home.models import input_post

# Creating views.
def register_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()  # Create the user
            login(request, user)  # Log the user in


            posts = input_post.objects.all()  # Get all posts
            username = request.user.username  # Get the username of the logged-in user

            for post in posts:
                # Use .copy() to avoid modifying immutable JSONField data
                user_like_list = post.user_like.copy()
                user_comment_list = post.user_comment.copy()

                # Add new data to the lists
                user_like_list.append({"username": username, "is_like": 0})
                user_comment_list.append({"username": username, "comments": []})

                # Assign updated lists back to the post fields
                post.user_like = user_like_list
                post.user_comment = user_comment_list
                post.save()  # Save the updated post

            return redirect(reverse('home:dashboard'))  # Redirect to the dashboard page

    # Initialize the form with empty data for the first GET request
    initial_data = {'username': '', 'password1': '', 'password2': ''}
    form = UserCreationForm(initial=initial_data)
    
    return render(request, 'register.html', context={'form': form})


def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data = request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request,user)
            return redirect(reverse('home:dashboard'))
    initial_data = {'username':'','password':''}
    form = AuthenticationForm(initial = initial_data)
    return render(request,'login.html',context={'form':form})    

@login_required
def logout_view(request):
    logout(request)
    return redirect('auth_app:login')
