from django.contrib import admin
from . import models


# Register your models here.

# 查询界面设置
class bookadmin(admin.ModelAdmin):
    # 将出版日期作为导航查询字段
    date_hierarchy = 'publishdate'
    # 设置字段无值时显示的内容
    empty_value_display = '-None-'
    # 设置author字段的选择方式为水平扩展选择
    # fields=('title','descript','publishdate','publishing','author')
    filter_horizontal = ('author',)
    # 以下代码在页面上对字段进行分组显示或布局
    fieldsets = (
        (
            '图书信息',
            {'fields': (('title', 'publishdate'), 'publishing', 'author')}),
        (
            '图书简介',
            {'classes': ('collapse',), 'fields': ('descript',)}),)  # collapse: 图书简介(显示)

    def descript_str(self, obj):  # 自定义一个字段
        return obj.descript[:20]  # 对字段进行切片，取前20个字符

    descript_str.short_description = '简介'  # 定义字段名字
    list_filter = ('title', 'publishing', 'author')  # 设置右侧过滤导航字段
    search_fields = ('title', 'publishing__name', 'author__name')  # 设置上方查询的字段
    list_display = ('title', 'descript_str', 'publishdate', 'publishing',)  # 中间列表显示字段
    show_full_result_count = True  # 显示查询到记录数
    list_per_page = 6  # 设定每页显示6条记录

    def change_publishing(self, request, queryset):
        publishing_obj = models.publishing.objects.get(name='机械工业出版社')
        rows = queryset.update(publishing=publishing_obj)
        self.message_user(request, '%s 条记录被修改成“机械工业出版社”' % rows)

    change_publishing.short_description = '选中记录出版社改为“机械工业出版社”'
    actions = ['change_publishing']


admin.site.register(models.book, bookadmin)


class publishingadmin(admin.ModelAdmin):
    list_display = ('name', 'address')
    list_editable = ('address',)
    list_per_page = 10


admin.site.register(models.publishing, publishingadmin)

from django.utils.html import format_html
from django.utils.safestring import mark_safe


class authoradmin(admin.ModelAdmin):
    def header_data(self, obj):  # 定义一字段，使图像带有HTML格式并显示
        return mark_safe(u'<img src="/media/%s" width="50px"  height="30px"/>' % obj.header)  # 防止HTML代码被转义，我们用mark_safe

    header_data.short_description = '简介'  # 定义字段名字
    list_display = ('name', 'email', 'birthday', 'header_data')
    list_per_page = 10


admin.site.register(models.author, authoradmin)

# 修改标题
admin.site.site_header = "图书信息管理系统"
