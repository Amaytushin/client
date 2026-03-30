from django.shortcuts import render, redirect
from .models import Post  # Өөрийн үүсгэсэн Post моделийг импортлох
from .forms import PostForm

def post_list_view(request):
    # 1. Өгөгдлийн сангаас бүх post-ын мэдээллийг авах
    posts = Post.objects.all() 
    
    # 2. Мэдээллийг 'posts.html' файл руу дамжуулах
    # 'posts' гэсэн түлхүүр үгээр HTML дотор ашиглана
    return render(request, 'posts.html', {'posts': posts})


def create_post(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            form.save() # Өгөгдлийн санд хадгалах
            return redirect('post_list') # Амжилттай бол жагсаалт руу шилжих
    else:
        form = PostForm()
    
    return render(request, 'create_post.html', {'form': form})