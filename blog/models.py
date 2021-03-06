from django.db import models
from datetime import datetime
from django.utils import timezone
from django.contrib.auth.models import User
import datetime
import sys

reload(sys)
sys.setdefaultencoding('utf8')

class Post(models.Model):
	autor = models.ForeignKey('auth.User')
	titulo = models.CharField(max_length = 200)
	texto = models.TextField()
	fecha_creacion = models.DateTimeField(default=timezone.now)
	fecha_publicacion = models.DateTimeField(blank=True, null=True)

	def publish(self):
		self.fecha_publicacion = timezone.now()
		self.save()

	def __unicode__(self):
		return self.titulo
