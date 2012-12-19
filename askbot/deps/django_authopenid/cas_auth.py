from django.contrib.auth.models import User
from askbot.deps.django_authopenid.models import UserAssociation
from askbot.models.signals import user_registered
import logging
 
LOG = logging.getLogger(__name__)

def cas_get_or_create_user(cas_response):
    """takes the result returned by the :func:`ldap_authenticate`
    
    and returns a :class:`UserAssociation` object
    """
    # create new user in local db
    try:
        logging.debug("Getting user association for %s", cas_response.get('user'))
        assoc = UserAssociation.objects.get(
            openid_url = cas_response.get('user') + '@ldap',
            provider_name = 'ldap'
        )
        return assoc
    except UserAssociation.DoesNotExist:

        try:
            user = User.objects.get(username=cas_response.get('user'))
        except User.DoesNotExist:

            user = User()
        user.username = cas_response.get('django_username', cas_response.get('user'))
        user.set_unusable_password()

        user.first_name = cas_response['attributes'].get('firstName', None)

        user.last_name = cas_response['attributes'].get('lastName', None)

        user.email = cas_response['attributes'].get('email', None)
        user.is_staff = False
        user.is_superuser = False
        user.is_active = True
        user.save()
        user_registered.send(None, user = user)
        logging.debug('Created New User : [{0}]'.format(cas_response.get('user')))

        assoc = UserAssociation()
        assoc.user = user
        assoc.openid_url = cas_response.get('user') + '@ldap'
        assoc.provider_name = 'ldap'
        assoc.save()
        return assoc