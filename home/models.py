from distutils.command.upload import upload
from django.db import models
STATE_CHOICES=(
    ('Andhra Pradesh','Andhra Pradesh'),('Assam','Assam'),('Bihar','Bihar'),('Chhattisgarh','Chhattisgarh'),('Goa','Goa'),('Gujarat','Gujarat'),('Haryana','Haryana'),('Himachal Pradesh','Himachal Pradesh'),('Jammu and Kashmir','Jammu and Kashmir'),('Jharkhand','Jharkhand'),('Karnataka','Karnataka'),('Kerala','Kerala'),('Madhya Pradesh','Madhya Pradesh'),('Maharashtra','Maharashtra'),
)
# Create your models here.
class Resume(models.Model):
    name=models.CharField(max_length=50)
    dob=models.DateField(auto_now=False,auto_now_add=False)
    gender=models.CharField(max_length=25)
    locality=models.CharField(max_length=100)
    city=models.CharField(max_length=100)
    pin=models.PositiveIntegerField()
    state=models.CharField(choices=STATE_CHOICES,max_length=25)
    mobile=models.PositiveIntegerField()
    email=models.EmailField()
    job_city=models.CharField(max_length=25)
    profile_img=models.ImageField(upload_to="MyImage",blank=True)
    file_doc=models.FileField(upload_to="MyFile",blank=True)
