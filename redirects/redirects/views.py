from django.http import HttpResponse
from django.shortcuts import redirect


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
