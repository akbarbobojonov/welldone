from django.db import models
from django.utils import timezone
from django.utils.translation import ugettext as _

from django.shortcuts import resolve_url

from django.contrib.auth.models import User

from django.conf import settings
from django.core.mail import send_mail, EmailMessage

from django.template.loader import render_to_string


class CProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='cprofile', verbose_name=_("User"))

    activation_key = models.CharField(max_length=255, blank=True, null=True, verbose_name=_("Activation key"))
    key_expires = models.DateTimeField(blank=True, null=True, verbose_name=_("Key expires"))
    email_verified = models.BooleanField(default=False, verbose_name=_("Email verified"))

    class Meta:
        verbose_name = _("Profile")
        verbose_name_plural = _("Profiles")

    def __str__(self):
        return self.user.first_name

    def confirm_activation_key(self):
        if timezone.now() > self.key_expires:
            return False

        self.email_verified = True
        self.user.is_active = True
        self.user.save()

        self.activation_key = None
        self.save()

        return True

    def send_email_verified(self, request):
        subject = _("Activate your Site account.")

        fullname = self.user.first_name

        html_message = render_to_string("site/registration/email/signup_email_verified.html", {
            'fullname': fullname,
            'confirm_url': request.build_absolute_uri(resolve_url('email_verified', self.activation_key)),
        })

        msg = EmailMessage(subject, html_message, settings.NOREAPLY_EMAIL, [self.user.email])
        msg.content_subtype = "html"
        msg.send()