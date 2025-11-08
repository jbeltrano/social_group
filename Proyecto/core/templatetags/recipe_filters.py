from django import template

register = template.Library()

@register.filter(name='format_duration')
def format_duration(time):
    if not time:
        return ''

    horas = time.hour
    minutos = time.minute

    if horas > 0 and minutos > 0:
        return formato_horas_minutos(horas, minutos)

    if horas > 0:
        return formato_horas(horas)

    if minutos > 0:
        return formato_minutos(minutos)

    return ''


def formato_horas(horas):
    return f'{horas} hora{"s" if horas != 1 else ""}'


def formato_minutos(minutos):
    return f'{minutos} minuto{"s" if minutos != 1 else ""}'


def formato_horas_minutos(horas, minutos):
    return f'{formato_horas(horas)} y {formato_minutos(minutos)}'
