import sys
import json
import requests

URL_API = 'http://smsmasking.ca/api.html'

def sendSMS(sender, number, message):
    message_data = {
        'sender' : sender,
        'number' : number,
        'message': message
    }
    response    = requests.post(url=URL_API, data=message_data)
    status_code = response.status_code
    if status_code == 200:
        print " {} to {}\n Message: {}".format(
            json.loads(response.text)['success'],
            number,
            message
        )
    else:
        print " Status Code: {}\n Info: {}".format(
            status_code,
            response.text
        )

if __name__ == '__main__':
    if len(sys.argv) != 4:
        print "\nUsage:"
        print "  python", __file__, "[sender] [number] [message]"
        print "Example:"
        print "  python", __file__, "'yourname' +62857xxxxxxxx 'Sample Message'\n"
        sys.exit()
    
    sendSMS(sys.argv[1], sys.argv[2], sys.argv[3])
