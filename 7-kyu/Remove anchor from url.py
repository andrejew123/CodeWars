"""Complete the function/method so that it returns the url with anything after the anchor (#) removed.

Examples
# returns 'www.codewars.com'
remove_url_anchor('www.codewars.com#about')

# returns 'www.codewars.com?page=1'
remove_url_anchor('www.codewars.com?page=1') """


def remove_url_anchor(url):
    return url.partition("#")[0]


def remove_url_anchor_2(url):
    return url.split("#")[0]


assert remove_url_anchor("www.codewars.com#about") == "www.codewars.com"
assert remove_url_anchor("www.codewars.com/katas/?page=1#about") == "www.codewars.com/katas/?page=1"
assert remove_url_anchor("www.codewars.com/katas/") == "www.codewars.com/katas/"

assert remove_url_anchor_2("www.codewars.com#about") == "www.codewars.com"
assert remove_url_anchor_2("www.codewars.com/katas/?page=1#about") == "www.codewars.com/katas/?page=1"
assert remove_url_anchor_2("www.codewars.com/katas/") == "www.codewars.com/katas/"