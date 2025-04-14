from django.contrib import admin
from testapp.models import StudentPG,StudentPhd
from testapp.models import Marksheet

class StudentPgAdmin(admin.ModelAdmin):
    list_display=['id','Inrollment_no','name','AdharCard','Mobile','Address','course','Gender','Semester','Fee']

admin.site.register(StudentPG,StudentPgAdmin)

class StudentPhdAdmin(admin.ModelAdmin):
    list_display=['id','Inrollment_no','name','AdharCard','Mobile','Address','course','Gender','Semester','Fee']

admin.site.register(StudentPhd,StudentPhdAdmin)

class MarksheetAdmin(admin.ModelAdmin):
    list_display=['id','Inrollment_no','student_name','Course','Gender','Semester','Subject_1','Subject_2','Subject_3','Subject_4','Subject_5','Total_Marks','Total_Obtained','Percentage','status']
admin.site.register(Marksheet,MarksheetAdmin)