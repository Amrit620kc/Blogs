from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Post,Contact,Comment
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login as auth_login,logout as auth_logout
from django.contrib import messages
from blogapp.templatetags import dict



from django.http import Http404





# Create your views here.
#For Html page
def home(request):
    postt=Post.objects.all()
    context={
        "post":postt,
    }
    return render(request,"home/index.html",context)

def about(request):
    return render(request,"home/about.html")

def blog(request):
    Blog=Post.objects.all()[:10]
    context={
        'blog':Blog,
    }
    return render(request,"home/blog.html",context)

def contact(request):
    if request.method=="POST":
        fname=request.POST['fname']
        lname=request.POST['lname']
        email=request.POST['email']
        message=request.POST['message']
        Data=Contact(fname=fname, lname=lname, email=email, message=message)
        Data.save()
        messages.success(request,"Successfully saved!")

    return render(request,"home/contact.html")

def show_more(request,url):
    show=Post.objects.get(url=url)
    show.views=show.views + 1
    show.save()
    comments=Comment.objects.filter(post=show,parent=None )
    replies=Comment.objects.filter(post=show).exclude(parent=None)
    replydict={}
  
    for reply in replies:
        if reply.parent.sno not in replydict.keys():
            replydict[reply.parent.sno]=[reply]
        else:
            replydict[reply.parent.sno].append(reply)
    
    context={
        "post":show,
        "comments":comments,
        "user":request.user,
        "replydict":replydict
    }
    return render(request, "home/show_more.html",context)

def search(request):
    search=request.GET['search']
    if len(search)>78:
        merge=Post.objects.none()
    else:
        posts=Post.objects.filter(body__icontains=search)
        title=Post.objects.filter(title__icontains=search)
        merge=posts.union(title)

    if merge.count()==0:
        messages.warning(request,"No search results found!")
      
    context={
        'posts':merge,
        'search':search
    }
    return render(request, 'home/search.html',context)


#For authentication
def signup(request):
    if request.method=="POST":
        username=request.POST['username']
        fname=request.POST['fname']
        lname=request.POST['lname']
        email=request.POST['email']
        pass1=request.POST['pass1']
        pass2=request.POST['pass2']
        if len(username)>15:
            messages.error(request,"username name must be under 10 characters!")
            return redirect('home')
        if not username.isalnum():
            messages.error(request,'please enter albhabetic & numberic!')
        if len(fname)>10:
            messages.error(request, "first name must be under 10 characters!")
            return redirect('home')
        if len(lname)>10:
            messages.error(request,"last name must be under 10 characters!")
            return redirect('home')
        if pass1!=pass2:
            messages.error(request,"Do not match your password")
            return redirect('home')
        
        user=User.objects.create_user(username=username, email=email, password=pass1)
        user.first_name=fname
        user.last_name=lname
        user.save()
        messages.success(request,f"{username} Your account has been successfully created!")
        return redirect("home")
        
    else:
       return HttpResponse("404- Not Found!")

def login(request):
    if request.method=="POST":
        username=request.POST['username']
        password=request.POST['password']
        loginuser=authenticate(username=username, password=password)
        if loginuser is not None:
            auth_login(request,loginuser)
            messages.success(request,"successfully logged In!")
            return redirect("home")
        else:
            return redirect('home')
            messages.error(request,"Invalid credentials Please try again!")
            
    return HttpResponse("404 - Not found!")

def logout(request):
    auth_logout(request)
    messages.success(request,"successfully logged out!")
    return redirect('home')



#For comment

'''def commentt(request):
    if request.method=='POST':
        comment=request.POST.get('comment')
        user=request.user
        postsno=request.POST.get('postsno')
        post=Post.objects.get(id=postsno)
        parentsno=request.POST.get('parentsno')

        if parentsno=="":
           Commentt=Comment(comment=comment,user=user, post=post)
           Commentt.save()
           messages.success(request,"comment has been posted successfully")
        else:
           parent=Comment.objects.get(sno=parentsno)
           Commentt=Comment(comment=comment,user=user, post=post,parent=parent)
           Commentt.save()
           messages.success(request,"reply has been posted successfully")
    return redirect(f'/show_more/{post.url}')'''

def commentt(request):

    if request.method == 'POST':
        comment = request.POST.get('comment')
        user = request.user
        postsno = request.POST.get('postsno')
        post = Post.objects.get(id=postsno)
        parentsno = request.POST.get('parentsno')
        print(parentsno)

        try:
            if parentsno == None:
                Commentt = Comment(comment=comment, user=user, post=post)
                Commentt.save()
                messages.success(request, "Comment has been posted successfully")
            else:
                parent = Comment.objects.get(sno=parentsno)
                Commentt = Comment(comment=comment, user=user, post=post, parent=parent)
                Commentt.save()
                messages.success(request, "Reply has been posted successfully")

        except Comment.DoesNotExist:
            raise Http404("Parent comment does not exist")

    return redirect(f'/show_more/{post.url}')