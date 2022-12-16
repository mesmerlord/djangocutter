import factory
from django_cutter.fitness.models import Set, Workout, Exercise
from django_cutter.users.tests.factories import UserFactory
class SetFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = 'Set'

    name = factory.Faker('word')
    reps = factory.Faker('random_int')
    weight = factory.Faker('random_int')
    date = factory.Faker('date_this_decade')
    workout = factory.Iterator(Workout.objects.all())

class WorkoutFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = 'Workout'

    name = factory.Faker('word')
    date = factory.Faker('date_this_decade')

class ExerciseFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = 'Exercise'

    name = factory.Faker('word')
    person = factory.SubFactory(UserFactory)
