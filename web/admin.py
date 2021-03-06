from django.contrib import admin

from .models import Page, Resource, Category, EmailTemplate, ResourceImage


class ResourceAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'post_status', 'event_type', 'contact', 'institution', 'year')
    readonly_fields = ('created', 'modified',)
    search_fields = ('post_id', 'title', 'country', 'contact', 'firstname', 'lastname', 'email', 'institution', 'link')
    list_filter = ('post_status', 'post_type', 'event_type', 'notified')

    save_as = True


class PageAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}
    change_form_template = 'web/admin/change_form.html'


class CategoryAdmin(admin.ModelAdmin):
    pass


class EmailTemplateAdmin(admin.ModelAdmin):
    pass


class ResourceImageAdmin(admin.ModelAdmin):
    pass


admin.site.register(Resource, ResourceAdmin)
admin.site.register(Page, PageAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(EmailTemplate, EmailTemplateAdmin)
admin.site.register(ResourceImage, ResourceImageAdmin)
