import os
import sys
import time
import base64
import hashlib
import hmac
import requests
import json

def sens(title) :
    access_key = "2UTRrVslfLIOskouFwDP"
    secret_key = "F4UcJcrFNc26cHVHegUMAPaCWyNwNybddfEecGtO"
    uri = "/sms/v2/services/ncp:sms:kr:258199054509:sens/messages"
    hostDomain = "https://sens.apigw.ntruss.com"
    method = "POST"
    url = hostDomain + uri
    timestamp = int(time.time() * 1000)
    timestamp = str(timestamp)
    enctext = title

    # body값을 json 형태로 작성
    body = {}
    messages = {}

    messages["to"] = "01025369227"  #수신번호
    messages["content"] = enctext    #개별 메시지 내용

    body["type"] = "SMS"               #Type
    body["contentType"] = "COMM"        #COMM: 일반메시지
    body["countryCode"] = "82"          #국가번호
    body["from"] = "01025369227"        #발신번호
    body["content"] = "test messages"
    body["messages"] = [messages]   #messages 키 값으로 전체 호출


    # signature 함수 정의
    def	make_signature(timestamp, uri, access_key, secret_key, method):
    	secret_key = bytes(secret_key, 'UTF-8')
    	message = method + " " + uri + "\n" + timestamp + "\n" + access_key
    	message = bytes(message, 'UTF-8')
    	signingKey = base64.b64encode(hmac.new(secret_key, message, digestmod=hashlib.sha256).digest())
    	return signingKey


    # 헤더 부분 정의
    headers = {
        "x-ncp-apigw-timestamp": timestamp,
        "x-ncp-iam-access-key": access_key,
        "x-ncp-apigw-signature-v2": make_signature(timestamp, uri, access_key, secret_key, method),
        "Content-Type": "application/json"
    }

    # 데이터 값을 json 형식으로 호출
    response = requests.post(url,  data=json.dumps(body), headers=headers)
    rescode = response.status_code
    print(response)
    if(rescode==202):
        response_body = response.json
        print(response_body)
    else:
        print("Error Code:" + str(rescode))
