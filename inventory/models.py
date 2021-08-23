from django.db import models

# Create your models here.
class Categoria(models.Model):
    cat_nomb = models.CharField(max_length=150, blank=False)
    def __str__(self):
        return self.cat_nomb

class Marca(models.Model):
    marca_nomb = models.CharField(max_length=100)
    def __str__(self):
        return self.marca_nomb

class Tipomascota(models.Model):
    tip_mascota = models.CharField(max_length=100)
     
    def __str__(self): 
        return self.tip_mascota

class Producto(models.Model):
    prod_nomb = models.CharField(max_length=150)
    precio = models.DecimalField(max_digits=6, decimal_places=2, help_text='Solo número')
    opciones_estado = (
        ('DISPONIBLE', 'Listo para ser vendido'),
        ('AGOTADO', 'Producto agotado'),
        ('BAJO_STOCK', 'Bajo stock del producto')
    )
    estado = models.CharField(max_length=20, choices=opciones_estado, default="DISPONIBLE")
    cat_prod = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    marca_nomb = models.ForeignKey(Marca, on_delete=models.CASCADE, blank=True, null=True)
    tip_mascota = models.ForeignKey(Tipomascota, on_delete=models.CASCADE)
    def __str__(self):
        return self.prod_nomb

