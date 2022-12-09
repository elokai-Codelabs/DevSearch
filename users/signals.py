# import signals for post_save method
from django.db.models.signals import post_save,post_delete
from django.dispatch import receiver

# 
from django.contrib.auth.models import User
from .models import Profile

from django.core.mail import send_mail, EmailMessage
from django.conf import settings

from django.http import HttpResponse

 # you can connect using @receiver()
# @receiver(post_save, sender=Profile)
def createProfile(sender,instance,created,**kwargs):
    print("profile saved")
    print("profile saved")
    print("profile saved")
    print("profile saved")
    if created:
        user = instance
        profile = Profile.objects.create(
            user=user,
            username = user.username,
            email = user.email,
            name = user.first_name,)

        # subject ='Welcome to DevSearch'
        # message = 'We are glad you are here!'
        
        # to_be_sent = EmailMessage(
        #     subject, message, settings.EMAIL_HOST_USER, ['pskyeremanteng@st.ug.edu.gh']
        # )

        # to_be_sent.fail_silently = True
        # to_be_sent.save()
        # return HttpResponse('<h1>Mail send witout error</h1>')

def deleteUser(sender,instance,**kwargs):
    user = instance.user
    user.delete()

   
post_save.connect(createProfile,sender=User)
post_delete.connect(deleteUser,sender=Profile)