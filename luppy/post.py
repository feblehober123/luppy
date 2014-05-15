import luppy
import re
import base64

#This will interact with tinyboard's posting script
def post(board=None, thread=None, name=None, email=None, subject=None, body=None, file=None, spoiler_image=None, embed=None):
    if (len(name) > 35):
        raise ValueError('Name longer than max of 35 chars.')
    if len(email) > 40):
        raise ValueError('Email longer than max of 40 chars.')
    if len(subject) > 100):
        raise ValueError('Subject longer than max of 100 chars.')
    if type(spoiler_image) != bool:
        raise ValueError('spoiler_image must be type bool.')
    if len(embed) > 120:
        raise ValueError('Embed URL longer than max of 120 chars.')
    #Done with var checks, now logical posting checks and adding to the post data
    
    post_data = {'json_response':True}
    
    if board==None:
        raise ValueError('Cannot post: no board selected.')
    post_data['board'] = board
    
    if thread==None and file_url==None:
        raise ValueError('Cannot post: no thread selected and no image selected to create an OP with.')
    if email:
        post_data['email'] = email
    if subject:
        post_data['subject'] = subject
    if body:
        post_data['body'] = body
    #validates image file
    try:
        with open(file, 'rb') as f:
            img = base64.b64encode(f.read())
            post_data['file'] = img
    except IOError:
        raise ValueError('Cannot post: Specified file does not exist')
    if spoiler_image:
        if not(file):
            raise ValueError('Cannot post: Cannot spoiler nonexistant image.')
    if embed:
        post_data['embed'] = embed
    #add more as I convince nanasi to enable things, especially upload from url
    r = request.post(fourch.urls['post'], data=post_data)
    #validate response? nah.
