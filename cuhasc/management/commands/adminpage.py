"""Management command ``adminpage``: (re)set the admin-page token and print its full link.
The Culture Lead uses that page to recover Team and Member links if the cookie is lost.

Normally reached as ``cuhasc adminpage``, which passes the base URL of the running server;
in a source checkout, ``python manage.py adminpage`` does the same for a local dev server.
"""
import os

from django.core.management.base import BaseCommand
from django.urls import reverse

import cuhasc.base as base
import cuhasc.deployment as deployment
from cuhasc.models import AdminPage

DEFAULT_BASE_URL = 'http://localhost:8037'  # where `cuhasc run` listens unless told otherwise


class Command(BaseCommand):
    help = "(Re)set the admin-page token and print its full link."

    def add_arguments(self, parser):
        parser.add_argument('--base-url', default=None,
                            help="URL under which this server is reached (default: "
                                 f"${deployment.PUBLIC_URL_ENV} if set, else {DEFAULT_BASE_URL})")

    def handle(self, *args, **options):
        base_url = (options['base_url'] or os.environ.get(deployment.PUBLIC_URL_ENV)
                    or DEFAULT_BASE_URL)
        adminpage = AdminPage.reset()
        self.stdout.write(base.join_url(base_url, reverse('adminpage', args=[adminpage.token])))
