from .factories import SetFactory, WorkoutFactory, ExerciseFactory

def seed():
    for _ in range(100):
        workout_instance = WorkoutFactory.create_batch(size=200)
        set_instance = SetFactory.create_batch(size=10)
        exercise_instance = ExerciseFactory.create_batch(size=100)
        for exc in exercise_instance:
            exc.sets.set(set_instance)
            exc.save()

    
