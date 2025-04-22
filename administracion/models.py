from django.db import models
from administracion.validadorRut import validador_rut_django # para validar el rut

# Create your models here.

class Rol(models.Model):
    TIPO_ROLES = [
        ('residente', 'Residente'),
        ('conserje', 'Conserje'),
        ('super_administrador', 'Super Administrador'),
    ]
    tipo = models.CharField(max_length=50, unique=True, choices=TIPO_ROLES)

    def __str__(self):
        return self.get_tipo_display()

class ComplejoHabitacional(models.Model):
    TIPO_HABITACIONAL = [('edificio','Edificio'),('condominio','Condominio')]
    nombre = models.CharField(max_length=50, unique=True)
    direccion = models.CharField(max_length=150)
    tipo = models.CharField(max_length=20, choices=TIPO_HABITACIONAL)

    def __str__(self):
        return self.nombre
    
class UnidadHabitacional(models.Model):
    TIPO_OPCIONES = [
        ('departamento', 'Departamento'),
        ('casa', 'Casa'),
    ]
    numero = models.CharField(max_length=10)
    letra = models.CharField(max_length=5, blank=True, null=True)
    bloque = models.CharField(max_length=10, blank=True, null=True)
    piso = models.IntegerField(blank=True,null=True)
    tipo = models.CharField(max_length=20, choices=TIPO_OPCIONES)
    complejo = models.ForeignKey(ComplejoHabitacional, on_delete=models.PROTECT, null=True, blank=True) #no olvidar sacar a futuro ese null y

    def __str__(self):
        if self.tipo == 'departamento':
            if self.piso and self.bloque:
                return f"Depto {self.numero}, Piso {self.piso}, Bloque {self.bloque}"
            elif self.piso:
                return f"Depto {self.numero}, Piso {self.piso}"
            elif self.bloque:
                return f"Depto {self.numero}, Bloque{self.bloque}"
            else:
                return f"Depto {self.numero}"
        
        elif self.tipo =='casa':
            if self.letra:
                return f"Casa {self.numero} Letra {self.letra}"
            else:
                return f"Casa {self.numero}"
        
        else:
            return self.numero

class Residente(models.Model):
    nombre = models.CharField(max_length=100)
    rut = models.CharField(max_length=12, primary_key=True, validators=[validador_rut_django])
    correo = models.EmailField(unique=True)
    fecha_registro = models.DateTimeField(auto_now_add=True)
    unidad = models.ForeignKey(UnidadHabitacional, on_delete=models.PROTECT)
    rol = models.ForeignKey(Rol, on_delete=models.PROTECT)

    def __str__(self):
        return self.nombre
    

