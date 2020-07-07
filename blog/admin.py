from django.contrib import admin
from . import models
from django.utils.safestring import mark_safe

# Register your models here.

@admin.register(models.Categorie)
class CategorieAdmin(admin.ModelAdmin):
    list_display  = ('nom','date_add','date_update','status')
    list_filter = ('date_add','date_update','status')
    search_fields = ('nom',)
    fieldsets = [
            ('Categorie_info', {'fields':['nom']}),
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

@admin.register(models.Tag)
class TagAdmin(admin.ModelAdmin):
    list_display  = ('nom','date_add','date_update','status')
    list_filter = ('date_add','date_update','status')
    search_fields = ('nom',)
    fieldsets = [
            ('Tag_info', {'fields':['nom']}),
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

@admin.register(models.Lieu)
class LieuAdmin(admin.ModelAdmin):
    list_display  = ('ville','description','telephone','adresse','email','date_add','date_update','status','marp_url')
    list_filter = ('date_add','date_update','status')
    search_fields = ('nom',)
    fieldsets = [
            ('Lieu_info', {'fields':['ville','description','telephone','adresse','email','marp_url']}),
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

@admin.register(models.Event)
class EventAdmin(admin.ModelAdmin):
    list_display  = ('titre','lieu','date_start','date_end','prix','organisateurs','speackers','categorie','date_add','date_update','status','image_view')
    list_filter = ('date_add','date_update','status','lieu','categorie','tags')
    search_fields = ('titre',)
    date_hierarchy = 'date_add'
    list_display_links = ['titre']
    fieldsets = [
          ('Event_info', {'fields':['titre', 'description','date_start','date_end','prix','organisateurs','speackers','categorie','lieu','tags','image']}),
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
    
@admin.register(models.Partner)
class PartnerAdmin(admin.ModelAdmin):
    list_display  = ('nom','lien','date_add','date_update','status','image_view')
    list_filter = ('date_add','date_update','status')
    search_fields = ('nom',)
    date_hierarchy = 'date_add'
    list_display_links = ['nom']
    fieldsets = [
          ('Partner_info', {'fields':['nom','lien','image']}),
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

    @admin.register(models.New)
    class NewAdmin(admin.ModelAdmin):
        list_display = ('titre','slug', 'description','event','date_add','date_update','status','image_view')
        list_filter = ('date_add','date_update','status','event',)
        search_fields = ('titre',)
        date_hierarchy = 'date_add'
        list_display_links = ['titre']
        fieldsets = [
            ('New_info', {'fields':['titre','description','event','image']}),
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