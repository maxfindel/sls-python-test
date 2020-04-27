from aws_xray_sdk.core import xray_recorder
import json
import numpy as np


@xray_recorder.capture('big_array')
def big_array():
    a = np.arange(50000000).reshape(10000, 5000)
    return

def hello(event, context):
    body = {
        "message": "Go Serverless v1.0! Your function executed successfully!",
        "input": event
    }
    
    # Start an xray subsegment, because hte segment is already crreated automatically
    subsegment = xray_recorder.begin_subsegment('numpy_subsegment')
    
    # Create a random matrix using numpy and print it
    a = np.arange(50).reshape(10, 5)
    print("Your numpy array:")
    print(a)

    big_array()

    # Add metadata and annotations
    subsegment.put_annotation('event_key', 'numpy')
    subsegment.put_metadata('event-data', event, 'data-received')
    
    # Close the subsegment
    xray_recorder.end_subsegment()

    response = {
        "statusCode": 200,
        "body": json.dumps(body)
    }

    return response

if __name__ == "__main__":
    hello('', '')
