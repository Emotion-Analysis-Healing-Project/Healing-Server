from django.db import models

class Calender(models.Model):
    facial_choice=[
        ('G','good'),
        ('B','bad'),
        ('S','sad'),
        ('N','nervous')
    ]
    id=models.AutoField(primary_key=True,)
    date=models.DateTimeField(auto_now_add=True, null=False)
    facial=models.CharField(choices=facial_choice, max_length=1)
    #user

    def get_facial(self):
        return str(self.facial)
