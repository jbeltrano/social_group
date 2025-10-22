from django import template

register = template.Library()

@register.filter(name='format_duration')
def format_duration(time):
    if not time:
        return ''
    
    hours = time.hour
    minutes = time.minute
    
    if hours > 0:
        if minutes > 0:
            return f'{hours} hora{"s" if hours != 1 else ""} y {minutes} minuto{"s" if minutes != 1 else ""}'
        return f'{hours} hora{"s" if hours != 1 else ""}'
    elif minutes > 0:
        return f'{minutes} minuto{"s" if minutes != 1 else ""}'
    return ''