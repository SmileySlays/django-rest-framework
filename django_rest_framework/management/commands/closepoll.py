from django.core.management.base import BaseCommand, CommandError
from quickstart.models import ShoeColor, ShoeType

class Command(BaseCommand):
    help = 'Populate tables with data'

    def add_arguments(self, parser):
        parser.add_argument('--shoe_type', type=string, help="list of shoe types to add to populate")
        parser.add_argument('--shoe_color', type=string, help="list of shoe colors to add to populate")


    def handle(self, *args, **options):
        # shoe_types = ["sneaker". "boot", "sandal", "dress", "other"]
        # shoe_colors = ["red", "orange", "yellow", "green", "blue", "indigo", "violet", "white", "black"]
        if args = "shoe_type":
            for shoe in options['shoe_types']:
                try:
                    ShoeType.objects.create(
                        shoe
                    )
                except ShoeType.DoesNotExist:
                    raise CommandError('ShoeType model does not exist')

                self.stdout.write(self.style.SUCCESS('Successfully created ShoeType %s', shoe)
    
        if args = "shoe_color":
        for shoe in options['shoe_colors']:
            try:
                ShoeColor.objects.create(
                    shoe
                )
            except ShoeColor.DoesNotExist:
                raise CommandError('ShoeColor model does not exist')

            self.stdout.write(self.style.SUCCESS('Successfully created ShoeColor %s', shoe)