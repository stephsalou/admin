from django.contrib import admin
#-------Importation----------#
from . import models
from django.utils.safestring import mark_safe
from django_better_admin_arrayfield.admin.mixins import DynamicArrayMixin
from django_json_widget.widgets import JSONEditorWidget
from django.contrib.postgres.fields import JSONField
#-----------Register inline--------------#

class SousCategorieInline(admin.TabularInline):
    model =  models.SousCategorie
    #-------------le nombre d element a ajouter----------------#
    extra = 0





#------------register simple------------#

@admin.register(models.Categorie)
class CategorieAdmin(admin.ModelAdmin):
    inlines = [SousCategorieInline]
    list_display = (
        'view_image',
        'nom',
        'status',
        'date_add',
        'date_upd',
    )
    list_filter = (
        'status',
        'date_add',
        'date_upd',
    )
    
    #-------- fonction pour afficher une image dans l admin-----------------#
    def view_image(self,obj):
        
        return mark_safe('<img src="{img_url}" width="100px", heigth="100px"/>'.format(img_url=obj.image.url))
    def detail_image(self,obj):
        
        return mark_safe('<img src="{img_url}" width="100px", heigth="100px"/>'.format(img_url=obj.image.url))
    
    search_fields = ('nom',)
    date_hierarchy = 'date_add'
    #---------pour personnaliser les actions de l admin-------------#
    actions = (
        'active',
        'desactive',
    )
    #--------Pour rendre un element cliquable. tous les elements sauf standards ----------------#
    list_display_links = [
        'view_image',
        'nom',
        ]
    
    #--------------Pour afficher le nombre d element par Page---------------------#
    list_per_page = 3
    
    #------------- Ordonner par ordre alphabetique ---------------#
    ordering = [
        'nom',
    ]
    readonly_field = ['detail_image']
    
    def active(self,request,queryset):
        queryset.update(status=True)
        self.message_user(request,"la selection a ete activer avec succes")
    active.short_description = "Activer les Categorie selectionner"
    
    def desactive(self,request,queryset):
        queryset.update(status=False)
        self.message_user(request,"la selection a ete desactiver avec succes")
    desactive.short_description = "desactiver les Categorie selectionner"
    
    
@admin.register(models.SousCategorie)
class SousCategorieAdmin(admin.ModelAdmin):
    list_display = (
        'categorie',
        'nom',
        'status',
        'date_add',
        'date_upd',
        'view_image',
    )
    list_filter = (
        'status',
        'date_add',
        'date_upd',
        'categorie',
    )
    readonly_field = ['detail_image']
    
    search_fields = ('nom',)
    date_hierarchy = 'date_add'
    #---------pour personnaliser les actions de l admin-------------#
    actions = (
        'active',
        'desactive',
    )
    #--------Pour rendre un element cliquable. tous les elements sauf standards ----------------#
    list_display_links = [
        'view_image',
        'nom',
        ]
    
    #--------------Pour afficher le nombre d element par Page---------------------#
    list_per_page = 3
    
    #------------- Ordonner par ordre alphabetique ---------------#
    ordering = [
        'nom',
    ]
    #-------- fonction pour afficher une image dans l admin-----------------#
    def view_image(self,obj):
        
        return mark_safe('<img src="{img_url}" width="100px", heigth="100px"/>'.format(img_url=obj.image.url))
    
    def detail_image(self,obj):
        
        return mark_safe('<img src="{img_url}" width="100px", heigth="100px"/>'.format(img_url=obj.image.url))
    
    
    def active(self,request,queryset):
        queryset.update(status=True)
        self.message_user(request,"la selection a ete activer avec succes")
    active.short_description = "Activer les SousCategorie selectionner"
    
    def desactive(self,request,queryset):
        queryset.update(status=False)
        self.message_user(request,"la selection a ete desactiver avec succes")
    desactive.short_description = "desactiver les SousCategorie selectionner"
    
@admin.register(models.Produit)
class ProduitAdmin(admin.ModelAdmin,DynamicArrayMixin):
    list_display = (
        'sous_cat',
        'titre',
        'status',
        'date_add',
        'date_updt',
        'image',
        'view_image',
        'taille',
        'famille',
        'prix',
        'periode_promo',
        
    )
    list_filter = (
    'status',
    'date_add',
    'date_updt',
    'sous_cat',
    'tag',
    )
    formfield_overrides = {
        JSONField: {'widget': JSONEditorWidget},
    }
    def view_image(self,obj):
            
        return mark_safe('<img src="{img_url}" width="100px", heigth="100px"/>'.format(img_url=obj.image.url))
        
    def detail_image(self,obj):
            
        return mark_safe('<img src="{img_url}" width="100px", heigth="100px"/>'.format(img_url=obj.image.url))
    
    readonly_field = ['detail_image']
        
    search_fields = ('titre',)
    date_hierarchy = 'date_add'
    #---------pour personnaliser les actions de l admin-------------#
    actions = (
        'active',
        'desactive',
    )
    #--------Pour rendre un element cliquable. tous les elements sauf standards ----------------#
    list_display_links = [
        'view_image',
        'titre',
        ]
        
    #--------------Pour afficher le nombre d element par Page---------------------#
    list_per_page = 3
        
    #------------- Ordonner par ordre alphabetique ---------------#
    ordering = [
        'titre',
    ]
    fieldsets = [
        ('titre et visibilite',{'fields':['titre','status']}),
        ('description et image',{'fields':['description','image']}),
        ('tag et sous categorie',{'fields':['tag','sous_cat']}),
        ('taille ',{'fields':['taille','famille','prix','periode_promo']})
    ]
    filter_horizontal = ('tag',)
    
    #-------- fonction pour afficher une image dans l admin-----------------#
   
        
        
    def active(self,request,queryset):
        queryset.update(status=True)
        self.message_user(request,"la selection a ete activer avec succes")
    active.short_description = "Activer les SousCategorie selectionner"
        
    def desactive(self,request,queryset):
        queryset.update(status=False)
        self.message_user(request,"la selection a ete desactiver avec succes")
    desactive.short_description = "desactiver les SousCategorie selectionner"
    
@admin.register(models.Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = (
        'nom',
        'status',
        'date_add',
        'date_updt',
        
    )
    list_filter = (
    'status',
    'date_add',
    'date_updt',
    'nom',
    )

    
    readonly_field = ['detail_image']
            
    search_fields = ('nom',)
    date_hierarchy = 'date_add'
    #---------pour personnaliser les actions de l admin-------------#
    actions = (
        'active',
        'desactive',
    )
    #--------Pour rendre un element cliquable. tous les elements sauf standards ----------------#
    list_display_links = [
        'nom',
        ]
            
    #--------------Pour afficher le nombre d element par Page---------------------#
    list_per_page = 3
            
    #------------- Ordonner par ordre alphabetique ---------------#
    ordering = [
        'nom',
    ]
    #-------- fonction pour afficher une image dans l admin-----------------#
    
            
            
    def active(self,request,queryset):
        queryset.update(status=True)
        self.message_user(request,"la selection a ete activer avec succes")
    active.short_description = "Activer les SousCategorie selectionner"
            
    def desactive(self,request,queryset):
        queryset.update(status=False)
        self.message_user(request,"la selection a ete desactiver avec succes")
    desactive.short_description = "desactiver les SousCategorie selectionner"
