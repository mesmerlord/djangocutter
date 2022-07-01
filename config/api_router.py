from django.conf import settings
from django_cutter.fitness.views import ExcerciseViewSet, SetViewSet, WorkoutViewSet
from rest_framework.routers import DefaultRouter, SimpleRouter

from django_cutter.users.api.views import UserViewSet

if settings.DEBUG:
    router = DefaultRouter()
else:
    router = SimpleRouter()

router.register("users", UserViewSet)
router.register("sets", SetViewSet)
router.register("excercises", ExcerciseViewSet)
router.register("workouts", WorkoutViewSet)


app_name = "api"
urlpatterns = router.urls
