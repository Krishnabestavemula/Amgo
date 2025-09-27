from rest_framework import serializers
from .models import Project, Asset, Job,AnalyticsEvent

class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = '__all__'

class AssetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Asset
        fields = '__all__'

class JobSerializer(serializers.ModelSerializer):
    class Meta:
        model = Job
        fields = '__all__'

class AnalyticsEventSerializer(serializers.ModelSerializer):
    projectId = serializers.PrimaryKeyRelatedField(
        source='project', queryset=Project.objects.all(), write_only=True
    )

    class Meta:
        model = AnalyticsEvent
        fields = ['projectId', 'event_type', 'timestamp']
        read_only_fields = ['timestamp']