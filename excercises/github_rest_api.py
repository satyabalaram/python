'Goal: practice for accessing REST APIs'

import json
import urllib

def show_user_info(user):
    "Display a Github user's name, company and email"
    url = 'https://api.github.com/users/' + user
    u = urllib.urlopen(url)
    info = json.load(u)

    #print '%s works at %s. Contact at %s' %(info['name'],info['company'],info['email'])
    print '%(name)s works at %(company)s. Contact at %(email)s' %info

if __name__ == '__main__':

    show_user_info('raymondh')
    show_user_info('hugs')
