from django.conf import settings

DEBUG = True
TEMPLATE_DEBUG = DEBUG

if DEBUG is not True:
	import dj_database_url
	settings.DATABASES['default'] = dj_database_url.config()