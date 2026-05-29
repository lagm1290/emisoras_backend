from django.db import models


class Emisora(models.Model):
    titulo = models.CharField(max_length=200)
    cadena = models.CharField(max_length=100, db_index=True)
    ciudad = models.CharField(max_length=100, db_index=True)
    url = models.URLField()
    via = models.CharField(max_length=50, default='streamtheworld')
    codename = models.CharField(max_length=100, blank=True, default='')
    orden = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['orden', 'id']
        verbose_name = 'Emisora'
        verbose_name_plural = 'Emisoras'

    def __str__(self):
        return self.titulo
