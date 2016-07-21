import random
from django.shortcuts import render

from . import models


# list: modelname_list
# single: modelname_detail

def expense_list(request):
    qs = models.Expense.objects.order_by('-created_at')

    # TODO: fix name to meet convention
    return render(request, "expense_list.html", {
        'object_list': qs,
    })
