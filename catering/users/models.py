from django.db import models

class User(models.Model):
    username = models.CharField(max_length=100, blank=True, null=False)
    password = models.CharField(max_length=100, blank=False, null=False)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "{}".format(self.username)

    class Meta:
        ordering = ['-date']
        verbose_name_plural = "User"
