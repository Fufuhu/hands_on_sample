from django.views.generic import View
from django.shortcuts import render

class BaseView(View):
    def get(self, request):
        response_params = {}
        return render(request, 'base.html', response_params)