from rest_framework import serializers


from .models import Set, Exercise, Workout

class WorkoutSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Workout
        fields = "__all__"

class SetSerializer(serializers.ModelSerializer):
    workout = WorkoutSerializer()

    class Meta:
        model = Set
        fields = "__all__"

class ExerciseSerializer(serializers.ModelSerializer):
    sets = SetSerializer(many=True)
    class Meta:
        model = Exercise
        fields = "__all__"

