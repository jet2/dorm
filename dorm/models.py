from django.db import models

class Handlezone(models.Model):
	id = models.AutoField(primary_key=True)
	caption = models.TextField()

	def add_zone(self):
		self.caption='Безымянная'
		self.save()

	def __str__(self):
		return self.caption

class Room(models.Model):
	handlezone_id = models.ForeignKey('Handlezone')
	number = models.TextField()
	level  = models.IntegerField()
	length = models.IntegerField()
	width  = models.IntegerField()
	bedscount = models.IntegerField()
	comfort = models.IntegerField() 
	bedslocked = models.IntegerField()

	def add_room(self):
		self.number='xxx'
		self.level  = 1
		self.length = 3
		self.width  = 3
		self.bedscount = 8
		self.comfort = 1
		self.bedslocked = 0
		self.save()

	def __str__(self):
		return self.number +'/'+  str(self.bedscount)+'/'+ str(self.bedslocked)