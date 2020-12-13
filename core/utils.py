import uuid

from django.utils.deconstruct import deconstructible


def change_name_files(filename):
    ext = filename.split('.')[-1]
    filename = "%s.%s" % (uuid.uuid4(), ext)
    return '{0}'.format(filename)


@deconstructible
class SetUniqueName(object):

    def __init__(self, path=''):
        self.path = path

    def __call__(self, _, filename):
        if self.path != '':
            return '{path}/{filename}'.format(path=self.path, filename=change_name_files(filename))
        return change_name_files(filename)


def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip

