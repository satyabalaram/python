''' A true, old, and sordid tale of Python
    featuring raisins, pushy relatives, checkerboards,
    business cards, web pages, and getting much needed rest.
'''

import csv
import urllib

# Vcard format documented at: https://en.wikipedia.org/wiki/VCard

vcard_template = '''BEGIN:VCARD
VERSION:3.0
N:%s;%s
FN:%s %s
ORG:Raisins R Us, Inc.
TITLE:%s
TEL;TYPE=WORK,VOICE:%s
ADR;TYPE=WORK,PREF:;;100 Flat Grape Dr;Fresno;CA;95777;United States of Amer
 ica
EMAIL:%s
REV:2017-02-01T19:52:43Z
END:VCARD
'''

html_template = '''\
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="utf-8">
    <title> %(fname)s %(lname)s Contact Info </title>
</head>
<body>
<h1> Contact info for <em> %(fname)s %(lname)s </em> </h1>
<hr>
<ul>
   <li> Name: %(fname)s %(lname)s </li>
   <li> Title: %(title)s </li>
   <li> Phone: %(phone)s </li>
</ul>
</body>
</html>
'''

with open('notes/raisin_team_update.csv') as f:
    for lname, fname, title, email, phone in csv.reader(f):
        normalized_email = email.replace('@', '_at_').replace('.', '_dot_')

        vcard = vcard_template % (lname, fname, fname, lname, title, phone, email)
        filename = '%s.vcf' % normalized_email
        with open(filename, 'w') as vcard_file:
            vcard_file.write(vcard)
        print 'Wrote: ', filename

        html= html_template % dict(lname=lname, fname=fname, title=title, phone=phone)
        filename = '%s.html' % normalized_email
        with open(filename, 'w') as html_file:
            html_file.write(html)
        print 'Wrote: ', filename

        # QR Code from the Google Chart REST API documented at:
        # https://developers.google.com/chart/infographics/docs/qr_codes

        root_url = 'https://chart.googleapis.com/chart?'
        query = dict(cht='qr', chs='300x300', chl=vcard)
        url = root_url + urllib.urlencode(query)
        u = urllib.urlopen(url)
        image = u.read()
        # https://www.w3.org/TR/PNG/#5PNG-file-signature
        assert map(ord, image[:8]) == [137, 80, 78, 71, 13, 10, 26, 10]

        filename = '%s.png' % normalized_email
        with open(filename, 'wb') as image_file:
            image_file.write(image)
        print 'Wrote: ', filename

