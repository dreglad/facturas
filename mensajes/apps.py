from django.apps import AppConfig

class MensajesAppConfig(AppConfig):
    name = 'mensajes'

    def ready(self):
        import mensajes.signals.handlers
    
