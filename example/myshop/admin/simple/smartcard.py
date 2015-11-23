# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib import admin
from django.utils.translation import ugettext_lazy as _
from adminsortable2.admin import SortableAdminMixin
from shop.admin.product import CMSPageAsCategoryMixin, ProductImageInline
from myshop.models import SmartCard


@admin.register(SmartCard)
class SmartCardAdmin(SortableAdminMixin, CMSPageAsCategoryMixin, admin.ModelAdmin):
    fieldsets = (
        (None, {
            'fields': ('name', 'slug', 'unit_price', 'active', 'description',),
        }),
        (_("Properties"), {
            'fields': ('manufacturer', 'storage', 'card_type',)
        }),
    )
    inlines = (ProductImageInline,)
    prepopulated_fields = {'slug': ('name',)}
    list_display = ('name', 'unit_price', 'active',)