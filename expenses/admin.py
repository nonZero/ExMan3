from django.contrib import admin

from . import models


class ExpenseAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'amount',
        'created_at',
        'id',
    )
    date_hierarchy = 'created_at'
    search_fields = (
        'title',
        'amount',
        'id',
        'description',
    )


admin.site.register(models.Expense, ExpenseAdmin)
