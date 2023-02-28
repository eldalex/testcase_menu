from django.db import models

class Menu(models.Model):
    name = models.CharField(max_length=50)
    parent = models.ForeignKey('self', blank=True, null=True, related_name='children', on_delete=models.CASCADE)
    url = models.CharField(max_length=200)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name  = 'Пункт меню'
        verbose_name_plural  = 'Пункты меню'