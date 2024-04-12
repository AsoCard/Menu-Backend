from .models import Menu


def get_menu(pk: int = 1) -> Menu | dict:
    try:
        return Menu.objects.get(pk=pk)
    except Menu.DoesNotExist:
        return {}
