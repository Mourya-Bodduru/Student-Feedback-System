from django.contrib import admin
from feedback.models import Student, Feedback ,Contact

class MemberAdmin(admin.ModelAdmin):
    list_display = ("reg_no", "username", "year", "email")  

admin.site.register(Student, MemberAdmin)

@admin.register(Feedback)
class FeedbackAdmin(admin.ModelAdmin):
    list_display = ['tname', 'sname', 'dept', 'feedback_text', 'rating']

class contactAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'message', 'is_resolved')
    list_editable = ('is_resolved',)



admin.site.register(Contact,contactAdmin)