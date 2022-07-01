from django.contrib import admin

from .models import Workout, Exercise, Set


class WorkoutAdmin(admin.ModelAdmin):
    list_display = [f.name for f in Workout._meta.fields]

class ExerciseAdmin(admin.ModelAdmin):
    list_display = [f.name for f in Exercise._meta.fields]

class SetAdmin(admin.ModelAdmin):
    list_display = [f.name for f in Set._meta.fields]


admin.site.register(Workout, WorkoutAdmin)
admin.site.register(Exercise, ExerciseAdmin)
admin.site.register(Set, SetAdmin)