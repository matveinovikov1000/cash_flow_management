from django_filters import DateFilter, FilterSet

from records_management.models import CashFlowStatement


class CashFlowStatementFilter(FilterSet):
    """Фильтрация по периоду дат"""

    created_at_start = DateFilter(field_name="created_at", lookup_expr="gte")
    created_at_end = DateFilter(field_name="created_at", lookup_expr="lte")

    class Meta:
        model = CashFlowStatement
        fields = [
            "status",
            "type",
            "category",
            "subcategory",
        ]
