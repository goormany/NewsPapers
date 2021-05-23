from django import template


register = template.Library()

bad_words = [
    'Test', 'test', 'bad', 'xxx', 'oloxa', 'test+'
]

@register.filter(name='censor_filter')
def censor_filter(value):
    x = value.lower()
    if ' ' in x:
        a = list(x.split(' '))
        for i in a:
            if i in bad_words:
                y = a.index(i)
                a.remove(i)
                a.insert(y, '***')
                value = (" ".join(a))
                return value

    if x in bad_words:
        x = '***'
        return x
    else:
        return x