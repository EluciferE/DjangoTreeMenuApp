from django import template
from tree_menu.models import Menu, MenuBranch
from django.utils.html import format_html

register = template.Library()


@register.inclusion_tag('tree_menu/menu.html', takes_context=True)
def draw_menu(context, slug: str) -> dict:
    """
    draw tree menu

    :return: dict
    {
    'menus' : [{
            'name': name of menu,
            'children': [ids of branches that grows from menu],
            'branches': array of branches from menu
                        [ {
                            'name': branch name,
                            'parent': parent_branch_id or None,
                            'children': [array of children ids]
                        }, ...]
            },...],
    'target': id of target branch,
    'opened': [array of oppened branches],
    }
    """
    target_branch = context['request'].GET.get('target')

    menus = Menu.objects.filter(slug=slug)
    context = {'menus': []}

    for menu in menus:
        menu_context = {
            'name': menu.name,
            'children': [],
            'branches': {},
        }

        branches = MenuBranch.objects.filter(menu=menu)

        menu_context['branches'] = {
            branch.id: {
                'name': branch.name,
                'parent': getattr(branch.parent, 'id', None),
                'children': []
            } for branch in branches
        }

        for branch in branches:
            if branch.parent is None:
                menu_context['children'].append(branch.id)
            else:
                menu_context['branches'][branch.parent.id]['children'].append(branch.id)

        context['menus'].append(menu_context)

    if target_branch is None or not target_branch.isnumeric():
        return context

    target_branch = int(target_branch)

    target_menu = [menu for menu in context['menus'] if target_branch in menu['branches'].keys()]
    if len(target_menu) == 0:
        return context

    target_menu = target_menu[0]
    context['target'] = int(target_branch)
    context['opened'] = []

    while target_branch is not None:
        context['opened'].append(target_branch)
        target_branch = target_menu['branches'][target_branch]['parent']

    return context
