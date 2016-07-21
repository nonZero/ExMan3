import random

from django.http.response import HttpResponseNotFound
from django.shortcuts import render, get_object_or_404

from . import models


# list: modelname_list
# single: modelname_detail

def expense_list(request):
    qs = models.Expense.objects.order_by('-created_at')

    # TODO: fix name to meet convention
    return render(request, "expense_list.html", {
        'object_list': qs,
    })


def expense_detail(request, id):
    o = get_object_or_404(models.Expense, id=id)
    # try:
    #     o = models.Expense.objects.get(id=id)
    # except models.Expense.DoesNotExist:
    #     return HttpResponseNotFound("go away")

    # TODO: fix name to meet convention
    return render(request, "expense_detail.html", {
        'object': o,
    })
