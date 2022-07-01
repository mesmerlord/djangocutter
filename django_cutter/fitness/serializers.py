from rest_framework import serializers


from .models import Set, Exercise, Workout


class SetSerializer(serializers.ModelSerializer):

    class Meta:
        model = Set
        fields = "__all__"

class ExerciseSerializer(serializers.ModelSerializer):

    class Meta:
        model = Exercise
        fields = "__all__"

class WorkoutSerializer(serializers.ModelSerializer):

    class Meta:
        model = Workout
        fields = "__all__"