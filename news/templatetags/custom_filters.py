from django import template


register = template.Library()

bad_words = [
    'Test', 'test', 'bad', 'xxx', 'oloxa',
]

@register.filter(name='censor_filter')
def censor_filter(value):
    for i in bad_words:
        value = value.lower()
        value = value.replace(i, '***')
    return value