from django.core.management.base import BaseCommand, CommandError
from cats.models import Catfact
import getmodule


class Command(BaseCommand):
    help = 'Gets cat facts from the https://cat-fact.herokuapp.com API and stores them in the database'

    def handle(self, *args, **options):
        # Returns a list of facts with id and text fields
        facts = getmodule.getfacts()

        for fact in facts:
            cf = Catfact(api_id=fact.get('_id'), text=fact.get('text'))
            cf.save()
        self.stdout.write('Downloaded catfacts to DB')

        """
        for poll_id in options['poll_id']:
            try:
                poll = Poll.objects.get(pk=poll_id)
            except Poll.DoesNotExist:
                raise CommandError('Poll "%s" does not exist' % poll_id)

            poll.opened = False
            poll.save()

            self.stdout.write(self.style.SUCCESS('Successfully closed poll "%s"' % poll_id))"""
