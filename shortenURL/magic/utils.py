import hashlib, random, string


# generate one random secret code every time
# 1. because we query database every time 
#    we want to decode a shorten URL
#    so there is no need to have a fixed code
# 2. I only use the first 16 char in this code
#    because hex only contains 0-9a-f
# 3. The problem of this method is that if our 
#    server restarts, Link A will get a new shorten
#    URL because CODE is chaged.
CODE = list(string.ascii_letters + string.digits + 'z')
random.shuffle(CODE)


def shorten_url(originURL, r=None):

    factor = str(random.random()) if r else ''

    url = hashlib.md5(originURL + factor).hexdigest()[:8]

    return ''.join([CODE[int(x, 16)] for x in url])
