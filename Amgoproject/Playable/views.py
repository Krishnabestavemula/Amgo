from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from .models import Project, Asset, Job
from .serializers import ProjectSerializer, AssetSerializer, JobSerializer, AnalyticsEventSerializer
from datetime import timedelta
import django_rq
from .tasks import render_job_function

class ProjectCreateView(APIView):
    def post(self, request):
        serializer = ProjectSerializer(data=request.data)
        if serializer.is_valid():
            project = serializer.save()
            return Response(ProjectSerializer(project).data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class AssetUploadView(APIView):
    def post(self, request, id):
        project = get_object_or_404(Project, id=id)
        uploaded_file = request.FILES.get('file')
        if not uploaded_file:
            return Response({"error": "No file provided"}, status=status.HTTP_400_BAD_REQUEST)

        asset = Asset.objects.create(project=project, file=uploaded_file)
        return Response(AssetSerializer(asset).data, status=status.HTTP_201_CREATED)


class RenderJobEnqueueView(APIView):
    def post(self, request, id):
        project = get_object_or_404(Project, id=id)
        job = Job.objects.create(project=project, status='pending')

        queue = django_rq.get_queue('default')
        queue.enqueue_in(timedelta(seconds=10), render_job_function, job.id)
        return Response(JobSerializer(job).data, status=status.HTTP_201_CREATED)

class JobStatusView(APIView):
    def get(self, request, id):
        job = get_object_or_404(Job, id=id)
        return Response(JobSerializer(job).data)


class AnalyticsEventView(APIView):
    def post(self, request):
        serializer = AnalyticsEventSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "Event logged"}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
