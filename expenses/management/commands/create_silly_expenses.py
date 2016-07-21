import decimal

from django.core.management.base import BaseCommand, CommandError

from expenses.models import Expense
import silly


class Command(BaseCommand):
    help = 'Creates silly expenses'

    def handle(self, *args, **options):
        n = 10
        for i in range(n):
            o = Expense(
                created_at=silly.datetime(),
                title="{} {}".format(silly.adjective(), silly.noun()),
                amount=str(silly.number() + silly.number() / 10)[:5],
                description=silly.sentence() + "\n" + silly.sentence()
            )
            o.full_clean()
            o.save()
            o.created_at = silly.datetime()
            o.save()
