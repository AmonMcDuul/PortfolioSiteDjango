from django.db.models.signals import post_save, post_delete
# from django.dispatch import receiver
from django.contrib.auth.models import User
from django.core.mail import send_mail
from django.conf import settings
from .models import Profile


# @receiver(post_save, sender=Profile)
def createProfile(sender, instance, created, **kwargs):
    if created:
        user = instance
        profile = Profile.objects.create(
            user = user,
            username = user.username,
            email = user.email,
            name = user.first_name
        )
        subject = "Welcome to JoranSchols!"
        message = 'Supercool dat je je hebt aangemeld op JoranSchols.com!!'

        send_mail(
            subject,
            message,
            settings.EMAIL_HOST_USER,
            [profile.email],
            fail_silently=False
        )

def updateUser(sender, instance, created, **kwargs):
    profile = instance
    user = profile.user
    if created == False:
        user.first_name = profile.name
        user.username = profile.username
        user.email = profile.email
        user.save()


def deleteUser(sender, instance, **kwargs):
    try:
        user = instance.user
        user.delete()
    except:
        pass

def messageCreated(inputname, inputemail, inputsubject, inputmessage):
    subject = "Message recieved on JoranSchols"
    message = ('Er is een bericht verstuurd\n\ndoor: '+ inputname + '\nemail: ' + inputemail + '\n\nbericht:\n' + inputsubject + '\n\n' + inputmessage)
    email = ['schols.joran@gmail.com']

    send_mail(
        subject,
        message,
        settings.EMAIL_HOST_USER,
        email,
        fail_silently=False
    )

post_save.connect(createProfile, sender=User)
post_save.connect(updateUser, sender=Profile)
post_delete.connect(deleteUser, sender=Profile)