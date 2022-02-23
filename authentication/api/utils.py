# overriding the default payload handler

import datetime
from django.conf import settings
from django.utils import timezone

expiration_delta = settings.JWT_AUTH['JWT_REFRESH_EXPIRATION_DELTA']


def jwt_response_payload_handler(token, user=None, request=None):
    return {
        'token': token,
        'user': user.username,
        'expires': timezone.now() + expiration_delta - datetime.timedelta(seconds=3600)
    }



