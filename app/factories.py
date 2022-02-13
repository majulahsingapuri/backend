import factory

from users.models import User


def add_many2many(obj, create, extracted, field):
    if not create:
        return

    if extracted:
        for relation in extracted:
            getattr(obj, field).add(relation)
