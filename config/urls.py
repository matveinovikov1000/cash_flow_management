from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("admin/", admin.site.urls),
    path(
        "records_management/",
        include("records_management.urls", namespace="records_management"),
    ),
]
