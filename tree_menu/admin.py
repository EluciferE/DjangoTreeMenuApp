from django.contrib import admin
from django.contrib.auth.models import User, Group
from django.core.exceptions import ValidationError
from .models import Menu, MenuBranch
from .forms import MenuBranchForm


class MenuBranchInline(admin.StackedInline):
    model = MenuBranch
    extra = 0
    fields = (('name', 'parent'),)
    form = MenuBranchForm


class MenuAdmin(admin.ModelAdmin):
    inlines = (MenuBranchInline,)

    def save_formset(self, request, form, formset, change):
        """
        Avoid circular relationship in MenuBranch
        """
        relations = {}
        for f in formset.forms:
            obj = f.instance
            if obj.id is None or obj.parent is None:
                continue

            relations[obj.id] = obj.parent.id

            if relations.get(obj.parent.id) == obj.id:
                obj.parent = None

        super().save_formset(request, form, formset, change)


class MenuBranchAdmin(admin.ModelAdmin):
    form = MenuBranchForm


# Unregister useless models
admin.site.unregister(User)
admin.site.unregister(Group)

# Register my project models
admin.site.register(Menu, MenuAdmin)
admin.site.register(MenuBranch, MenuBranchAdmin)
