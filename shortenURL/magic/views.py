from django.shortcuts import render, redirect, get_object_or_404

from shortenURL.magic.utils import shorten_url
from shortenURL.magic.models import ShortenURL
from shortenURL.magic.forms import URLForm


DOMAIN = 'http://infinite-eyrie-9012.herokuapp.com/'


def welcome(request):
	return render(request, 'welcome.html')


def short(request):
	originURL = request.POST['originURL']
	# TODO check URL

	shortenURL = None

	# if originURL has already been in our database
	if ShortenURL.objects.filter(originURL=originURL).exists() == True:
		url = ShortenURL.objects.get(originURL=originURL)
		shortenURL = url.shortenURL
	
	# otherwise, shorten url
	else:
		r = False

		while True:
			shortenURL = DOMAIN + shorten_url(originURL, r)
			if ShortenURL.objects.filter(shortenURL=shortenURL).exists() == True:
				r = True
			else:
				newShortenURL = ShortenURL()
				newShortenURL.shortenURL = shortenURL
				newShortenURL.originURL = originURL
				newShortenURL.save()
				break 
	
	return render(request, 'success.html',
				  {'result': shortenURL
				  })


def recover(request, shortenURL):
	url = get_object_or_404(ShortenURL, shortenURL=shortenURL)
	return redirect(url.originURL)
