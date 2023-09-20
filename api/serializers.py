from rest_framework import serializers
from .models import Department,Faculty

# Department
class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model=Department
        fields=['name','faculty']
        
# faculty
class FacultySerializer(serializers.ModelSerializer):
    class Meta:
        model=Faculty
        fields=['name']