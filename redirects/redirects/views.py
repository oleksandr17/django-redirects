from random import choice

from django.http import HttpResponse
from django.shortcuts import redirect
from django.views.generic.base import RedirectView


def redirect_view(request):    
    ### Use response class
    # response = HttpResponse(status=302)
    # response['Location'] = '/redirect/success/'
    # return response

    ### Use response redirect class
    # return HttpResponseRedirect('/redirect/success/')

    ### Use model's `get_absolute_url()` method
    # product = Product.objects.filter(featured=True).first()
    # return redirect(product)

    ### Use url name
    # return redirect('redirect-success')

    ### Use url
    return redirect('/redirect-success/')


def redirect_success_view(request):
    return HttpResponse("Redirect success")


class SearchRedirectView(RedirectView):
    url = 'https://google.com/?q=%(term)s'


class RandomAnimalView(RedirectView):

    animal_urls = ['/dog/', '/cat/', '/parrot/']
    is_permanent = True

    def get_redirect_url(self, *args, **kwargs):
        return choice(self.animal_urls)
