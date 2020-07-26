import urllib.request,json
from .models import Quote

base_url = None

def configure_request(app):
    global base_url

    base_url = app.config['RANDOM_QUOTE_URL']

def get_quote():
    '''
    Function that gets the json response to our url request
    '''
    with urllib.request.urlopen(base_url) as url:
        get_quote_data = url.read()
        quote_result = json.loads(get_quote_data)

        quote_object = None
        if quote_result:
            author = quote_result.get('author')
            quote = quote_result.get('quote')

            quotr_object = Quote(author,quote)
    
    return quote_object
        