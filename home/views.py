from django.shortcuts import render
from django.views.generic import TemplateView, FormView
from django.http import HttpResponseRedirect
from .forms import SignUpForm


class HomeView(FormView):
    template_name = 'home/home.html'
    form_class = SignUpForm

    def get_context_data(self, **kwargs):
        context = super(HomeView, self).get_context_data(**kwargs)
        return context

    def post(self, request, *args, **kwargs):
        sign_up_form = self.form_class(request.POST)
        if sign_up_form.is_valid():
            instance = sign_up_form.save(commit=False)
            sign_up_form.email = sign_up_form.cleaned_data.get('email')
            instance.save()
            return HttpResponseRedirect('/about/')

        return render(request, self.template_name, {'sign_up_form': sign_up_form, })

