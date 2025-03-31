from django.contrib import admin
from .models import ErrorReport, Cabinets

# from django.contrib.admin.models import LogEntry #удаление последних действий
# LogEntry.objects.all().delete()


def mark_as_fixed(modeladmin, request, queryset):
    queryset.update(is_fixed=True)
    modeladmin.message_user(request, "Выбранные баги помечены как исправленные")
mark_as_fixed.short_description = "Отметить баг, как исправленный"

@admin.register(ErrorReport) #отображение в admin панели отправленных ошибок
class ErrorReportAdmin(admin.ModelAdmin):
    list_display = ('user', 'description', 'file', 'createdAt', 'is_fixed')
    search_fields = ('createdAt',)
    list_filter = ('createdAt',)
    actions = [mark_as_fixed]

@admin.register(Cabinets) #отображение в admin панели кабинетов
class CabinetsAdmin(admin.ModelAdmin):
    list_display = ('cabinetsId', 'cabinetsName', 'xCoord', 'yCoord')
    search_fields = ('cabinetsId', 'cabinetsName')
