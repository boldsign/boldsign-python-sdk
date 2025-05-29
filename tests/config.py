import os

API_KEY = os.getenv('API_KEY')
BASE_URL = os.getenv('HOST_URL')

# How to section to add an API key and Base url in environmental variables
    # 1. Generate an API key through your Bold Sign account.
    # 2. Select the search bar on the taskbar and search for 'Edit environmental variables for your account'.
    # 3. Add the API key and URL to 'API_KEY' and 'HOST_URL' respectively.
    # 4. Once the API key and URL are added, restart your application and then run the test cases.

# If you use your own API key in environmental variables kindly follow theses steps:
    # 1. Activate SMS option while sending document to SMS OTP
    # 2. Approved sender identity person for while sending on behalf document use the approve mail id in approved onbehalf email 
    # 3. While executing testcases mostly use Enterprise API plan and Live API key.