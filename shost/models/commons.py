from django.utils.translation import ugettext_lazy as _
from django.db import models as ext


class Currency(ext.Model):
    id = ext.IntegerField(_("id"), primary_key=True)
    iso_code = ext.CharField(_("iso code"), max_length=10, null=True, blank=True)
    iso_name = ext.CharField(_("iso name"), max_length=10, null=True, blank=True)
    decimal_digits = ext.IntegerField(_("decimal digits"), null=True, blank=True)

    class Meta:
        verbose_name = _('currency')
        verbose_name_plural = _('currencies')

    def __str__(self):
        return "%d : %s" % (self.id, self.iso_name)


class Country(ext.Model):
    iso_code = ext.CharField(_("iso code"), max_length=10, null=True, blank=True)
    name = ext.CharField(_("name"), max_length=255, null=True, blank=True)

    class Meta:
        verbose_name = _('country')
        verbose_name_plural = _('countries')

    def __str__(self):
        return "%d : %s" % (self.id, self.name)
