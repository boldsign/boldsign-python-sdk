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
    
    create_user = [
        boldsign.CreateUser(
            emailId= "luthercooper@cubeflakes.com",
            teamId="0274212c-cf83-4f99-9c8f-6791f90f4386",
            userRole="Admin",
            metaData=
            {
                "Employee": "Permanent",
                "Department": "Sales",
                "Designation": "Sales Manager"
            }
                
        )
    ]
    
    create_user_response = user_api.create_user(
        create_user=create_user
    )
    
    print(f"User successfully created")