from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Post, Comment
from .forms import PostForm, EditForm, CommentForm
from django.urls import reverse_lazy, reverse
from django.http import HttpResponseRedirect
# Create your views here.
class HomeView(ListView):
    model = Post
    template_name = 'home.html'
    ordering = ['-post_date']
    # ordering = ['-id']

def Likeview(request, pk):
    like = get_object_or_404(Post, id=request.POST.get('post_id'))
    liked = False
    if like.likes.filter(id=request.user.id).exists():
        like.likes.remove(request.user)
        liked = False
    else:
        like.likes.add(request.user)
        liked = True
    return HttpResponseRedirect(reverse('post_detail', kwargs={'pk':pk}))

def userpost(request, pk):
    user_post = Post.objects.filter(author__id=pk)
    return render(request, 'userpost.html',{'user_post':user_post})

class PostDetailView(DetailView):
    model = Post
    template_name = 'post_detail.html'

    def get_context_data(self, *args, **kwargs):
        context = super(PostDetailView, self).get_context_data()
        info = get_object_or_404(Post, id=self.kwargs['pk'])
        total_likes = info.total_likes()
        liked = False
        if info.likes.filter(id=self.request.user.id).exists():
            liked = True
        context["total_likes"] = total_likes
        context["liked"] = liked
        return context

class AddPostView(CreateView):
    model = Post
    form_class = PostForm
    template_name = 'add_post.html'
    # fields = '__all__'

class PostUpdateView(UpdateView):
    model = Post
    form_class = EditForm
    template_name = 'edit_post.html'
    # fields = ['title', 'title_tag', 'body']

class PostDeletelView(DeleteView):
    model = Post
    template_name = 'post_delete.html'
    success_url = reverse_lazy('home')

#####Comment########
