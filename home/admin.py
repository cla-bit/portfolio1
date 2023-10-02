from django.contrib import admin
from .models import Project, Category, Contact, Portfolio, Skill

# Register your models here.


@admin.register(Skill)
class SkillsInline(admin.ModelAdmin):
    list_display = ['skill']


@admin.register(Portfolio)
class PortfolioAdmin(admin.ModelAdmin):
    list_display = ['user', 'resume']
    filter_horizontal = ['skills']


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ['name', 'category']
    prepopulated_fields = {'slug': ('name',)}


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name']
    prepopulated_fields = {'slug': ('name',)}


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ['name', 'email']
