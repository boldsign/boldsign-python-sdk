import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import boldsign

configuration = boldsign.Configuration(
    api_key = os.getenv('BoldSignAPIKey'),
    host=os.getenv('BoldSignApiUrl')
)

with boldsign.ApiClient(configuration) as api_client:
    
    user_api = boldsign.UserApi(api_client)
    
    user_list_response = user_api.list_users(
        page_size=10, page=1
    )
    
    for users in user_list_response.result:
        if users.email == "prakash.viswanathan+sdk+926@syncfusion.com":
            print("TestUserID:"+users.user_id)
    
    # print(f"User list:{user_list_response.result}")