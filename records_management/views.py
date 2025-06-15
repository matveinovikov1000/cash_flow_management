from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics

from records_management.filters import CashFlowStatementFilter
from records_management.models import (
    CashFlowStatement,
    EntrySubcategory,
    PostCategory,
    RecordStatus,
    RecordType,
)
from records_management.serializers import (
    CashFlowStatementSerializer,
    EntrySubcategorySerializer,
    PostCategorySerializer,
    RecordStatusSerializer,
    RecordTypeSerializer,
)


class CashFlowStatementListAPIView(generics.ListAPIView):
    """Получает список записей о движении денежных средств"""

    queryset = CashFlowStatement.objects.all()
    serializer_class = CashFlowStatementSerializer
    filter_backends = (DjangoFilterBackend,)
    filterset_class = CashFlowStatementFilter
    search_fields = (
        "status",
        "type",
        "category",
        "subcategory",
    )
    filterset_fields = ("created_at",)


class CashFlowStatementCreateAPIView(generics.CreateAPIView):
    """Создает запись о движении денежных средств"""

    queryset = CashFlowStatement.objects.all()
    serializer_class = CashFlowStatementSerializer


class CashFlowStatementUpdateAPIView(generics.UpdateAPIView):
    """Редактирует запись о движении денежных средств"""

    queryset = CashFlowStatement.objects.all()
    serializer_class = CashFlowStatementSerializer


class CashFlowStatementDestroyAPIView(generics.DestroyAPIView):
    """Удаляет запись о движении денежных средств"""

    queryset = CashFlowStatement.objects.all()
    serializer_class = CashFlowStatementSerializer


class EntrySubcategoryCreateAPIView(generics.CreateAPIView):
    """Создает подкатегорию"""

    queryset = EntrySubcategory.objects.all()
    serializer_class = EntrySubcategorySerializer


class EntrySubcategoryUpdateAPIView(generics.UpdateAPIView):
    """Редактирует подкатегорию"""

    queryset = EntrySubcategory.objects.all()
    serializer_class = EntrySubcategorySerializer


class EntrySubcategoryDestroyAPIView(generics.DestroyAPIView):
    """Удаляет подкатегорию"""

    queryset = EntrySubcategory.objects.all()
    serializer_class = EntrySubcategorySerializer


class PostCategoryCreateAPIView(generics.CreateAPIView):
    """Создает категорию"""

    queryset = PostCategory.objects.all()
    serializer_class = PostCategorySerializer


class PostCategoryUpdateAPIView(generics.UpdateAPIView):
    """Редактирует категорию"""

    queryset = PostCategory.objects.all()
    serializer_class = PostCategorySerializer


class PostCategoryDestroyAPIView(generics.DestroyAPIView):
    """Удаляет категорию"""

    queryset = PostCategory.objects.all()
    serializer_class = PostCategorySerializer


class RecordTypeCreateAPIView(generics.CreateAPIView):
    """Создает тип"""

    queryset = RecordType.objects.all()
    serializer_class = RecordTypeSerializer


class RecordTypeUpdateAPIView(generics.UpdateAPIView):
    """Редактирует тип"""

    queryset = RecordType.objects.all()
    serializer_class = RecordTypeSerializer


class RecordTypeDestroyAPIView(generics.DestroyAPIView):
    """Удаляет тип"""

    queryset = RecordType.objects.all()
    serializer_class = RecordTypeSerializer


class RecordStatusCreateAPIView(generics.CreateAPIView):
    """Создает статус"""

    queryset = RecordStatus.objects.all()
    serializer_class = RecordStatusSerializer


class RecordStatusUpdateAPIView(generics.UpdateAPIView):
    """Редактирует статус"""

    queryset = RecordStatus.objects.all()
    serializer_class = RecordStatusSerializer


class RecordStatusDestroyAPIView(generics.DestroyAPIView):
    """Удаляет статус"""

    queryset = RecordStatus.objects.all()
    serializer_class = RecordStatusSerializer
