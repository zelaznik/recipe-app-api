# django command to wait for the database to be available
from django.core.management.base import BaseCommand
from psycopg2 import OperationalError as Psycopg2Error
from django.db.utils import OperationalError
import time


class Command(BaseCommand):
    """Django command to wait for database."""

    def handle(self, *args, **options):
        """Entrypoint for command."""

        self.stdout.write('Waiting for database...')

        while True:
            try:
                self.check(databases=['default'])
                break
            except (Psycopg2Error, OperationalError):
                pass

            self.stdout.write('Database unavailable, waiting 1 second')
            time.sleep(1)

        self.stdout.write(self.style.SUCCESS('Database available'))
