from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import PasswordChangeView as PasswordView
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.views import generic
from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.conf import settings
from portfo.apps.accounts.forms import SignUpForm, EditProfileForm, PasswordChangeForm, UserDeleteForm
from django.contrib import messages


class PasswordChangeView(PasswordView):
    form_class = PasswordChangeForm
    success_url = reverse_lazy('password_change_success')

    @staticmethod
    def password_change_success(request):
        return render(request, 'accounts/password_change_success.html')


class SignUpView(generic.CreateView):
    form_class = SignUpForm
    template_name = 'accounts/signup.html'
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        valid = super().form_valid(form)
        username, password = form.cleaned_data.get('username'), form.cleaned_data.get('password1')
        new_user = authenticate(username=username, password=password)
        login(self.request, new_user)
        return valid

    def dispatch(self, *args, **kwargs):
        if self.request.user.is_authenticated:
            return redirect('home')
        return super().dispatch(*args, **kwargs)


class EditProfileView(generic.UpdateView):
    form_class = EditProfileForm
    template_name = 'accounts/profile.html'
    success_url = reverse_lazy('home')

    def get_object(self, queryset=None):
        return self.request.user

    @staticmethod
    @login_required
    def delete_account(request):
        if request.method == 'POST':
            delete_form = UserDeleteForm(request.POST, instance=request.user)
            user = request.user
            user.delete()
            messages.info(request, 'Your account has been deleted.')
            return redirect('home')
        else:
            delete_form = UserDeleteForm(instance=request.user)

        context = {
            'delete_form': delete_form
        }

        return render(request, 'accounts/delete_account.html', context)

