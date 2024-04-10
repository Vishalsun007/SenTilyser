from django.apps import AppConfig

from SenTilyser.processor import Processor, Model


class SentilyserConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'SenTilyser'


    def ready(self) -> None:
        

        self.processor = Processor()
        self.model = Model()
