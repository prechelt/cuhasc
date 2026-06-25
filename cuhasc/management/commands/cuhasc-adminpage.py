"""Management command ``cuhasc-adminpage``: (re)set the admin-page token and print
its full link. The Culture Lead uses that page to recover Team and Member links if
the cookie is lost. Run by the deployer:

    python manage.py cuhasc-adminpage
"""
from django.core.management.base import BaseCommand
from django.urls import reverse

import cuhasc.base as base
import cuhasc.constants as c
from cuhasc.models import AdminPage

# The dev server's default; the deployer adjusts the host/port in the printed link as needed.
DEFAULT_BASE_URL = 'http://localhost:8000'


class Command(BaseCommand):
    help = "(Re)set the admin-page token and print its full link."

    def handle(self, *args, **options):
        token = base.random_token(c.TOKEN_LENGTH_ADMINPAGE)
        adminpage = AdminPage.objects.first()
        if adminpage is None:
            AdminPage.objects.create(token=token)
        else:
            adminpage.token = token
            adminpage.save()
        url = reverse('adminpage', args=[token])
        self.stdout.write(f"{DEFAULT_BASE_URL}{url}")
