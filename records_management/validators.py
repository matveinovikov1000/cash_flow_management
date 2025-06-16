from django.core.exceptions import ValidationError


def validate_cash_flow(obj):
    """Валидация для модели CashFlowStatement:
    - подкатегория должна принадлежать выбранной категории;
    - категария должна относится к выбранному типу
    """
    if obj.subcategory and obj.subcategory.category != obj.category:
        raise ValidationError(
            f"Подкатегория {obj.subcategory} не относится к категории {obj.category}"
        )

    if obj.category and obj.category.type != obj.type:
        raise ValidationError(
            f"Категория {obj.category} не относится к типу {obj.type}"
        )
