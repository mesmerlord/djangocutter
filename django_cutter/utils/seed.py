from .factories import SetFactory, WorkoutFactory, ExerciseFactory

def seed():
    sets = []
    workouts = []
    exercises = []
    for _ in range(10000):
        set_instance = SetFactory()
        sets.append(set_instance)
        workout_instance = WorkoutFactory()
        workouts.append(workout_instance)
        exercise_instance = ExerciseFactory()
        exercises.append(exercise_instance)
    Set.objects.bulk_create(sets, batch_size = 200)
    Workout.objects.bulk_create(workouts, batch_size = 200)
    Exercise.objects.bulk_create(exercises, batch_size = 200)
