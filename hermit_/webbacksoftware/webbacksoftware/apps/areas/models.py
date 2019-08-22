from django.db import models

# Create your models here.
class Areas(models.Model):
    name=models.CharField(max_length=50,verbose_name='location')
    pid=models.ForeignKey('self',on_delete=models.SET_NULL,related_name='addinfos',null=True)


    class Meta:
        db_table='areas'

    def __str__(self):
        return self.name