from .models import Menu


def get_menu(name: str = 'Hot') -> Menu | dict:
    try:
        return Menu.objects.get(name=name)
    except Menu.DoesNotExist:
        return {}
