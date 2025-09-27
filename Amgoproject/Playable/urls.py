from django.urls import path, include
from .views import ProjectCreateView, AssetUploadView, RenderJobEnqueueView, JobStatusView, AnalyticsEventView

from django.contrib import admin
from django.urls import path, include
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

schema_view = get_schema_view(
   openapi.Info(
      title="Amgo API",
      default_version='v1',
      description="Minimal backend for project + render job + asset upload",
      terms_of_service="https://www.example.com/terms/",
      contact=openapi.Contact(email="contact@example.com"),
      license=openapi.License(name="MIT License"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)
urlpatterns = [
    path('projects/', ProjectCreateView.as_view(), name='create-project'),
    path('projects/<int:id>/assets/', AssetUploadView.as_view(), name='upload-asset'),
    path('projects/<int:id>/render/', RenderJobEnqueueView.as_view(), name='enqueue-render'),
    path('jobs/<int:id>/', JobStatusView.as_view(), name='job-status'),
    path('analytics/', AnalyticsEventView.as_view(), name='log-analytics'),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path("django-rq/", include("django_rq.urls")),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]