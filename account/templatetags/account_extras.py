from django import template

register = template.Library()

@register.filter(name='myInt')
def myInt(value):
    if value is not None:
        return int(value)
    return 0


@register.filter(name='myRange')
def myRange(value, arg):
    if arg is None:
        return False

    arr = arg.split(',')

    for l in arr:

        if int(l) == int(value):
            return True
    return False