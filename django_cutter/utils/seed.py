from .factories import SetFactory, WorkoutFactory, ExerciseFactory

def seed():
    for _ in range(100):
        workout_instance = WorkoutFactory.create_batch(size=100)
        set_instance = SetFactory.create_batch(size=100)
        exercise_instance = ExerciseFactory.create_batch(size=100)
    
