from django.apps import AppConfig # type: ignore


class CreamsquizzConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'creamsQuizz'
    
    def ready(self) -> None:
        import users.signals
