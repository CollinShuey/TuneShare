from django.db import models
from django.contrib.auth import get_user_model
# Create your models here.
# Gets current user model and stores it in User, the default one that comes with Django
User = get_user_model()

class Profile(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    id_user = models.IntegerField()
    bio = models.TextField(blank=True,max_length=500)
    profileimg = models.ImageField(upload_to='profile_images',default='blank-profile-picture.png')
    location = models.CharField(max_length=100,blank=True)

    def __str__(self):
        return self.user.get_username()
