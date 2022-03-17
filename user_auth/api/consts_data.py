from django.contrib.auth import get_user_model

consts_data = {
     'name_singular': get_user_model()._meta.verbose_name.capitalize()
     }
