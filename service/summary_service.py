import sys
from utils.api_endpoint import ApiEndpoint
from core.api_client import get_request

def get_summary():
    print("get summary service called", file=sys.stderr, flush=True)
    response = get_request(ApiEndpoint.SUMMARY, is_auth=True)
    if response.get("status") != "SUCCESS":
        raise Exception(response.get("message", "Failed to get summary"))
    return response.get("data")