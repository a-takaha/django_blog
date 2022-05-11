from django.shortcuts import redirect, render, get_object_or_404
from  .forms import CommentCreateForm, CreatePost, CreateTitle
from blog.models import Post,Comment


def index(request):
    posts = Post.objects.all()
    context = {
        "posts" : posts,
    }
    return render(request, "blog/index.html", context)

def create(request):
   
    createTitle = CreateTitle()
    createPost = CreatePost()
    context  = {
        "title" : createTitle,
        "form" : createPost,
    }
    
    return render(request, "blog/create.html", context)

def store(request):
    post = Post(
        title = request.POST.get("title"),
        text = request.POST.get("text"),
        user = request.user,
    )
    post.save()
    return redirect(index)

def show(request, id):
    post = get_object_or_404(Post, pk=id)
    comments = Comment.objects.filter(target=id)
    context = {
        "post" : post,
        "comments" : comments,
    }
    return render(request, "blog/show.html", context)

def edit(request, id):
    post = get_object_or_404(Post, pk=id)    
    editTitle = CreateTitle()
    editPost = CreatePost()
    context = {
        "post" : post,
        "title" : editTitle,
        "form" : editPost,
    }


    return render(request, "blog/edit.html", context)

def update(request, id):
    post = Post(
        pk = id,
        title = request.POST.get('title'),
        text = request.POST.get('text'),
    )
    post.save(
        update_fields = [
            "title",
            "text",
            "updated_at"
        ]
    )
    return redirect(index)

def destroy(request, id):
    post = Post.objects.get(pk=id)
    post.delete()
    return redirect(index)

def comment(request, id):
    post = get_object_or_404(Post, pk=id)
    if request.method == "POST":
        commentCreateForm = CommentCreateForm(request.POST)
        if commentCreateForm.is_valid():
            comment = commentCreateForm.save(commit=False)
            comment.user = request.user
            comment.target = post
            comment.save()
            return redirect(show, id)
    else:
        commentCreateForm =CommentCreateForm()

    context  = {
        "post" : post,
        "form" : commentCreateForm,
    }

    return render(request, "blog/comment.html", context)