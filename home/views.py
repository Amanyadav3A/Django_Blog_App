from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import input_post
from datetime import datetime
from django.contrib.auth.models import User

#for rest framework
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import post_serializer


# Creating views .
@login_required
def home_view(request):
    isLike = []
    comment = []
    posts = input_post.objects.all().order_by('-time')
    username = request.user.username
    for post in posts:
        temp = []
        for data in post.user_like:
            if(data["username"] == username):
                isLike.append(data["is_like"])
        for item in post.user_comment:
            u_name = item["username"]
            if item["comments"]:
                for i in item["comments"]:
                    temp.append({"u_name":u_name,"comment": i})
        comment.append(temp)  

    posts = zip(posts,isLike,comment)           
            
    return render(request,'home.html',context={'posts':posts})

@login_required
def dashboard_view(request):
    name = request.user.username
    posts = input_post.objects.filter(author__username = name).order_by('-time')
    total_like = []
    total_comment = []
    
    if posts.exists():
        for post in posts:
            temp = []
            total_like.append(post.like)
            for item in post.user_comment:
                username = item["username"]
                for data in item["comments"]:
                    if data:
                        temp.append({"username":username, "comments":data})
            total_comment.append(temp)            

        posts = zip(posts,total_like,total_comment)

    return render(request,'dashboard.html',context={'posts':posts,'name':name})

@login_required
def create_post(request):
    if request.method == 'POST':
        user = request.user
        heading = request.POST.get('heading')
        desc = request.POST.get('desc')
        time = datetime.now()
        
        # Fetch all users only once (efficient way)
        users = User.objects.values_list('username', flat=True)

        # Create user_like and user_comment lists
        user_like = [{"username": username, "is_like": 0} for username in users]
        user_comment = [{"username": username, "comments": []} for username in users]

        input_post.objects.create(heading = heading, desc = desc, author = user, time = time, user_comment = user_comment, user_like = user_like)
        return redirect('home:dashboard')
    return render(request,'input_post.html')

@login_required
def update_post(request,id):
    post = input_post.objects.get(id = id)
    if request.method == 'POST':
        post.heading = request.POST.get('heading')
        post.desc = request.POST.get('desc')
        post.time = datetime.now()
        post.save()
        return redirect('home:dashboard')
    return render(request,'update_post.html',context={'post':post})

@login_required
def delete_post(request,id):
    input_post.objects.get(id = id).delete()
    return redirect('home:dashboard')


# for rest api

@api_view(['PATCH'])
def post_api(request,id):
    id = int(id)
    if request.method == 'PATCH':
        temp = []
        obj = input_post.objects.get(id = id)
        # i am going to update user_like
        user_likes = obj.user_like
        for data in user_likes:
            if data['username'] == request.user.username:
                if data["is_like"] == 0:
                    data["is_like"] = 1
                else:
                    data["is_like"] = 0    
            temp.append(data)
        obj.user_like = temp
        obj.save()     
        #now i am going to update by api
        obj = input_post.objects.get(id = id)
        data = request.data  
        print(data)           
        serializer = post_serializer(obj, data = data, partial = True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)


@api_view(['PATCH'])
def comment_api(request, id):
    if request.method == 'PATCH':
        data = request.data
        comment = data["comments"]
        username = request.user.username
        id = int(id)
        obj = input_post.objects.get(id = id)
        user_comment = obj.user_comment
        for item in user_comment:
            if item["username"] == username:
                item["comments"].append(comment)

        obj.user_comment = user_comment
        obj.save()        
        
        return Response(data)

    
