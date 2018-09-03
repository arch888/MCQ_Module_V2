from django.db import models

from django.contrib.auth import authenticate,login,get_user_model,logout

User=get_user_model()
# Create your models here.



class leaderboard(models.Model):
	user=models.ForeignKey(User,on_delete=models.CASCADE)
	correct_qus=models.IntegerField()
	wrong_qus=models.IntegerField()
	points=models.IntegerField()
	message=models.CharField(max_length=255)
	attempted_qus=models.IntegerField()


	def __str__(self):
		return self.user.email
