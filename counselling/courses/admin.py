from django.contrib import admin

from courses.models import CoursesPage, ExamCategory, Course, TopCollege, NeedHelpSection

class ExamcategoryInline(admin.TabularInline):
    model = ExamCategory
    extra = 1
    
class TopCollegeInline(admin.StackedInline):
    model = TopCollege
    extra = 1
    
class NeedHelpSectionInline(admin.StackedInline):
    model = NeedHelpSection
    extra = 1

class CourseInline(admin.StackedInline):
    model = Course
    extra = 1
# @admin.register(TopCollege)
# class TopCollegeAdmin(admin.ModelAdmin):
#     list_display = ("exam_category","name","college_type","location","order")
    
    
    
      
@admin.register(CoursesPage)
class CoursePageAdmin(admin.ModelAdmin):
    list_display = ("page", "created_at")
    inlines = [
        ExamcategoryInline,
        NeedHelpSectionInline
    ]
    
@admin.register(ExamCategory)
class ExamCategoryAdmin(admin.ModelAdmin):
    list_display = ("title","courses_page","order","created_at")
    list_filter = ("courses_page",)
    search_fields = ("title",)
    ordering = ("order",)
    inlines = [
        CourseInline,
        TopCollegeInline,
    ]
        