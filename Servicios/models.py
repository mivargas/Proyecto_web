from django.db import models

# Create your models here.

class Servicio(models.Model):
	titulo=models.CharField(max_length=50)
	contenido=models.CharField(max_length=50)
	imagen=models.ImageField(upload_to='servicios') #aqui dentro de media lo suvira a servicios dentro de la misma, esto es muy util cuando se trabaja con mas de una aplicacion
	created=models.DateTimeField(auto_now_add=True)
	updated=models.DateTimeField(auto_now_add=True)


	class  Meta:
		verbose_name='servicio'
		verbose_name_plural='servicios'

	def __str__(self):
		return self.titulo
		