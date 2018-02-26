from django.db import models
from django.db.models import Max, QuerySet


class TODOItemQuerySet(QuerySet):
    def trim_rows(self):
        # TODO move to manager
        MAX = 1000000
        BUFFER = 5000
        total = self.objects.count()
        if total > MAX:
            pk_pointer = self.order_by('pk')[:total-MAX+BUFFER].aggregate(Max('pk'))['pk__max']
            self.filter(pk__lt=pk_pointer).delete()


class TODOItem(models.Model):
    session_id = models.CharField(max_length=255, db_index=True, blank=True)
    description = models.CharField(max_length=255)
    priority = models.IntegerField(default=10)
    created_at = models.DateTimeField(auto_now_add=True)
    completed_date = models.DateTimeField(null=True)
    objects = TODOItemQuerySet.as_manager()


    class Meta:
        ordering = ['-completed_date', 'priority', '-created_at']
