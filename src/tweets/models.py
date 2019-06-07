from django.db import models
from django.conf import settings
from .validators import validate_content
from django.urls import reverse
# Create your models here.


class Tweet(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL , on_delete = models.CASCADE)
    content = models.CharField(max_length=140 , validators=[validate_content])
    timestamp = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    # def clean(self,*args,**kwargs):
    #     content = self.content
    #     if content == "abc":
    #         raise ValidationError("It cannot be abc")
    #     return super(Tweet,self).clean(*args,**kwargs)

    def __str__(self):
        return str(self.content)

    def get_absolute_url(self):
        return reverse("tweets:detail_view" , kwargs={"pk":self.pk})