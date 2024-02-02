from django.shortcuts import redirect

def auth_temporary_products(get_response):
    # One-time configuration and initialization.
    def temporary_products(request):
        print(request.session.get('customer'))
        returnUrl = request.META['PATH_INFO']
        print(request.META['PATH_INFO'])
        if not request.session.get('customer'):
           return redirect(f'login?return_url={returnUrl}')

        response = get_response(request)
        return response

    return temporary_products