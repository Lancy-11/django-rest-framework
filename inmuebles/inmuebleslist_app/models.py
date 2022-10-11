from django.db import models



# Create your models here.
class Edificacion(models.Model) :
    direccion = models.CharField(max_length=255)
    ciudad = models.CharField(max_length=255)
    CP = models.DecimalField(help_text="ingrese codigo postal",decimal_places=0 ,max_digits=6 ) 
    pais = models.CharField(max_length=255)
    activo = models.BooleanField(default=True)
    Creado = models.DateTimeField(auto_now_add=True)
    

    
    
    def __str__(self) : 
         return self.direccion

class Empresa(models.Model):
    nombre = models.CharField(max_length=250)
    website = models.URLField(max_length=250)
    activo = models.BooleanField(default=True)
    
    def __str__ (self):
        return self.nombre
    
                
                
        
    
    
            

    
