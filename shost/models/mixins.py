from django.db import models as ext
from django.utils.translation import gettext_lazy as _

from shost.utils import get_now, setallattr


class NoAutoIdWithDescriptionMixin(ext.Model):
    id = ext.IntegerField(_("id"), primary_key=True)
    description = ext.CharField(_("description"), max_length=255, null=True, blank=True)

    class Meta:
        abstract = True

    def __str__(self):
        return "%d : %s" % (self.id, self.description)


class ActiveMixin(ext.Model):
    active = ext.BooleanField(_("active"), default=True)
    deactivated_at = ext.DateTimeField(_("deactivated at"), null=True, blank=True)
    activated_at = ext.DateTimeField(_("activated at"), null=True, blank=True)
    fixed = ext.BooleanField(_("fixed"), default=False,
                         help_text=_("If true, This field will not affected on bulk activation/deactivation processes"))

    class Meta:
        abstract = True

    def activate(self):
        activate(self)

    def deactivate(self):
        deactivate(self)


class LastUpdateMixin(ext.Model):
    updated_at = ext.DateTimeField(_("updated at"), null=True, blank=True)

    class Meta:
        abstract = True

    def save(self, *args, **kwargs):
        self.updated_at = get_now()
        return super(LastUpdateMixin, self).save(*args, **kwargs)


def deactivate_all(queryset, deactivated_at=None):
    if not deactivated_at:
        deactivated_at = get_now()
    queryset.filter(fixed=False, active=True).update(active=False, deactivated_at=deactivated_at)


def deactivate(obj, deactivated_at=None):
    if not obj.active or obj.fixed:
        return
    if not deactivated_at:
        deactivated_at = get_now()
    setallattr(obj, active=False, deactivated_at=deactivated_at)
    obj.save()


def activate_all(queryset, activated_at=None):
    if not activated_at:
        activated_at = get_now()
    queryset.filter(fixed=False, active=False).update(active=True, activated_at=activated_at)


def activate(obj, activated_at=None):
    if obj.active or obj.fixed:
        return
    if not activated_at:
        activated_at = get_now()
    setallattr(obj, active=True, activated_at=activated_at)
    obj.save()
