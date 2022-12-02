from django.shortcuts import render, redirect
from django.views.generic import View
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from .forms import RegisterBuyerForm, LoginBuyerForm
from .models import Buyer


class RegisterBuyerView(View):
    def get(self, request, *args, **kwargs):
        template_name = 'accounts/register.html'
        form = RegisterBuyerForm()
        context = {
            'form': form
        }

        return render(request, template_name, context)

    def post(self, request, *args, **kwargs):
        if request.method == 'POST':
            if request.POST['password1'] == request.POST['password2']:
                form = RegisterBuyerForm(request.POST)
                if form.is_valid():
                    buyer = Buyer.objects.create_user(username=form.cleaned_data['username'], password=form.cleaned_data['password1'])
                    buyer.save()
                    login(request, buyer)

                    return redirect('products:home')
                else:
                    for msg in form.errors:
                        messages.error(request, form.errors[msg])

                    context = {
                        'form': form
                    }

                    return render(request, 'accounts/register.html', context)
            else:
                form = RegisterBuyerForm()
                context = {
                    'form': form,
                    'error': 'Sus contraseñas no son iguales'
                }

                return render(request, 'accounts/register.html', context)


class LogoutBuyerView(View):
    def get(self, request, *args, **kwargs):
        logout(request)
        return redirect('products:home')


class LoginBuyerView(View):
    def get(self, request, *args, **kwargs):
        form = LoginBuyerForm()
        context = {
            'form': form,
        }

        return render(request, 'accounts/login.html', context)

    def post(self, request, *args, **kwargs):
        form = LoginBuyerForm()
        if request.method == 'POST':
            buyer = authenticate(request, username=request.POST['username'], password=request.POST['password'])

            if buyer is None:
                context = {
                    'form': form,
                    'error': 'Usuario o contraseña incorrecto'
                }

                return render(request, 'accounts/login.html', context)
            else:
                login(request, buyer)
                return redirect('products:home')
