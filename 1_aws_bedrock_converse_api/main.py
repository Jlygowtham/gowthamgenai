import os
import boto3
from dotenv import load_dotenv

load_dotenv()

bedrock = boto3.client(
 "bedrock-runtime",
 region_name=os.getenv("AWS_REGION"),
 aws_access_key_id=os.getenv("AWS_ACCESS_KEY"),
 aws_secret_access_key=os.getenv("AWS_SECRET_KEY"))

response = bedrock.converse(
  modelId=os.getenv("MODEL_ID"),
  messages=[
  {
   "role": "user", 
   "content": [{"text": "What is Amazon Bedrock?"}]
  } ],
  inferenceConfig={ 
   "maxTokens": 1024,
   "temperature": 0.7} 
)

print(response["output"]["message"]["content"][0]["text"])
