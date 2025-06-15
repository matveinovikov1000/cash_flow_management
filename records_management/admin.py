from django.contrib import admin

from records_management.models import (
    CashFlowStatement,
    EntrySubcategory,
    PostCategory,
    RecordStatus,
    RecordType,
)


@admin.register(EntrySubcategory)
class EntrySubcategoryAdmin(admin.ModelAdmin):
    list_display = (
        "title",
        "category",
        "formatted_created_at",
    )

    def formatted_created_at(self, obj):
        """Меняет формат отображения даты в админке"""
        return obj.created_at.strftime("%d.%m.%Y") if obj.created_at else ""

    formatted_created_at.short_description = "Дата создания/изменения"
    formatted_created_at.admin_order_field = "created_at"


@admin.register(PostCategory)
class PostCategoryAdmin(admin.ModelAdmin):
    list_display = (
        "title",
        "formatted_created_at",
        "type",
    )

    def formatted_created_at(self, obj):
        """Меняет формат отображения даты в админке"""
        return obj.created_at.strftime("%d.%m.%Y") if obj.created_at else ""

    formatted_created_at.short_description = "Дата создания/изменения"
    formatted_created_at.admin_order_field = "created_at"


@admin.register(RecordType)
class RecordTypeAdmin(admin.ModelAdmin):
    list_display = (
        "title",
        "formatted_created_at",
    )

    def formatted_created_at(self, obj):
        """Меняет формат отображения даты в админке"""
        return obj.created_at.strftime("%d.%m.%Y") if obj.created_at else ""

    formatted_created_at.short_description = "Дата создания/изменения"
    formatted_created_at.admin_order_field = "created_at"


@admin.register(RecordStatus)
class RecordStatusAdmin(admin.ModelAdmin):
    list_display = (
        "title",
        "formatted_created_at",
    )

    def formatted_created_at(self, obj):
        """Меняет формат отображения даты в админке"""
        return obj.created_at.strftime("%d.%m.%Y") if obj.created_at else ""

    formatted_created_at.short_description = "Дата создания/изменения"
    formatted_created_at.admin_order_field = "created_at"


@admin.register(CashFlowStatement)
class CashFlowStatementAdmin(admin.ModelAdmin):
    list_display = (
        "formatted_created_at",
        "status",
        "type",
        "category",
        "subcategory",
        "price",
        "comment",
    )
    list_filter = (
        "created_at",
        "status",
        "type",
        "category",
        "subcategory",
    )
    date_hierarchy = "created_at"

    def formatted_created_at(self, obj):
        """Меняет формат отображения даты в админке"""
        return obj.created_at.strftime("%d.%m.%Y") if obj.created_at else ""

    formatted_created_at.short_description = "Дата создания/изменения"
    formatted_created_at.admin_order_field = "created_at"
