from django.db import models

class Department(models.Model):
    name=models.CharField(max_length=23)
    faculty=models.ForeignKey('Faculty', on_delete=models.CASCADE, null=True)
    
    
    def __str__(self):
        return self.faculty.name + " =>" + self.name
        
    
class Faculty(models.Model):
    name=models.CharField(max_length=255,default='Science')
    
    class Meta:
        # verbose_name='Faculty'
        verbose_name_plural='Faculties'

    def __str__(self):
        return self.name