from django.core.validators import MinValueValidator
from django.db import models
from rest_framework.exceptions import ValidationError


class RecordType(models.Model):
    """Модель типа записи движения денежных средтсв"""

    title = models.CharField(
        max_length=100,
        unique=True,
        verbose_name="Название типа",
        help_text="Укажите название типа",
    )
    created_at = models.DateField(auto_now=True)

    class Meta:
        verbose_name = "Тип записи движения денежных средств"
        verbose_name_plural = "Типы записей движения денежных средств"
        ordering = [
            "title",
            "created_at",
        ]

    def __str__(self):
        return self.title


class PostCategory(models.Model):
    """Модель категории записи движения денежных средтсв"""

    title = models.CharField(
        max_length=100,
        unique=True,
        verbose_name="Название категории",
        help_text="Укажите название категории",
    )
    type = models.ForeignKey(
        RecordType,
        on_delete=models.CASCADE,
        default=None,
        verbose_name="Тип",
        help_text="Укажите тип, к которому относится категория",
        related_name="categories",
    )
    created_at = models.DateField(auto_now=True)

    class Meta:
        verbose_name = "Категория записи движения денежных средств"
        verbose_name_plural = "Категории записей движения денежных средств"
        ordering = [
            "title",
            "type",
            "created_at",
        ]

    def __str__(self):
        return self.title


class EntrySubcategory(models.Model):
    """Модель подкатегории записи движения денежных средтсв"""

    title = models.CharField(
        max_length=100,
        unique=True,
        verbose_name="Название подкатегории",
        help_text="Укажите название подкатегории",
    )
    category = models.ForeignKey(
        PostCategory,
        on_delete=models.CASCADE,
        default=None,
        verbose_name="Категория",
        help_text="Укажите категорию, в которую входит подкатегория",
        related_name="subcategories",
    )
    created_at = models.DateField(auto_now=True)

    class Meta:
        verbose_name = "Подкатегория записи движения денежных средств"
        verbose_name_plural = "Подкатегории записей движения денежных средств"
        ordering = [
            "title",
            "category",
            "created_at",
        ]

    def __str__(self):
        return self.title


class RecordStatus(models.Model):
    """Модель статуса записи движения денежных средтсв"""

    title = models.CharField(
        max_length=100,
        unique=True,
        verbose_name="Название статуса",
        help_text="Укажите название статуса",
    )
    created_at = models.DateField(auto_now=True)

    class Meta:
        verbose_name = "Статус записи движения денежных средств"
        verbose_name_plural = "Статусы записей движения денежных средств"
        ordering = [
            "title",
            "created_at",
        ]

    def __str__(self):
        return self.title


class CashFlowStatement(models.Model):
    """Модель записи движения денежных средств"""

    created_at = models.DateField(auto_now=True)
    status = models.ForeignKey(
        RecordStatus,
        on_delete=models.PROTECT,
        blank=True,
        null=True,
        verbose_name="Статус",
        help_text="Укажите статус записи",
        related_name="cash_flow_statement",
    )
    type = models.ForeignKey(
        RecordType,
        on_delete=models.PROTECT,
        verbose_name="Тип",
        help_text="Укажите тип записи",
        related_name="cash_flow_statement",
    )
    category = models.ForeignKey(
        PostCategory,
        on_delete=models.PROTECT,
        verbose_name="Категория",
        help_text="Укажите категорию записи",
        related_name="cash_flow_statement",
    )
    subcategory = models.ForeignKey(
        EntrySubcategory,
        on_delete=models.PROTECT,
        verbose_name="Подкатегория",
        help_text="Укажите подкатегорию записи",
        related_name="cash_flow_statement",
    )
    price = models.DecimalField(
        max_digits=15,
        decimal_places=2,
        validators=[
            MinValueValidator(0),
        ],
        verbose_name="Сумма в рублях",
        help_text="Укажите сумму в рублях",
    )
    comment = models.TextField(
        blank=True,
        null=True,
        verbose_name="Комментарий",
        help_text="Укажите комментарий к записи",
    )

    class Meta:
        verbose_name = "Запись о движении денежных средств"
        verbose_name_plural = "Записи о движении денежных средств"
        ordering = [
            "created_at",
            "status",
            "type",
            "category",
            "subcategory",
            "price",
        ]

    def __str__(self):
        return f"{self.status} {self.type} {self.price}"

    def clean(self):
        """Ограничивает выбор подкатегории для категории и выбор категории для типа"""
        if self.subcategory and self.subcategory.category != self.category:
            raise ValidationError(
                f"Подкатегория {self.subcategory} не относится к категории {self.category}"
            )

        if self.category and self.category.type != self.type:
            raise ValidationError(
                f"Категория {self.category} не относится к типу {self.type}"
            )
