from django.db import models

# Create your models here.


class Food(models.Model):
    name = models.CharField(max_length=100, null=False, blank=False)
    description = models.CharField(max_length=1000, null=False, blank=False)
    isveg = models.BooleanField(default=True)
    price = models.IntegerField(null=False, blank=False)
    image = models.CharField(max_length=500, default='https://www.fnasafety.com/wp-content/uploads/2016/04/ComingSoon2-fnasafety.png', )

    def __str__(self) -> str:
        return self.name    
