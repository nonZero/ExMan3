import decimal

from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from django.db import models


class Expense(models.Model):
    user = models.ForeignKey(User, related_name='expenses')
    created_at = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=300)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return "[#{}] {} (${})".format(
            self.id,
            self.title,
            self.amount,
        )

    def get_absolute_url(self):
        return reverse("expenses:detail", args=(self.pk,))

    def amount_with_tax(self):
        return self.amount * decimal.Decimal("1.17")
