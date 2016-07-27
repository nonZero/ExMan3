import random

from django import forms
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.core.mail import mail_admins
from django.core.urlresolvers import reverse
from django.http.response import HttpResponseNotFound
from django.shortcuts import render, get_object_or_404, redirect

from . import models


class ContactUsForm(forms.Form):
    email = forms.EmailField()
    subject = forms.CharField()
    message = forms.CharField(widget=forms.Textarea)
    # date = forms.DateField()


def contact_us_view(request):
    if request.method == "POST":
        form = ContactUsForm(request.POST)

        if form.is_valid():
            mail_admins(form.cleaned_data['subject'],
                        form.cleaned_data['message'])

            messages.success(request, "Your message was sent. Thank you!")

            return redirect(reverse("expenses:list"))

    else:
        form = ContactUsForm()

    return render(request, "form.html", {
        'form': form,
    })


# class LoginForm(forms.Form):
#     username = forms.CharField()
#     password = forms.CharField(widget=forms.PasswordInput())
#
#
# def login_view(request):
#     if request.method == "POST":
#         form = LoginForm(request.POST)
#
#         if form.is_valid():
#             user = authenticate(**form.cleaned_data)
#             if user:
#                 login(request, user)
#                 return redirect(reverse("expenses:list"))
#             form.add_error(None, "User / Password does not match")
#
#     else:
#         form = LoginForm()
#
#     return render(request, "form.html", {
#         'title': 'Login',
#         'form': form,
#     })


# def logout_view(request):
#     logout(request)
#     messages.info(request, "bye bye!")
#     return redirect(reverse("expenses:list"))


# list: modelname_list
# single: modelname_detail

@login_required
def expense_list(request):



    qs = models.Expense.objects.order_by('-created_at')

    # TODO: fix name to meet convention
    return render(request, "expense_list.html", {
        'object_list': qs,
    })


@login_required
def expense_detail(request, id):
    o = get_object_or_404(models.Expense, id=id)

    # TODO: fix name to meet convention
    return render(request, "expense_detail.html", {
        'object': o,
    })


# class CreateExpenseView(CreateView):
#     model = models.Expense
#     fields = '__all__'


class ExpenseForm(forms.ModelForm):
    class Meta:
        model = models.Expense
        fields = '__all__'


@login_required
def expense_create_view(request):
    if request.method == "POST":
        form = ExpenseForm(request.POST)

        if form.is_valid():
            form.save()
            messages.success(request, "Expense #{} added.".format(
                form.instance.id
            ))
            return redirect(form.instance)
            # return redirect(reverse("expenses:list"))

    else:
        form = ExpenseForm()

    return render(request, "form.html", {
        'title': "Create New Expense",
        'form': form,
    })
