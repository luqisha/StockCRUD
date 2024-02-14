from django.apps import AppConfig
from django.db.models.signals import post_migrate
from django.apps import apps


class ViewStockDataConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'ViewStockData'

    def ready(self):
        from .management.commands.load_data import Command as LoadStockDataCommand

        # Define a signal handler to execute the management command after migrations
        def load_data_handler(sender, **kwargs):
            if sender.name == 'ViewStockData':
                LoadStockDataCommand().handle()

        # Connect the signal handler to the post_migrate signal
        post_migrate.connect(load_data_handler, sender=apps.get_app_config('ViewStockData'))
