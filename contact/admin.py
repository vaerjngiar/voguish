from django.contrib import admin
from .forms import ContactForm
from .models import Contact


class ContactAdmin(admin.ModelAdmin):
    list_display = ['sender', 'subject', 'created']

admin.site.register(Contact, ContactAdmin)