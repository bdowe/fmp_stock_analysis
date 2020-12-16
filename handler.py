import sys 
import os
import json

sys.path.append(os.path.abspath("./src"))
from stats import get_stats


def stats_lambda(event, context):
    request_data = event["queryStringParameters"]
    ticker = request_data["ticker"]
    return {
        "statusCode": 200,
        "body": get_stats(ticker).to_json(orient='records')
    }
