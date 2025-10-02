# Create your views here.
from rest_framework import viewsets
from .models import Project
from .serializers import ProjectSerializer

# API view
class ProjectViewSet(viewsets.ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer