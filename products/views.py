from django.shortcuts import render, redirect
from django.views.generic import View


class HomeView(View):
    def get(self, request, *args, **kwargs):
        template_name = 'products/index.html'
        context = {}

        return render(request, template_name, context)
