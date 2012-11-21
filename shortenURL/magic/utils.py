import hashlib, random


def shorten_url(originURL, r=None):
	# TODO do not use hex here
	# it's better to use 0-9 and a-z
	factor = str(random.random()) if r else ''

	return hashlib.md5(originURL + factor).hexdigest()[:8]
