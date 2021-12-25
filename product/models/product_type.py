from django.db.models import CharField, DateTimeField, Model
from django.utils.translation import gettext_lazy as _


class ProductType(Model):
    name = CharField(_('name'), max_length=255)
    created_at = DateTimeField(_('created_at'), auto_now_add=True)
    updated_at = DateTimeField(_('updated_at'), auto_now=True)

    class Meta:
        ordering = ['name']
        verbose_name = _('type')
        verbose_name_plural = _('types')

    def __str__(self):
        return self.name
