import os


def set_django_settings():
    if os.environ.get("LOCAL", "False") == "True":
        os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'drfbackend.settings.local_settings')
    elif os.environ.get("PRODUCTION", "False") == "True":
        os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'drfbackend.settings.production_settings')
    else:
        print("Settings Not Found")
    return
