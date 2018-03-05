import uuid
from django.db import models
from django.db.models import Max, QuerySet


class TODOItemQuerySet(QuerySet):
    def trim_rows(self):
        # TODO move to manager
        MAX = 1000000
        BUFFER = 5000
        total = self.count()
        if total > MAX:
            pk_pointer = self.order_by('pk')[:total-MAX+BUFFER].aggregate(Max('pk'))['pk__max']
            self.filter(pk__lt=pk_pointer).delete()


class TODOItem(models.Model):
    uuid = models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True)
    session_id = models.CharField(max_length=255, db_index=True, blank=True, editable=False)
    description = models.CharField(max_length=255)
    priority = models.IntegerField(default=10)
    created_at = models.DateTimeField(auto_now_add=True)
    completed_at = models.DateTimeField(null=True)
    objects = TODOItemQuerySet.as_manager()


    class Meta:
        ordering = ['priority', '-created_at']
