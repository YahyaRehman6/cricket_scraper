from django.contrib.admin.models import LogEntry, ADDITION, CHANGE, DELETION
from django.contrib.contenttypes.models import ContentType
from django.contrib.auth.models import User

def log_entry(action_flag=ADDITION, content_type_id=None, object_id=None, object_repr='', message=''):
    user = User.objects.all().first()
    print("user is : ", user)
    LogEntry.objects.create(
        user_id=user.id,
        content_type_id=content_type_id,
        object_id=object_id,
        object_repr=object_repr,
        action_flag=action_flag,
        change_message=message,
    )