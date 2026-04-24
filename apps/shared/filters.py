from django_filters import rest_framework as filters
from django_filters import CharFilter
from django.db import models


FILTERABLE_FIELD_TYPES = (
    models.BooleanField,
    models.IntegerField,
    models.FloatField,
    models.DecimalField,
    models.SmallIntegerField,
    models.PositiveIntegerField,
    models.PositiveSmallIntegerField,
    models.CharField,
)


def is_filterable_field(field: models.Field) -> bool:
    if isinstance(field, FILTERABLE_FIELD_TYPES):
        if isinstance(field, models.CharField) and not field.choices:
            return False
        return True
    return False


def get_filterable_fields(model) -> dict:
    return {
        field.name: ["exact"]
        for field in model._meta.get_fields()
        if isinstance(field, models.Field) and is_filterable_field(field)
    }


class BaseAutoFilterSet(filters.FilterSet):
    class Meta:
        abstract = True
        filter_overrides = {
            models.ImageField: {
                "filter_class": CharFilter,
                "extra": lambda f: {"lookup_expr": "exact"},
            },
            models.FileField: {
                "filter_class": CharFilter,
                "extra": lambda f: {"lookup_expr": "exact"},
            },
        }


def make_filter(model):
    class AutoFilter(BaseAutoFilterSet):
        class Meta(BaseAutoFilterSet.Meta):
            abstract = False
            m = model
            fields = get_filterable_fields(m)

        Meta.model = model

    return AutoFilter