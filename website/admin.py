from django.contrib import admin
from . import models
from django.utils.safestring import mark_safe

@admin.register(models.About)
class AboutAdmin(admin.ModelAdmin):
    list_display  = ('titre','description','date_add','date_update','status','image_view')
    list_filter = ('date_add','date_update','status')
    search_fields = ('titre',)
    date_hierarchy = 'date_add'
    list_display_links = ['titre']
    fieldsets = [
          ('About_info', {'fields':['titre', 'description','image']}),
          ('standard', {'fields':['status']}),
          ]
    def image_view(self,obj):
        return mark_safe("<img src='{url}' width='100px',height='50px'>".format(url=obj.image.url))

    actions = ('active','desactive')
    def active(self, request, queryset):
        queryset.update(status=True)
        self.message_user(request, 'La selection a été activé avec succès')
    active.short_description = 'activer'
        
    def desactive(self, request, queryset):
        queryset.update(status=False)
        self.message_user(request, 'La selection a été desactivé avec succès')
    desactive.short_description = 'desactiver'

@admin.register(models.Siteinfo)
class SiteinfoAdmin(admin.ModelAdmin):
    list_display  = ('slogan','date_add','date_update','status','logo_H_view')
    list_filter = ('date_add','date_update','status')
    date_hierarchy = 'date_add'
    fieldsets = [
          ('Siteinfo_info', {'fields':['slogan','logo_H']}),
          ('standard', {'fields':['status']}),
          ]
    def logo_H_view(self,obj):
        return mark_safe("<img src='{url}' width='100px',height='50px'>".format(url=obj.logo_H.url))

    
    actions = ('active','desactive')
    def active(self, request, queryset):
        queryset.update(status=True)
        self.message_user(request, 'La selection a été activé avec succès')
    active.short_description = 'activer'
        
    def desactive(self, request, queryset):
        queryset.update(status=False)
        self.message_user(request, 'La selection a été desactivé avec succès')
    desactive.short_description = 'desactiver'

@admin.register(models.Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display  = ('nom','email','subject','message','date_add','date_update','status')
    list_filter = ('date_add','date_update','status')
    search_fields = ('nom',)
    date_hierarchy = 'date_add'
    list_display_links = ['nom']
    fieldsets = [
          ('Contact_info', {'fields':['nom', 'email','subject','message']}),
          ('standard', {'fields':['status']}),
          ]

    actions = ('active','desactive')
    def active(self, request, queryset):
        queryset.update(status=True)
        self.message_user(request, 'La selection a été activé avec succès')
    active.short_description = 'activer'
        
    def desactive(self, request, queryset):
        queryset.update(status=False)
        self.message_user(request, 'La selection a été desactivé avec succès')
    desactive.short_description = 'desactiver'

@admin.register(models.Reseau_social)
class Reseau_socialAdmin(admin.ModelAdmin):
    list_display  = ('nom','lien','icone','date_add','date_update','status')
    list_filter = ('date_add','date_update','status')
    search_fields = ('nom',)
    date_hierarchy = 'date_add'
    list_display_links = ['nom']
    fieldsets = [
          ('Reseau_info', {'fields':['nom', 'lien','icone']}),
          ('standard', {'fields':['status']}),
          ]
    actions = ('active','desactive')
    def active(self, request, queryset):
        queryset.update(status=True)
        self.message_user(request, 'La selection a été activé avec succès')
    active.short_description = 'activer'
        
    def desactive(self, request, queryset):
        queryset.update(status=False)
        self.message_user(request, 'La selection a été desactivé avec succès')
    desactive.short_description = 'desactiver'

@admin.register(models.Newletter)
class NewletterAdmin(admin.ModelAdmin):
    list_display  = ('nom','email','date_add','date_update','status')
    list_filter = ('date_add','date_update','status')
    search_fields = ('nom',)
    date_hierarchy = 'date_add'
    list_display_links = ['nom']

    fieldsets = [
          ('Newletter_info', {'fields':['nom', 'email']}),
          ('standard', {'fields':['status']}),
          ]
    actions = ('active','desactive')
    def active(self, request, queryset):
        queryset.update(status=True)
        self.message_user(request, 'La selection a été activé avec succès')
    active.short_description = 'activer'
        
    def desactive(self, request, queryset):
        queryset.update(status=False)
        self.message_user(request, 'La selection a été desactivé avec succès')
    desactive.short_description = 'desactiver'

