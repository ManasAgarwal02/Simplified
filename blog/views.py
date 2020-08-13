from django.contrib import messages
from django.shortcuts import render, redirect

from .models import Blog, BlogComment
from blog.templatetags import extras

# Create your views here.

def index(request):
    blogs = Blog.objects.all()
    context = {'allBlogs': blogs}
    return render(request, 'blog/blogHome.html', context)


def blogpost(request, smug):
    blog = Blog.objects.filter(smug=smug)[0]
    comments = BlogComment.objects.filter(post=blog, parent=None)
    replies = BlogComment.objects.filter(post=blog).exclude(parent=None)
    replyDict = {}
    for reply in replies:
        if reply.parent.Sno not in replyDict.keys():
            replyDict[reply.parent.Sno] = [reply]
        else:
            replyDict[reply.parent.Sno].append(reply)
    context = {'blog': blog, 'comments': comments, 'user': request.user, 'replyDict': replyDict}
    return render(request, 'blog/blogpost.html', context)


def postComment(request):
    if request.method == "POST":
        comment = request.POST["comment"]
        user = request.user
        postSno = request.POST.get("postSno")
        parentSno = request.POST.get("commentSno")
        post = Blog.objects.get(blog_id=postSno)

        if parentSno == "":
            comment = BlogComment(comment=comment, user=user, post=post)
            messages.success(request, "Comment has been added successfully!")
        else:
            parent = BlogComment.objects.get(Sno=parentSno)
            comment = BlogComment(comment=comment, user=user, post=post, parent=parent)
            messages.success(request, "Reply has been added successfully!")
        comment.save()

    return redirect(f'/blog/{post.smug}/')
