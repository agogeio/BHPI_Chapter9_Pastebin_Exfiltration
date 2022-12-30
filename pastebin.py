import os   
import requests

from dotenv import load_dotenv

#? pastebin API documentation 
#? https://pastebin.com/doc_api

load_dotenv()
PASTEBIN_USERNAME = os.getenv('PASTEBIN_USERNAME')
PASTEBIN_PASSWORD = os.getenv('PASTEBIN_PASSWORD')
PASTEBIN_API_KEY = os.getenv('PASTEBIN_API_KEY')

def paste(title, content) -> tuple:
    PASTEBIN_LOGIN_URL = 'https://pastebin.com/api/api_login.php'
    PASTEBIN_POST_URL = 'https://pastebin.com/api/api_post.php'
    #* Creating An 'api_user_key' Using The API Member Login System
    #* https://pastebin.com/doc_api#9
    PASTEBIN_LOGIN_DATA = {
        'api_dev_key' : PASTEBIN_API_KEY,
        #? Not full email address just name
        'api_user_name' : PASTEBIN_USERNAME, 
        'api_user_password' : PASTEBIN_PASSWORD
    }

    pb_response_user_key = requests.post(PASTEBIN_LOGIN_URL, data=PASTEBIN_LOGIN_DATA)

    print(pb_response_user_key.text)
    api_user_key = pb_response_user_key.text
    
    pb_paste_data ={
        'api_dev_key' : PASTEBIN_API_KEY,
        'api_user_key' : api_user_key,
        'api_option' : 'paste',
        'api_paste_private' : 0,
        #* api_paste_name - this will be the name / title of your paste.
        'api_paste_name' : title,
        #* api_paste_code - this is the text that will be written inside your paste.
        'api_paste_code' : content
    }

    pb_paste_response = requests.post(PASTEBIN_POST_URL, data=pb_paste_data)
    
    print(pb_paste_response.status_code)
    print(pb_paste_response.text)

    if pb_paste_response.status_code == 200:
        return (True, pb_paste_response.text)
    else:
        return (False, pb_paste_response.text)

#  paste('Sample agogeio Title', b'Sample agogeio Content')