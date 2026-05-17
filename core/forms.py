from django.utils.translation import gettext_lazy as _
from unfold.forms import AuthenticationForm

class CustomAdminAuthenticationForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].label = _("Email or Username")
