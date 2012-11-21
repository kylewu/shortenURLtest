from django.shortcuts import render, redirect, get_object_or_404
from django.core.validators import URLValidator
from django.core.exceptions import ValidationError


from shortenURL.magic.utils import shorten_url
from shortenURL.magic.models import ShortenURL


DOMAIN = 'http://infinite-eyrie-9012.herokuapp.com/'


def welcome(request):
    return render(request, 'welcome.html')


def short(request):
    if 'originURL' not in request.POST:
        return redirect('/')

    originURL = request.POST['originURL']
    # check URL
    val = URLValidator(verify_exists=False)
    try:
        val(originURL)
    except ValidationError, e:
        print e
        return render(request, 'welcome.html', {
                      'url_error': 'error'
                      })

    shortenURL = None

    # if originURL has already been in our database
    if ShortenURL.objects.filter(originURL=originURL).exists() == True:
        url = ShortenURL.objects.get(originURL=originURL)
        shortenURL = DOMAIN + url.shortenURL
    
    # otherwise, shorten url
    else:
        r = False

        while True:
            shortenURL = shorten_url(originURL, r)
            if ShortenURL.objects.filter(shortenURL=shortenURL).exists() == True:
                r = True
            else:
                newShortenURL = ShortenURL()
                newShortenURL.shortenURL = shortenURL
                newShortenURL.originURL = originURL
                newShortenURL.save()
                shortenURL = DOMAIN + shortenURL
                break 
    
    return render(request, 'success.html',
                  {'result': shortenURL
                  })


def recover(request, shortenURL):
    url = get_object_or_404(ShortenURL, shortenURL=shortenURL)
    return redirect(url.originURL)
