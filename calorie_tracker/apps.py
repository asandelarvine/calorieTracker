from django.apps import AppConfig


class CalorieTrackerConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'calorie_tracker'
    def ready(self): #new
        import calorie_tracker.signals #new
