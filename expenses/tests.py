from django.core.urlresolvers import reverse
from django.test import TestCase

from . import models


class ExpensesTestCase(TestCase):
    def test_expense_model(self):
        n = 10
        for i in range(n):
            o = models.Expense(
                title="My Expense #{}".format(i + 1),
                amount=10 * i,
                description="\n".join(["foo"] * (i + 1))
            )
            o.full_clean()
            o.save()
        self.assertEqual(models.Expense.objects.count(), n)

    def test_expense_list_view(self):
        n = 10
        for i in range(n):
            o = models.Expense(
                title="My Expense #{}".format(i + 1),
                amount=10 * i,
                description="\n".join(["foo"] * (i + 1))
            )
            o.full_clean()
            o.save()

        resp = self.client.get(reverse("expenses:list"))
        self.assertContains(resp, "Expense #1")




        # self.assertEqual(models.Expense.objects.count(), n)
