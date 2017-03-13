from django.utils.translation import ugettext_lazy as _

from shost.models.core import *
from shost.models.commons import *


class Host(ext.Model):
    owner = ext.ForeignKey(User, null=True, blank=True)
    description = ext.CharField(_("description"), max_length=255, null=True, blank=True)
    country = ext.ForeignKey(Country, null=True, blank=True)
    address = ext.CharField(_("address"), max_length=255, null=True, blank=True)
    latitude = ext.CharField(_("latitude"), max_length=255, null=True, blank=True)
    longitude = ext.CharField(_("longitude"), max_length=255, null=True, blank=True)

    class Meta:
        verbose_name = _('host')
        verbose_name_plural = _('hosts')
        default_related_name = 'hosts'


class UserStay(ext.Model):
    user = ext.ForeignKey(User, null=True, blank=True)
    host = ext.ForeignKey(Host, null=True, blank=True)
    started_at = ext.DateTimeField(_("started at"), null=True, blank=True)
    finished_at = ext.DateTimeField(_("started at"), null=True, blank=True)
    comments = ext.CharField(_("comments"), null=True, blank=True)

    class Meta:
        verbose_name = _('user stay')
        verbose_name_plural = _('user stays')
        default_related_name = 'user_stays'
