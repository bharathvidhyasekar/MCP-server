import sys
from utils.api_endpoint import ApiEndpoint
from core.api_client import post_request, set_user_info, set_auth_token


def user_login(email: str, password: str):

    print("login service called", file=sys.stderr, flush=True)

    response = post_request(
        ApiEndpoint.LOGIN,
        {
            "email": email,
            "password": password
        },
        is_auth=False
    )

    if response.get("status") != "SUCCESS":
        raise Exception(response.get("message", "Login failed"))

    data = response["data"]

    access_token = data["accessToken"]
    user = data["user"]

    # store token
    set_auth_token(access_token)

    # store user info
    set_user_info(
        user["firstName"],
        user["id"],
        user["email"]
    )

    return f"Login successful for {user['email']}"