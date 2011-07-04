from django import template
from django.contrib.auth.models import User
from django_pm.models import *

register = template.Library()

class MessageNode(template.Node):
    def __init__(self, username):
        self.username = template.Variable(username)

    def render(self, context):
        try:
            username = self.username.resolve(context)
        except template.VariableDoesNotExist:
            return ''

        user = User.objects.get(username=username)
        
        count = user.message_set.filter(is_unread=True).count()

        return count

@register.tag
def message_count(parser, token):
    try:
        tag_name, user = token.split_contents()
    except ValueError:
        raise template.TemplateSyntaxError, "%r tag requires a single argument" % token.contents.split()[0]

    return MessageNode(user)
