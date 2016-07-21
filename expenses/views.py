import random
from django.shortcuts import render

from . import models


# list: modelname_list
# single: modelname_detail

def expense_list(request):
    # qs = models.Expense.objects.all()
    qs = models.Expense.objects.order_by('-amount')[:10]
    # s = "<br/>".join([o.title for o in qs])
    # return HttpResponse(s)

    desc = """Lorem ipsum dolor sit amet,
consectetur adipisicing elit.
Accusantium dolorem doloremque
fugiat provident recusandae sunt!"""

    # TODO: fix name to meet convention
    return render(request, "expense_list.html", {
        'object_list': qs,
        'foo': 123,
        'bar': "kukukukukukuk<b>ukukuku</b>kukkukukukku",
        'x': random.randint(1, 10),
        'desc': desc,
        'colors': ['red', 'green', 'blue'],
    })
