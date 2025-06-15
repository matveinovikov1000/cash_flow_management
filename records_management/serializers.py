from rest_framework import serializers

from records_management.models import (
    CashFlowStatement,
    EntrySubcategory,
    PostCategory,
    RecordStatus,
    RecordType,
)


class EntrySubcategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = EntrySubcategory
        fields = "__all__"


class PostCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = PostCategory
        fields = "__all__"


class RecordTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = RecordType
        fields = "__all__"


class RecordStatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = RecordStatus
        fields = "__all__"


class CashFlowStatementSerializer(serializers.ModelSerializer):
    class Meta:
        model = CashFlowStatement
        fields = "__all__"
