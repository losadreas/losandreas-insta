from django.contrib.auth import logout, login, get_user_model
from django.contrib.auth.tokens import PasswordResetTokenGenerator
from django.core.mail import EmailMessage
from django.http import JsonResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.template.defaulttags import register
from django.urls import reverse_lazy
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.views import View
from django.views.generic import CreateView

from project.settings import DEFAULT_FROM_EMAIL
from .forms import CustomUserCreationForm, CustomUserChangeForm, CreatePostForm
from .models import User, Post, Image

User = get_user_model()


class ConfirmEmail(View):
    def get(self, request, *args, **kwargs):
        template = "confirm_email.html"
        return render(request, template)


class CheckLink(View):
    def get(self, request, *args, **kwargs):
        template = "check_link.html"
        return render(request, template)


class SignUp(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy("confirm_email")
    template_name = "register.html"

    def post(self, request, *args, **kwargs):
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            user = User.objects.get(email=request.POST.get("email"))
            account_activation_token = PasswordResetTokenGenerator()
            user.token = account_activation_token.make_token(user)
            user.is_active = False
            user.save()
            message = f'Verify email Follow the link {request._current_scheme_host}/users/verify_email/{user.token}/{str(urlsafe_base64_encode(force_bytes(user.pk)))}/'
            email = EmailMessage('Verify email', message, from_email=DEFAULT_FROM_EMAIL, to=[user.email])
            email.send()
            return redirect('confirm_email')
        context = {'form': form}
        return render(request, self.template_name, context)

    def get(self, request, *args, **kwargs):
        logout(request)
        result = super(SignUp, self).get(request, *args, **kwargs)
        return result


class VerifyEmail(View):
    template_name = 'verify_email.html'

    def get(self, request, token, pk_code):
        user = User.objects.get(pk=urlsafe_base64_decode(pk_code).decode())
        if user.token == token:
            user.is_active = True
            user.save()
            login(request, user, backend='django.contrib.auth.backends.ModelBackend')
        else:
            return redirect('check_link')
        return redirect('addition_info')


class AdditionInfo(CreateView):
    form_class = CustomUserChangeForm
    success_url = reverse_lazy("home")
    template_name = "addition_info.html"

    def post(self, request, *args, **kwargs):
        form = CustomUserChangeForm(request.POST, request.FILES, instance=request.user)
        if form.is_valid():
            form.save()
        return redirect('post')

    def get(self, request, *args, **kwargs):
        return super(AdditionInfo, self).post(request, *args, **kwargs)


class PostView(View):

    def get(self, request, *args, **kwargs):
        if request.user.id is None:
            return redirect('login')
        posts = Post.objects.order_by('-date_posted')
        images = Image.objects.all()
        template = "post.html"
        return render(request, template, {'post': posts, 'images': images})


class CreatePost(CreateView):
    form_class = CreatePostForm
    template_name = "create_post.html"

    def post(self, request, *args, **kwargs):
        form = CreatePostForm(request.POST, request.FILES)
        if form.is_valid():
            files = request.FILES.getlist('all_images')
            form = form.save(commit=False)
            form.user = request.user
            form.save()
            post_pk = form.pk
            for file in files:
                Image.objects.create(images=file, post_id=post_pk)
            return redirect('/post')
        context = {'form': form}
        return render(request, self.template_name, context)

    def get(self, request, *args, **kwargs):
        if request.user.id is None:
            return redirect('login')
        return super(CreatePost, self).get(self, request, *args, **kwargs)


def likeview(request, pk):
    post = get_object_or_404(Post, id=pk)
    if post not in Post.objects.filter(likes=request.user.id):
        post.quantity_likes += 1
        post.likes.add(request.user)
    else:
        post.quantity_likes -= 1
        post.likes.remove(request.user)
    post.save()
    likes_dislikes = check_likes(pk, request.user)
    return JsonResponse({'quantity_likes': post.quantity_likes, 'likes_dislikes': likes_dislikes}, status=200)


class HomeView(View):
    def get(self, request, *args, **kwargs):
        template = "home.html"
        return render(request, template)


class LogOut(View):
    def get(self, request, *args, **kwargs):
        logout(request)
        template = 'logout.html'
        return render(request, template)


class UserView(View):
    def get(self, request, user_id):
        if request.user.id is None:
            return redirect('login')
        template = 'user_view.html'
        user = User.objects.get(id=user_id)
        return render(request, template, {'user_view': user})


@register.simple_tag
def check_likes(pk, user):
    post = get_object_or_404(Post, id=pk)
    if post not in Post.objects.filter(likes=user.id):
        return 'Like'
    else:
        return 'Dislike'


def login_error_view(request):
    return render(request, 'login_error.html')
