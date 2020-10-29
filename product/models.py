from django.db import models

class Device(models.Model):
    def __str__(self):
        return self.manufacturer + " " + self.model_number
    manufacturer = models.CharField(max_length=200)
    model_number = models.CharField(max_length=200)
    


class Test_Results(models.Model):
    def __str__(self):
        return self.test_sequence + self.test_date
    product = models.ForeignKey(Device, on_delete=models.CASCADE)
    test_sequence = models.CharField(max_length=200)
    condition = models.CharField(max_length=200)
    test_date = models.DateTimeField('date tested')
    isc = models.FloatField(default=0)
    voc = models.FloatField(default=0)
    imp = models.FloatField(default=0)
    vmp = models.FloatField(default=0)
    ff = models.FloatField(default=0)
    pmp = models.FloatField(default=0)