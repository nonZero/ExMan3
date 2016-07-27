import decimal

from django.db import models


class Expense(models.Model):
    # id is automatic
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

    def amount_with_tax(self):
        return self.amount * decimal.Decimal("1.17")