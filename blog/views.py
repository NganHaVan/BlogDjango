from blog.forms import CommentForm, PostForm, UserForm, UserProfileForm
from blog.models import Comment, Post
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse_lazy, reverse
from django.utils import timezone
from django.views.generic import (CreateView, DeleteView, DetailView, ListView,
                                  TemplateView, UpdateView)

# Create your views here.


class AboutView(TemplateView):
    template_name = "about.html"


class PostListView(ListView):
    model = Post
    context_object_name = "post_list"

    """ def get_queryset(self):
        return Post.objects.filter(published_date__lte=timezone.now()).order_by('-published_date') """

    """ context_object_name = ''
    template_name = '' """


class PostDetailView(DetailView):
    model = Post
    # template_name = ''


class PostCreateView(LoginRequiredMixin, CreateView):
    login_url = "/auth/login/"
    redirect_field_name = "blog/post_detail.html"
    form_class = PostForm
    model = Post


class PostUpdateView(LoginRequiredMixin, UpdateView):
    login_url = "/auth/login/"
    redirect_field_name = "blog/post_detail.html"
    form_class = PostForm
    model = Post


class PostDeleteView(LoginRequiredMixin, DeleteView):
    model = Post
    success_url = reverse_lazy('post_list')


class DraftPostListView(LoginRequiredMixin, ListView):
    model = Post
    login_url = "/auth/login/"
    redirect_field_name = "blog/post_list.html"
    """ context_object_name = ''
    template_name = '' """

    """ def get_queryset(self):
        return Post.objects.filter(published_date__isnull=True).order_by('-create_date') """
#####################


def register(request):
    if request.method == "POST":
        user_form = UserForm(data=request.POST)
        profile_form = UserProfileForm(data=request.POST)
        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            # Hash password
            user.set_password(user.password)
            user.save()

            profile = profile_form.save(commit=False)
            profile.user = user

            if 'profile_pic' in request.FILES:
                profile.profile_pic = request.FILES['profile_pic']

            profile.save()
            reverse('blog:post_list')
        else:
            print(user_form.errors, profile_form.errors)
    else:
        user_form = UserForm()
        profile_form = UserProfileForm()
    return render(request, "registration/register.html", {'user_form': user_form, 'profile_form': profile_form})


@login_required
def post_publish(request, pk):
    post = get_object_or_404(Post, pk=pk)
    post.publish()
    return redirect('post_detail', pk=pk)


@login_required
def add_comment_to_post(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        print(form)
        if form.is_valid():
            comment = form.save(commit=False)
            # post is an attribute of Comment model which is connected as FOREGIN_KEY
            comment.post = post
            comment.author = request.user
            comment.save()
            return redirect('blog:post_detail', pk=post.pk)
    else:
        form = CommentForm()
        return render(request, 'blog/comment_form.html', {'form': form})


@login_required
def comment_approval(request, pk):
    comment = get_object_or_404(Comment, pk=pk)
    comment.approve()
    return redirect('post_detail', pk=comment.post.pk)


@login_required
def comment_remove(request, pk):
    comment = get_object_or_404(Comment, pk=pk)
    post_pk = comment.post.pk
    comment.delete()
    return redirect('post_detail', pk=post_pk)
