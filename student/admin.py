from django.contrib import admin

# Register your models here.
import student
from student.models import Student


class StudentAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'sex', 'profession', 'email', 'qq', 'phone', 'status', 'crated_time')
    list_filter = ('sex', 'status', 'crated_time')
    search_fields = ('name', 'profession')
    fieldsets = (
        (None, {
            'fields': (
                'name',
                ('sex', 'profession'),
                ('email', 'qq', 'phone'),
                'status'
            )
        }),
    )


admin.site.register(Student, StudentAdmin)
