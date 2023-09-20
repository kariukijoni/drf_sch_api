from rest_framework import generics
from api.serializers import DepartmentSerializer,FacultySerializer
from api.models import Department,Faculty

# department
class DepartmentList(generics.ListCreateAPIView):
    queryset=Department.objects.all()
    serializer_class=DepartmentSerializer
    
class DepartmentDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset=Department.objects.all()
    serializer_class=DepartmentSerializer
    
    
    
# faculty
class FacultyList(generics.ListCreateAPIView):
    queryset=Faculty.objects.all()
    serializer_class=FacultySerializer
    
class FacultyDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset=Faculty.objects.all()
    serializer_class=FacultySerializer