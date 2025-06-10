from django.apps import AppConfig


class StylesConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'apps.styles'

    def ready(self):
        from django.core.management import call_command
        try:
            call_command('register_styles')
        except Exception:
            # Ignore failures during startup
            pass
