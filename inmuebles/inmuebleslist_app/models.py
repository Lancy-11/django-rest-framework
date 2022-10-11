from django.db import models



# Create your models here.
class Inmueble(models.Model) :
    direccion = models.CharField(max_length=255)
    ciudad = models.CharField(max_length=255)
    CP = models.DecimalField(help_text="ingrese codigo postal",decimal_places=1 ,max_digits=6 ) 
    pais = models.CharField(max_length=255)
    activo = models.BooleanField(default=True)


    
    
    def __str__(self) : 
         return self.direccion
                
                
        
    
    
            

    
