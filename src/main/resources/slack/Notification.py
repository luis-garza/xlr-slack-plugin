#
# THIS CODE AND INFORMATION ARE PROVIDED "AS IS" WITHOUT WARRANTY OF ANY KIND, EITHER EXPRESSED OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE IMPLIED WARRANTIES OF MERCHANTABILITY AND/OR FITNESS
# FOR A PARTICULAR PURPOSE. THIS CODE AND INFORMATION ARE NOT SUPPORTED BY XEBIALABS.
#

import json
import urllib2


def printData(url, data):
    print
    print 'URL:'
    print '```'
    print url
    print '```'
    print 'Data:'
    print '```'
    print data
    print '```'

# Initialize variables & check parameters
response = ''
url = server['url']
user = server['userName']
icon = server['userIcon']
proxyUrl = server['proxyUrl']
if not url.strip():
    print 'Error!'
    print 'Server configuration url undefined\n'
    sys.exit(100)
if not user.strip():
    print 'Error!'
    print 'Server configuration user name undefined\n'
    sys.exit(100)
if not icon.strip():
    print 'Error!'
    print 'Server configuration user icon undefined\n'
    sys.exit(100)
if not channel.strip():
    print 'Error!'
    print 'Parameter channel undefined\n'
    sys.exit(200)
if not message.strip():
    print 'Error!'
    print 'Parameter message undefined\n'
    sys.exit(200)

# Set up proxy
# proxyUrl format: 'http:// username:password@proxyurl:proxyport'
if proxyUrl:
    proxy = urllib2.ProxyHandler({'http': proxyUrl.strip(), 'https': proxyUrl.strip()})
    auth = urllib2.HTTPBasicAuthHandler()
    opener = urllib2.build_opener(proxy, auth, urllib2.HTTPHandler)
    urllib2.install_opener(opener)

# Call Slack Incoming WebHook
try:
    request = urllib2.Request(url)
    request.add_header('Content-Type', 'application/json')
    postdata = {'channel': channel.strip(), 'username': user.strip(), 'icon_emoji': icon.strip(), 'text': message.strip()}
    data = json.dumps(postdata)
    response = urllib2.urlopen(request, data)
except urllib2.HTTPError as error:
    print 'HTTP %s error!' % error.code
    print 'Reason: %s' % error.read()
    printData(url, data)
    sys.exit(300)
except urllib2.URLError as error:
    print 'Network error!'
    print 'Reason: %s' % error.reason
    printData(url, data)
    sys.exit(400)

# Print output
print 'Slack message to channel %s sent successfully' % channel
print '```'
print message
print '```'
sys.exit(0)
