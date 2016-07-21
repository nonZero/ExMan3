from django.contrib import admin

from . import models


class ExpenseAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'amount',
        'created_at',
        'id',
    )


admin.site.register(models.Expense, ExpenseAdmin)
