from django.db import models

# Create your models here.

class Propietario(models.Model):
	opcionesTipo = (
		('ecuatoriana', 'Ecuatoriana'),
		('peruana', 'Peruana'),
		('colombiana', 'Colombiana'),
	)
	nombre = models.CharField(max_length=30)
	apellido = models.CharField(max_length=30)
	edad = models.IntegerField('Edad')
	nacionalidad = models.CharField(max_length=25, choices=opcionesTipo)
	def __str__(self):
		return "%s %s %d %s" % (self.nombre,
			self.apellido,
			self.edad,
			self.nacionalidad)

class Departamento(models.Model):
	costo = models.DecimalField(max_digits=100, decimal_places=2)
	nroCuartos = models.IntegerField('Numero de cuartos')
	nroBaños = models.IntegerField('Numero de baños')
	valorAlicuota = models.DecimalField(max_digits=100, decimal_places=2)
	propietario = models.ForeignKey(Propietario, on_delete=models.CASCADE, related_name="departamentos")

	def __str__(self):
		return "%.2f %d %d %.2f" % (self.costo, 
			self.nroCuartos,
			self.nroBaños,
			self.valorAlicuota)
