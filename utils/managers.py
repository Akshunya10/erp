from django.db.models import QuerySet, Q, Sum

class CustomQuerySet(QuerySet):
    """
    Custom queryset that will be reused by different models.
    """

    def _active(self):
        """Return only objects that haven't been soft deleted."""
        return self.filter(is_deleted=False)

    def all_objects(self):
        """Return all objects that haven't been soft deleted"""
        return self._active()

    def all_approved(self):
        """ return client companies that are approved"""
        return self._active().filter(approval_status='approved')

class ChannelsQuery(CustomQuerySet):
    """Queryset that will be used by the property model"""

    def for_client_admin(self, client_admin):
        """This query set returns all Channel that
           belongs to a client, whether published or not"""
        return self._active().filter(client_admin=client_admin)

    def by_channel_name(self, name):
        """Return property with the passed slug"""
        return self._active().filter(name=name)

    def all_published(self):
        """Returns all property that is published"""
        return self._active().filter(is_published=True)

    def all_published_and_all_by_client_admin(self, client_admin):
        """
        Return all Channels that are published and also all
        property owned by the client
        """
        return self._active().filter(Q(is_published=True)) | self._active(
        ).filter(Q(client_admin=client_admin))

# class LiveTvCategoryQuery(CustomQuerySet):
#     """live tv category custom queries"""