from django import forms
from .models import MenuBranch


class MenuBranchForm(forms.ModelForm):
    class Meta:
        model = MenuBranch
        fields = "__all__"

    def __init__(self, *args, **kwargs):
        """
        Specify a queryset  for parent field
        Rules:
            1. You can't take yourself as a parent
            2. You can't take a child as your parent
            3. You can't take a parent from another menu
        """
        super().__init__(*args, **kwargs)

        if self.instance.pk is None:
            return

        queryset = MenuBranch.objects.exclude(pk=self.instance.pk).exclude(parent=self.instance)
        queryset = queryset.filter(menu__exact=self.instance.menu)

        self.fields["parent"].queryset = queryset
