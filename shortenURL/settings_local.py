from django.conf import settings

DEBUG = False
TEMPLATE_DEBUG = DEBUG

if DEBUG is not True:
	import dj_database_url
	DATABASES['default'] = dj_database_url.config()
