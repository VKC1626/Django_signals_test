from django.apps import AppConfig


class AsyncTestConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "async_test"

    def ready(self):
        import async_test.signals
