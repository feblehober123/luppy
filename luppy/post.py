import fourch
import re

#This will interact with tinyboard's posting script
def post(name=None, email=None, subject=None, body=None, file_url=None, spoiler_image=None, embed=None):
    if (len(name) > 35):
        raise ValueError('Name longer than max of 25 chars.')
    if len(email) > 40):
        raise ValueError('Email longer than max of 40 chars.')
    if len(subject) > 100):
        raise ValueError('Subject longer than max of 100 chars.')
    if type(spoiler_image) != bool:
        raise ValueError('spoiler_image must be type bool.')
    if len(embed) > 120:
        raise ValueError('Embed URL longer than max of 120 chars.')
    
    #this line should make the url filename safe, may need debugging
    safe_file_url = re.match(r'(?:\w*://)?(?:.*\.)?([a-zA-Z-1-9]*\.[a-zA-Z]{1,}).*', file_url.translate(None, '/').groups()[0]
    with open('./images/'+safe_file_url) as img:
        #upload it and shig, i can't do this now
    except IOError:
        #downlaod the file then upload it, I gotta go
        
