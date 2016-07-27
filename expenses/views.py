import random

from django import forms
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.mail import mail_admins
from django.core.urlresolvers import reverse, reverse_lazy
from django.shortcuts import render, redirect
from django.utils.decorators import method_decorator
from django.utils.translation import gettext
from django.views.generic import CreateView, DeleteView, DetailView, ListView, \
    TemplateView, UpdateView

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


class RequireLoginMixin:
    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)


class ExpenseViewMixin(RequireLoginMixin):
    model = models.Expense
    fields = (
        'amount',
        'title',
        'tags',
        'description',
    )

    def get_queryset(self):
        return super().get_queryset().filter(user=self.request.user)


class ExpenseListView(ExpenseViewMixin, ListView):
    ordering = "-created_at"
    paginate_by = 10


# assert False, ExpenseListView.mro()

# @login_required
# def expense_list(request):
#     # qs = models.Expense.objects.filter(user=request.user).order_by('-created_at')
#     qs = request.user.expenses.order_by('-created_at')
#
#     # TODO: fix name to meet convention
#     return render(request, "expense_list.html", {
#         'object_list': qs,
#     })

class ExpenseDetailView(ExpenseViewMixin, DetailView):
    pass


# @login_required
# def expense_detail(request, id):
#     o = get_object_or_404(models.Expense, id=id, user=request.user)
#     # o = get_object_or_404(request.user.expenses, id=id)
#
#     # TODO: fix name to meet convention
#     return render(request, "expense_detail.html", {
#         'object': o,
#     })
#


class ExpenseCreateView(ExpenseViewMixin, CreateView):
    def form_valid(self, form):
        form.instance.user = self.request.user
        resp = super().form_valid(form)
        messages.success(self.request, gettext("Expense #{} added.").format(
            form.instance.id
        ))
        return resp


class ExpenseUpdateView(ExpenseViewMixin, UpdateView):
    def form_valid(self, form):
        resp = super().form_valid(form)
        messages.success(self.request, "Expense #{} updated.".format(
            form.instance.id
        ))
        return resp


class ExpenseDeleteView(ExpenseViewMixin, DeleteView):
    success_url = reverse_lazy("expenses:list")

    def delete(self, request, *args, **kwargs):
        id = self.get_object().id
        resp = super().delete(request, *args, **kwargs)
        messages.success(self.request, gettext("Expense #{} deleted.").format(
            id
        ))
        return resp


# class MyView(View):
#     def get(self, request, x):
#         return render(request, "my.html")
#     def post(self, request, x):
#         return render(request, "my.html")

class MyView(TemplateView):
    template_name = "my.html"

    bar = 456

    def baz(self):
        return random.randint(1, 10)

        # def get_context_data(self, **kwargs):
        #     d = super().get_context_data(**kwargs)
        #     d['foo'] = 123
        #     d['faz'] = random.randint(1, 10)
        #     return d




        # def get(self, request, x):
        #     return render(request, "my.html", )

        # def post(self, request):
        #     return HttpResponse("xxx")
