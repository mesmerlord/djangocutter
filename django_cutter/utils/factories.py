import factory

class SetFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = 'Set'

    name = factory.Faker('word')
    reps = factory.Faker('random_int')
    weight = factory.Faker('random_int')
    date = factory.Faker('date_this_decade')
    workout = factory.SubFactory('utils.WorkoutFactory')

class WorkoutFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = 'Workout'

    name = factory.Faker('word')
    date = factory.Faker('date_this_decade')

class ExerciseFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = 'Exercise'

    name = factory.Faker('word')
    sets = factory.SubFactory(SetFactory, workout=factory.SelfAttribute('..workout'))
    person = factory.SubFactory('users.UserFactory')
