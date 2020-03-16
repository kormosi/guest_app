from django.core.management.base import BaseCommand, CommandError
from export.models import Guest
from export.management.commands.image import image
import random, string

class Command(BaseCommand):

    help = "Generate N dummy guests and add them to database."

    def add_arguments(self, parser):
        parser.add_argument(
                'amount', type=int,
                 help="Indicates the number of Guests to be created."
                 )


    def handle(self, *args, **kwargs):
        amount = kwargs['amount']

        # Generate a random word to be used as first and last names.
        def randomword(length):
           letters = string.ascii_lowercase
           return ''.join(random.choice(letters) for i in range(length))

        # Create n Guest instances in bulk.
        Guest.objects.bulk_create([
            Guest(first_name=f"{randomword(7)}",
                  last_name=f"{randomword(10)}",
                  base64_image=image) for i in range(amount)
                  ])
