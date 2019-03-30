import urllib.request, urllib.parse, urllib.error
import oauth2 as oauth
import hidden


# https://apps.twitter.com/
# Create App and get the four strings, put them in hidden.py

def augment(url, post_body=None, http_method='GET', http_headers=None):
    secrets = hidden.oauth()
    consumer = oauth.Consumer(key=secrets['consumer_key'],
                              secret=secrets['consumer_secret'])
    token = oauth.Token(key=secrets['token_key'],
                        secret=secrets['token_secret'])
    client = oauth.Client(consumer, token)

    response, data = client.request(url,
                                    method=http_method)
    return data

    # oauth1
    # oauth_request = oauth.OAuthRequest.from_consumer_and_token(consumer,
    #                 token=token, http_method='GET', http_url=url,
    #                 parameters=parameters)
    # oauth_request.sign_request(oauth.OAuthSignatureMethod_HMAC_SHA1(),
    #                            consumer, token)
    # return oauth_request.to_url()
