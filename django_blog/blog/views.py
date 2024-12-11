from django.shortcuts import render, redirect, get_object_or_404
from django.views import generic
from django.urls import reverse_lazy, reverse
from django.contrib.auth.decorators import login_required
from .forms import CustomUserCreationForm, ProfileForm, UserForm, PostForm, CommentForm
from .models import Post, Comment
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

# Homepage View


class HomeView(generic.TemplateView):
    template_name = "blog/home.html"


# User Management Views


class UserCreateView(generic.CreateView):
    form_class = CustomUserCreationForm
    template_name = "registration/register.html"
    success_url = reverse_lazy("login")


@login_required
def edit_profile(request):
    user = request.user
    profile = user.profile

    if request.method == "POST":
        user_form = UserForm(data=request.POST, instance=user)
        profile_form = ProfileForm(request.POST, request.FILES, instance=profile)

        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            return redirect(reverse("home"))
    else:
        user_form = UserForm(instance=user)
        profile_form = ProfileForm(instance=profile)
    context = {
        "user_form": user_form,
        "profile_form": profile_form,
    }
    return render(request, "blog/edit_profile.html", context)


# Post Management Views


class PostListView(generic.ListView):
    model = Post
    template_name = "blog/post_list.html"
    context_object_name = "posts"


def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)  # Get the specific blog post
    comments = post.comments.all().order_by("-created_at")

    context = {
        "post": post,
        "comments": comments,
    }
    return render(request, "blog/post_detail.html", context)


class PostCreateView(LoginRequiredMixin, generic.CreateView):
    model = Post
    form_class = PostForm
    template_name = "blog/post_create.html"
    success_url = reverse_lazy("post_list")

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs["user"] = self.request.user  # Pass the logged-in user to the form
        return kwargs


class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, generic.UpdateView):
    model = Post
    form_class = PostForm
    template_name = "blog/post_update.html"

    def test_func(self):
        obj = self.get_object()
        return self.request.user == obj.author

    def get_success_url(self):
        # Use reverse_lazy with dynamic pk
        return reverse_lazy("post_detail", kwargs={"pk": self.object.pk})


class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, generic.DeleteView):
    model = Post
    template_name = "blog/post_delete.html"
    success_url = reverse_lazy("post_list")

    def test_func(self):
        obj = self.get_object()
        return self.request.user == obj.author


# Comment Management Views


class CommentCreateView(LoginRequiredMixin, generic.CreateView):
    model = Comment
    form_class = CommentForm
    template_name = "blog/comment_create.html"

    def get_form_kwargs(self):
        """Pass the post and user to the form."""
        kwargs = super().get_form_kwargs()
        # Fetch the post object based on the 'pk' in the URL
        kwargs["post"] = get_object_or_404(Post, id=self.kwargs["pk"])
        kwargs["user"] = self.request.user
        return kwargs

    def get_success_url(self):
        """Redirect to the post's detail view."""
        return reverse_lazy("post_detail", kwargs={"pk": self.kwargs["pk"]})


class CommentUpdateView(LoginRequiredMixin, UserPassesTestMixin, generic.UpdateView):
    model = Comment
    form_class = CommentForm
    template_name = "blog/comment_update.html"

    def get_object(self):
        """Retrieve the comment based on its primary key (pk)."""
        return get_object_or_404(Comment, id=self.kwargs["pk"])

    def get_success_url(self):
        """Redirect to the related post's detail view."""
        return reverse_lazy("post_detail", kwargs={"pk": self.object.post.id})

    def test_func(self):
        obj = self.get_object()
        return self.request.user == obj.author


class CommentDeleteView(LoginRequiredMixin, UserPassesTestMixin, generic.DeleteView):
    model = Comment
    template_name = "blog/comment_delete.html"

    def get_object(self):
        """Retrieve the comment based on its primary key (pk)."""
        return get_object_or_404(Comment, id=self.kwargs["pk"])

    def get_success_url(self):
        """Redirect to the related post's detail view after deletion."""
        return reverse_lazy("post_detail", kwargs={"pk": self.object.post.id})

    def test_func(self):
        obj = self.get_object()
        return self.request.user == obj.author


class CommentDetailView(generic.DetailView):
    model = Comment
    template_name = "blog/comment_detail.html"
    context_object_name = "comment"

    def get_object(self):
        """Fetch the comment ensuring it belongs to the specified post."""
        post = get_object_or_404(Post, id=self.kwargs["post_id"])
        return get_object_or_404(Comment, id=self.kwargs["comment_id"], post=post)


# class CommentCreateView(LoginRequiredMixin, generic.CreateView):
#     model = Comment
#     form_class = CommentForm
#     template_name = "blog/comment_create.html"

#     def get_form_kwargs(self):
#         """Pass the post and user to the form."""
#         kwargs = super().get_form_kwargs()
#         kwargs["post"] = get_object_or_404(Post, id=self.kwargs["pk"])
#         kwargs["user"] = self.request.user
#         return kwargs

#     def get_success_url(self):
#         """Redirect to the post's detail view."""
#         return reverse_lazy("post_detail", kwargs={"pk": self.kwargs["pk"]})


# class CommentUpdateView(LoginRequiredMixin, UserPassesTestMixin, generic.UpdateView):
#     model = Comment
#     form_class = CommentForm
#     template_name = "blog/comment_update.html"

#     def get_object(self):
#         """Retrieve the comment for the given post and comment IDs."""
#         post = get_object_or_404(Post, id=self.kwargs["post_id"])
#         return get_object_or_404(Comment, id=self.kwargs["comment_id"], post=post)

#     def get_form_kwargs(self):
#         """Pass the post and user to the form."""
#         kwargs = super().get_form_kwargs()
#         kwargs["post"] = get_object_or_404(Post, id=self.kwargs["post_id"])
#         kwargs["user"] = self.request.user
#         return kwargs

#     def get_success_url(self):
#         """Redirect to the post's detail view."""
#         return reverse_lazy("post_detail", kwargs={"pk": self.kwargs["post_id"]})

#     def test_func(self):
#         obj = self.get_object()
#         return self.request.user == obj.author


# class CommentDeleteView(LoginRequiredMixin, UserPassesTestMixin, generic.DeleteView):
#     model = Comment
#     template_name = "blog/comment_delete.html"

#     def get_object(self):
#         """Fetch the comment ensuring it belongs to the specified post."""
#         post = get_object_or_404(Post, id=self.kwargs["post_id"])
#         return get_object_or_404(Comment, id=self.kwargs["comment_id"], post=post)

#     def get_success_url(self):
#         """Redirect to the post's detail view after deletion."""
#         return reverse_lazy("post_detail", kwargs={"pk": self.kwargs["post_id"]})

#     def test_func(self):
#         obj = self.get_object()
#         return self.request.user == obj.author
