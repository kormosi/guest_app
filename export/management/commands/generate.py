from django.core.management.base import BaseCommand, CommandError
from export.models import Guest
import random, string
from export.management.commands.image import image

class Command(BaseCommand):

    help = "Generate N dummy guests and add them to database."

    def add_arguments(self, parser):
        parser.add_argument('amount', type=int, help="Indicates the number of Guests to be created.")


    def handle(self, *args, **kwargs):

        amount = kwargs['amount']

        def randomword(length):
           letters = string.ascii_lowercase
           return ''.join(random.choice(letters) for i in range(length))

        self.stdout.write("This can take up to several minutes.")

        for i in range(amount):
          self.stdout.write(i)
          guest = Guest(first_name=f"{randomword(7)}", last_name=f"{randomword(10)}", base64_image=image)
          guest.save()
