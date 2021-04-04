from django.shortcuts import render
from .models import Post
from .forms import PostForm

def post_list(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        print(request.POST['name'])
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            temp1 = request.POST['name'] + "さんは"
            temp2 =  (int(request.POST['money'])+ int(request.POST['money']) * 0.36)
            temp3 = "円です"
            post.text = temp1 + str(temp2) + temp3
            post.save()
            posts = Post.objects.all
            return render(request, 'chatApp/post_list.html', {'posts': posts})
    else:
        posts = Post.objects.all
        return render(request, 'chatApp/post_list.html', {'posts': posts})

