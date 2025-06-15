from django.urls import path

from records_management.apps import RecordsManagementConfig
from records_management.views import (
    CashFlowStatementCreateAPIView,
    CashFlowStatementDestroyAPIView,
    CashFlowStatementListAPIView,
    CashFlowStatementUpdateAPIView,
    EntrySubcategoryCreateAPIView,
    EntrySubcategoryDestroyAPIView,
    EntrySubcategoryUpdateAPIView,
    PostCategoryCreateAPIView,
    PostCategoryDestroyAPIView,
    PostCategoryUpdateAPIView,
    RecordStatusCreateAPIView,
    RecordStatusDestroyAPIView,
    RecordStatusUpdateAPIView,
    RecordTypeCreateAPIView,
    RecordTypeDestroyAPIView,
    RecordTypeUpdateAPIView,
)

app_name = RecordsManagementConfig.name

urlpatterns = [
    path(
        "cash_flow_statements/",
        CashFlowStatementListAPIView.as_view(),
        name="cash_flow_statements",
    ),
    path(
        "cash_flow_create/",
        CashFlowStatementCreateAPIView.as_view(),
        name="cash_flow_create",
    ),
    path(
        "cash_flow_update/<int:pk>/",
        CashFlowStatementUpdateAPIView.as_view(),
        name="cash_flow_update",
    ),
    path(
        "cash_flow_delete/<int:pk>/",
        CashFlowStatementDestroyAPIView.as_view(),
        name="cash_flow_delete",
    ),
    path(
        "subcategory_create/",
        EntrySubcategoryCreateAPIView.as_view(),
        name="subcategory_create",
    ),
    path(
        "subcategory_update/<int:pk>/",
        EntrySubcategoryUpdateAPIView.as_view(),
        name="subcategory_update",
    ),
    path(
        "subcategory_delete/<int:pk>/",
        EntrySubcategoryDestroyAPIView.as_view(),
        name="subcategory_delete",
    ),
    path(
        "category_create/", PostCategoryCreateAPIView.as_view(), name="category_create"
    ),
    path(
        "category_update/<int:pk>/",
        PostCategoryUpdateAPIView.as_view(),
        name="category_update",
    ),
    path(
        "category_delete/<int:pk>/",
        PostCategoryDestroyAPIView.as_view(),
        name="category_delete",
    ),
    path("type_create/", RecordTypeCreateAPIView.as_view(), name="type_create"),
    path(
        "type_update/<int:pk>/", RecordTypeUpdateAPIView.as_view(), name="type_update"
    ),
    path(
        "type_delete/<int:pk>/", RecordTypeDestroyAPIView.as_view(), name="type_delete"
    ),
    path("status_create/", RecordStatusCreateAPIView.as_view(), name="status_create"),
    path(
        "status_update/<int:pk>/",
        RecordStatusUpdateAPIView.as_view(),
        name="status_update",
    ),
    path(
        "status_delete/<int:pk>/",
        RecordStatusDestroyAPIView.as_view(),
        name="status_delete",
    ),
]
