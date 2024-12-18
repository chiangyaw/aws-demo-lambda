import os
import socket

def lambda_handler(event, context):
    try:
        addr1 = socket.gethostbyname('www.google.com')
    except PermissionError:
        addr1 = "Cannot get Google"
    
    try:
        addr2 = socket.gethostbyname('www.yahoo.com')
    except PermissionError:
        addr2 = "Cannot get Yahoo"
        
    addr = "www.google.com : " + addr1 + "<br>" + "www.yahoo.com : " + addr2
    
    response = "<html><body><h1>" + addr +"</h1></body></html>"
    return {
        'statusCode': 200,
        'body': response,
        'headers': {
            'Content-Type': 'text/html',
        }
    }