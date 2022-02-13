from django.core.management import BaseCommand
from django.contrib.sites.models import Site


class Command(BaseCommand):
    help = "Changes the default site name"

    def add_arguments(self, parser):
        parser.add_argument("site-domain")

    def handle(self, *args, **options):
        domain = options["site-domain"]
        name = "sample"

        try:
            site = Site.objects.get(domain="example.com")
            site.name = name
            site.domain = domain
            site.save()

        except Site.DoesNotExist:
            # No site with domain example.com exists.
            # Create a default site, but only if no sites exist.
            if Site.objects.count() == 0:
                Site.objects.create(name=name, domain=domain)
