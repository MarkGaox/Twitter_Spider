import twurl
import json
import urllib

while True:
    TWITTER_URL = 'https://api.twitter.com/1.1/friends/list.json?'
    REMAIN_URl = 'https://api.twitter.com/1.1/application/rate_limit_status.json'
    print('')

    acct = input('Enter Twitter Account:')
    if len(acct) < 1:
        break



    param = {'screen_name': acct, 'count': '5'}
    TWITTER_URL += urllib.parse.urlencode(param)

    users_data = twurl.augment(TWITTER_URL, http_method='GET')
    remain_data = twurl.augment(REMAIN_URl)  # retrieve the remaining user data

    users_js = json.loads(users_data)  # parse users data
    remain_js = json.loads(remain_data)  # parse the rate limitation data

    # print(json.dumps(remain_js, indent=2))

    # let users know how many rate limitation left
    print('Remaining:', remain_js['resources']['friends']['/friends/list'])

    # print out all the users that follow the given account
    if 'errors' in users_js:
        print
        "API Error"
        print
        users_js['errors']
    else:
        for u in users_js['users']:
            print(u['screen_name'])
            if 'status' not in u:
                print('   * No status found')
                continue
            s = u['status']['text']
            print('  ', s[:50])
