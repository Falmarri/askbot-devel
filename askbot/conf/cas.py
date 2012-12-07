"""Settings for LDAP login for Askbot"""
from askbot.conf.settings_wrapper import settings
from askbot.conf.super_groups import EXTERNAL_SERVICES
from askbot.deps import livesettings
from django.utils.translation import ugettext as _

CAS_SETTINGS = livesettings.ConfigurationGroup(
    'CAS_SETTINGS',
    _('CAS login configuration'),
    super_group = EXTERNAL_SERVICES
)


settings.register(
    livesettings.BooleanValue(
        CAS_SETTINGS,
        'USE_CAS_FOR_PASSWORD_LOGIN',
        description=_('Use CAS authentication for the password login'),
        defaut=False
    )
)


settings.register(
    livesettings.StringValue(
        CAS_SETTINGS,
        'CAS_SERVER',
        description=_('CAS_SERVER URL'),
        default="https://path.to.cas_server"
    )
)


settings.register(
    livesettings.StringValue(
        CAS_SETTINGS,
        'SERVICE_URL',
        description=_('CAS_SERVICE URL'),
        default="/CAS_serviceValidater?sendback=/application/"
    )
)

settings.register(
    livesettings.StringValue(
        CAS_SETTINGS,
        'PROXY_URL',
        description=_('CAS Proxy URL'),
        default="/CAS_proxyUrl"
    )
)


settings.register(
    livesettings.StringValue(
        CAS_SETTINGS,
        'PROXY_CALLBACK_URL',
        description=_('CAS Proxy Callback URL'),
        default="/CAS_proxyCallback"
    )
)