from django.shortcuts import render
from django.views.generic import FormView
from .forms import ContactForm
from django.http import HttpResponseRedirect


class ContactView(FormView):
    template_name = 'contact/contact.html'
    form_class = ContactForm
    success_url = '/contact/'

    def get_context_data(self, **kwargs):
        context = super(ContactView, self).get_context_data(**kwargs)
        return context

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            # instance.user = request.user
            form.name = form.cleaned_data.get('name')
            form.sender = form.cleaned_data.get('sender')
            form.subject = form.cleaned_data.get('subject')
            instance.save()
            return HttpResponseRedirect('/contact/')

        return render(request, self.template_name, {'form': form,
                                                    })


