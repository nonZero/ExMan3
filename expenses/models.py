import decimal

from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from django.db import models


class Tag(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name


class Expense(models.Model):
    user = models.ForeignKey(User, related_name='expenses')
    created_at = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=300)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField(null=True, blank=True)

    tags = models.ManyToManyField(Tag, blank=True,
                                  related_name='expenses',
                                  # through='ExpenseTag',
                                  )

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


# class ExpenseTag(models.Model):
#     created_at = models.DateTimeField(auto_now_add=True)
#     expense = models.ForeignKey(Expense)
#     tag = models.ForeignKey(Tag)
#
#     class Meta:
#         unique_together = (
#             ('expense', 'tag'),
#         )
