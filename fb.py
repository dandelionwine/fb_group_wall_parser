import facebook
import sql
import re


# Access token. Get one at https://developers.facebook.com/tools/explorer/
access_token = 'CAACEdEose0cBAFXKLJ2ogcPl1R8HET42HWjxWCCZA9S2ZBPvuhwW9gBDbX1xZCS5N38sZBiHQWEQIrc9KYKSIzZAljzAYzLndvoc8vOXn8uleeeVhHZAk9rppqcsmZAZBXp6UagwMHa0DIKjco6ZBytGo0wN0mtdeGmui5NTGZAqsRMVoy8ixkN4So2QdfmHS29F5OgSmPNE0tYwZDZD'
# Access my facebook account
graph = facebook.GraphAPI(access_token)

# This is the list of group ids that the program iterates over
group_ids = ["275895952527834", "1577441379149696", "560944294052181", "126278657527255", "369867503068226", "259894394042181", "215918835174776", "1599209366987554", "481697411926010", "364010093781688", "262444607263839", "623206594363552", "135486133130440", "29851114873", "241846582600572", "270558336379692", "204725947524", "408662892547848", "311509740857", "403268663033544", "210773429046471", "298148543640176", "1472740936287551", "160775681779", "157960580960255", "205686289555465", "177830275661611"]

def search_rsps(group_id):
    posts = graph.get_connections(group_id, "feed")
    for group_id in posts['data']:  # Take each post, which is a dict
        try:
            p = re.compile("exchange|swap*")
            if p.findall(group_id['message']):
                sql.add_entry(group_id['from']['id'], group_id['from']['name'], group_id['link'], 2, group_id['updated_time'], group_id['message'])
        except KeyError:
            pass

def check_fb(group_id):
    posts = graph.get_connections(group_id, "feed")
    for group_id in posts['data']:  # Take each post, which is a dict
        try:
            if "free" in group_id['message']:
                sql.add_entry(group_id['from']['id'], group_id['from']['name'], group_id['link'], 2, group_id['updated_time'], group_id['message'])
        except KeyError:
            pass

def check_photo(link):
    try:
        photo_id = re.findall('(?<=fbid=)[0-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9]', link)
        data = graph.get_object(photo_id[0])
    except KeyError:
        pass
    try:
        return re.search("(?P<url>https?://[^\s]+)", data['name']).group("url")
    except KeyError:
        return False


def find_facebook(item):
    if re.findall("facebook", item) == ['facebook']:
        return True
    else:
        return False
