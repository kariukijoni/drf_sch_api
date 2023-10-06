from django.urls import path,include
from .import views

urlpatterns = [
    path('departments/',views.DepartmentList.as_view()),
    path('departments/<int:pk>/',views.DepartmentDetail.as_view()),
    path('faculty/',views.FacultyList.as_view()),
    path('faculty/<int:pk>/',views.FacultyDetail.as_view()),
]
