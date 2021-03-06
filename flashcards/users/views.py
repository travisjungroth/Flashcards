from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import TemplateView

from .forms import CreateAccountForm


class SignupView(View):
    form_class = CreateAccountForm
    template_name = 'users/signup.html'

    def get(self, request, *args, **kwargs):
        form = self.form_class()
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Account created successfully')
            return redirect('users:login')
        else:  # Invalid form
            return render(request, self.template_name, {'form': form})


class UserDetailsView(LoginRequiredMixin, TemplateView):
    template_name = 'users/details.html'
    login_url = reverse_lazy('users:login')
