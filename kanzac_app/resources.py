from import_export import resources
from import_export.fields import Field
from import_export.widgets import ForeignKeyWidget

from .models import *


class OtherResource(resources.ModelResource):
    id = Field(column_name='Zakaz id', attribute='id')

    user = Field(
        column_name='Foydalanuvchi',
        attribute='user',
        widget=ForeignKeyWidget(model=User, field='name'))

    user_phone = Field(
        column_name='Raqam',
        attribute='user',
        widget=ForeignKeyWidget(model=User, field='phone')
    )

    product = Field(
        column_name='Kategoriya',
        attribute='product',
        widget=ForeignKeyWidget(model=Product, field='category__name'))

    price = Field(
        column_name='Narx',
        attribute='product',
        widget=ForeignKeyWidget(model=Product, field='price')
    )

    created_date = Field(column_name='Sana', attribute='created_date')

