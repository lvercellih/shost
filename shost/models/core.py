from django.contrib.auth.models import AbstractUser
from django.db import models as ext
from django.utils.translation import ugettext_lazy as _

from shost.models import mixins


class EClass(mixins.NoAutoIdWithDescriptionMixin):
    class Meta:
        verbose_name = _('entity class')
        verbose_name_plural = _('entity classes')


class Status(mixins.NoAutoIdWithDescriptionMixin):
    class Meta:
        verbose_name = _('entity status')
        verbose_name_plural = _('entity status')


class Operation(mixins.NoAutoIdWithDescriptionMixin):
    class Meta:
        verbose_name = _('operation')
        verbose_name_plural = _('operations')


class Entity(ext.Model):
    id = ext.BigAutoField(_("id"), primary_key=True)
    eclass = ext.ForeignKey(EClass, related_name='entities', null=True, blank=True)
    status = ext.ForeignKey(Status, related_name='entities', null=True, blank=True)
    created_at = ext.DateTimeField(_("created at"), null=True, blank=True)
    creation_process = ext.ForeignKey("Process", related_name='entity_creations', null=True, blank=True)
    first_history = ext.ForeignKey("History", related_name='+', null=True, blank=True)
    last_history = ext.ForeignKey("History", related_name='+', null=True, blank=True)

    class Meta:
        verbose_name = _('entity')
        verbose_name_plural = _('entities')


class History(ext.Model):
    id = ext.BigAutoField(_("id"), primary_key=True)
    entity = ext.ForeignKey(Entity, null=True, blank=True)
    status = ext.ForeignKey(Status, related_name='+', null=True, blank=True)
    issued_at = ext.DateTimeField(_("issued at"), null=True, blank=True)
    process = ext.ForeignKey("Process", null=True, blank=True)

    class Meta:
        verbose_name = _('history')
        verbose_name_plural = _('history')
        default_related_name = 'history'


class Process(ext.Model):
    id = ext.BigAutoField(_("id"), primary_key=True)
    operation = ext.ForeignKey(Operation, related_name='processes', null=True, blank=True)
    issued_by = ext.ForeignKey("User", related_name='processes', null=True, blank=True)
    started_at = ext.DateTimeField(_("started at"), null=True, blank=True)
    finished_at = ext.DateTimeField(_("finished at"), null=True, blank=True)

    class Meta:
        verbose_name = _('process')
        verbose_name_plural = _('processes')

    def __str__(self):
        return "[%d] [%s] [%s - %s]" % (self.id, str(self.operation), str(self.started_at), str(self.finished_at))


class Request(Process):
    tracking_id = ext.CharField(_("tracking id"), max_length=255, null=True, blank=True, db_index=True)
    request_ip = ext.CharField(_("request ip"), max_length=255, null=True, blank=True)
    request_method = ext.CharField(_("request method"), max_length=10, null=True, blank=True, db_index=True)
    request_url = ext.CharField(_("request url"), max_length=2000, null=True, blank=True)
    request_headers = ext.CharField(_("request headers"), max_length=8000, null=True, blank=True)
    request_query = ext.CharField(_("request query"), max_length=2000, null=True, blank=True)
    request_body = ext.CharField(_("request url"), max_length=8000, null=True, blank=True)
    response_code = ext.IntegerField(_("response code"), null=True, blank=True)
    response_body = ext.CharField(_("response code"), max_length=8000, null=True, blank=True)

    class Meta:
        verbose_name = _('request')
        verbose_name_plural = _('requests')

    def __str__(self):
        return "[%d] %s %s" % (self.id, self.request_method, self.request_url)


class Metadata(ext.Model):
    entity = ext.ForeignKey(Entity, related_name='metadata', null=True, blank=True)
    key_name = ext.CharField(_("key name"), max_length=255, null=True, blank=True)
    value = ext.CharField(_("value"), max_length=8000, null=True, blank=True)

    class Meta:
        verbose_name = _('metadata')
        verbose_name_plural = _('metadata')

    def __str__(self):
        return "[%s] %s -> %s" % (self.entity, self.key_name, self.value)


####################
## Authentication ##
####################


class User(AbstractUser):
    class Meta(AbstractUser.Meta):
        swappable = 'AUTH_USER_MODEL'


class AuthType(mixins.NoAutoIdWithDescriptionMixin):
    class Meta:
        verbose_name = _('auth type')
        verbose_name_plural = _('auth types')


class AuthKey(mixins.ActiveMixin):
    user = ext.ForeignKey(User, null=True, blank=True)
    auth_type = ext.ForeignKey(AuthType, null=True, blank=True)
    creation_request = ext.ForeignKey(Request, related_name='+', null=True, blank=True)

    class Meta:
        verbose_name = _('auth key')
        verbose_name_plural = _('auth keys')
        default_related_name = 'auth_keys'


class AuthRsaPublicKey(AuthKey):
    alias = ext.CharField(_("alias"), max_length=255, null=True, blank=True)
    key = ext.CharField(_("key"), max_length=255, null=True, blank=True)
    fingerprint = ext.CharField(_("fingerprint"), max_length=255, null=True, blank=True)

    class Meta:
        verbose_name = _('request')
        verbose_name_plural = _('requests')
        default_related_name = 'auth_tokens'


class AuthToken(ext.Model):
    key = ext.CharField(_("key"), max_length=255, db_index=True)

    class Meta:
        verbose_name = _('auth token')
        verbose_name_plural = _('auth tokens')
        default_related_name = 'auth_tokens'
