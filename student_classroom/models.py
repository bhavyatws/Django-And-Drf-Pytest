from django.utils.text import slugify
from django.db import models
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _

# Create your models here.

#validator
def avg_score_validator(value):
    if value < 0:
        raise ValidationError(
            _('%(value)s must be positive integer'),
            params={'value':value}
        )
class Student(models.Model):
    first_name=models.CharField(max_length=50)
    last_name=models.CharField(max_length=50)
    username=models.SlugField(blank=True,null=True)
    admission_number=models.IntegerField(unique=True)
    is_qualified=models.BooleanField(default=False)
    average_score=models.FloatField(blank=True,null=True,validators=[avg_score_validator])
    
    
    
    def __str__(self) -> str:
        return str(self.first_name)

    def get_score(self):
        if 0<= self.average_score < 40:
            return "Fail"
        elif 40 <= self.average_score <70:
            return "Pass"  

        elif 70 <= self.average_score <=100:
            return "Excellent"
        else:
            return "Error"  

    def save(self,*args,**kwargs):
        self.username=slugify(self.first_name)
        super(Student,self).save(*args,**kwargs)

class Classroom(models.Model):
    name=models.CharField(max_length=50)
    student_capacity=models.IntegerField(default=0)
    #student=models.ManyToManyField("app_name.model_name") i.e model_name is actually table name 
    student=models.ManyToManyField("student_classroom.Student")

    def __str__(self) -> str:
        return str(self.name)