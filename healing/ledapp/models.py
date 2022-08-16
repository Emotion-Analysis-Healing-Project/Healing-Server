from django.db import models
from calenderapp.models import Calender

class LED(models.Model):
    color_choice=[
        ('r','red'),
        ('b','blue'),
        ('g','green'),
        ('y','yellow'),
    ]
    state_choice=[
        ('1','on'),
        ('0','off')
    ]

    id=models.AutoField(primary_key=True)
    date=models.ForeignKey(Calender, on_delete=models.CASCADE,null=True)
    color=models.CharField(choices=color_choice, max_length=1)
    state=models.CharField(choices=state_choice, max_length=1, default=0)

    def __str__(self):
        return self.color
    
    def get_color(self):
        return self.color_choice