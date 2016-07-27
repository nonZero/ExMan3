from django import forms
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.mail import mail_admins
from django.core.urlresolvers import reverse
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


@login_required
def expense_list(request):
    # qs = models.Expense.objects.filter(user=request.user).order_by('-created_at')
    qs = request.user.expenses.order_by('-created_at')

    # TODO: fix name to meet convention
    return render(request, "expense_list.html", {
        'object_list': qs,
    })


@login_required
def expense_detail(request, id):
    o = get_object_or_404(models.Expense, id=id, user=request.user)
    # o = get_object_or_404(request.user.expenses, id=id)

    # TODO: fix name to meet convention
    return render(request, "expense_detail.html", {
        'object': o,
    })


class ExpenseForm(forms.ModelForm):
    class Meta:
        model = models.Expense
        fields = (
            'amount',
            'title',
            'description',
        )


@login_required
def expense_create_view(request):
    if request.method == "POST":
        form = ExpenseForm(request.POST)

        if form.is_valid():
            form.instance.user = request.user
            form.save()
            messages.success(request, "Expense #{} added.".format(
                form.instance.id
            ))
            return redirect(form.instance)
    else:
        form = ExpenseForm()

    return render(request, "form.html", {
        'title': "Create New Expense",
        'form': form,
    })
