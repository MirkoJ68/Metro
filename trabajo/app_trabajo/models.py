from django.db import models


class Usuario(models.Model):
    usuario = models.TextField(unique=True)
    clave = models.TextField()
    rol = models.TextField()

    class Meta:
        managed = False
        db_table = 'usuarios'

    def __str__(self):
        return self.usuario


class Linea(models.Model):
    nombre = models.TextField()

    class Meta:
        managed = False
        db_table = 'lineas'

    def __str__(self):
        return self.nombre


class Tren(models.Model):
    codigo = models.TextField()

    class Meta:
        managed = False
        db_table = 'trenes'

    def __str__(self):
        return self.codigo


class Cochera(models.Model):
    nombre = models.TextField()

    class Meta:
        managed = False
        db_table = 'cocheras'

    def __str__(self):
        return self.nombre


class Reclamo(models.Model):

    TIPO_CHOICES = [
        ("reclamo", "Reclamo"),
        ("objeto_perdido", "Objeto perdido"),
        ("sugerencia", "Sugerencia"),
        ("otro", "Otro"),
    ]

    nombre = models.CharField(max_length=100)
    email = models.EmailField()
    tipo = models.CharField(max_length=20, choices=TIPO_CHOICES)
    estacion = models.CharField(max_length=100)
    fecha = models.DateField()
    descripcion = models.TextField()
    creado = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-creado']

    def __str__(self):
        return f"{self.tipo} - {self.nombre} ({self.fecha})"