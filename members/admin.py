from django.contrib import admin
from .models import Member, Chapter


class MemberList(admin.ModelAdmin):
    list_display = ('memberFName', 'memberMidInitial', 'memberLName')
    list_filter = ('memberFName', 'memberLName')
    search_fields = ('memberLName', )
    ordering = ['memberLName']


class ChapterList(admin.ModelAdmin):
    list_display = ('code_chapter', 'chapter_name')
    search_fields = ('chapter_name',)
    ordering = ['chapter_name']


admin.site.register(Member, MemberList)
admin.site.register(Chapter, ChapterList)

