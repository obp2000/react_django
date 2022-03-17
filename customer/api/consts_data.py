from ..models import Customer

consts_data = {
     'name_singular': Customer._meta.verbose_name.capitalize(),
     'name_plural': Customer._meta.verbose_name_plural.capitalize()
     }
