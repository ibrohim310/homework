from django.db import models

class Features(models.Model):
    title = models.CharField(max_length = 255)
    body = models.TextField()
    icon = models.ImageField()
class Services(models.Model):
    title = models.CharField(max_length = 255)
    body = models.TextField()
    icon = models.ImageField()
class Projects(models.Model):
    title = models.CharField(max_length = 255)
    body = models.TextField()
    icon = models.ImageField()

class Quote(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    phone = models.CharField(max_length=13)
    message = models.TextField(null=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f"murojat {self.first_name}dan"
    
#    class Meta:
#        verbose_name = "Murojatlar royhati"
#        verbose_name_PLURAL = "Murojatlar"
#        ordering = ("is_active",)