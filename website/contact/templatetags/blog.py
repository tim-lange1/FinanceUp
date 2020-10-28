from django import template

register = template.Library()

@register.inclusion_tag('contact/partials/blog_post.html')
def blog_post(post):
    return {'post': post, 'willkommen': 'Moin bimsknzn'}

@register.filter
def to_uppercase(var):
    print(var)
    return var.upper()