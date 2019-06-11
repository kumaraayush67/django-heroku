from django.db import models

class Todo(models.Model):
    title= models.CharField(max_length=10)
    is_done= models.BooleanField(default=False)
    des = models.CharField(max_length=100)

    def __str__(self):
        if self.is_done:
            return self.title + "(completed)"
        else:
            return self.title

    def save(self, *args, **kwargs):
        super(Todo, self).save(*args, **kwargs)
        return self