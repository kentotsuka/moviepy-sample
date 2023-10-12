from dotenv import load_dotenv
load_dotenv()
import os

PROFILE_NAME = os.getenv('PROFILE_NAME')
BUCKET_NAME = os.getenv('BUCKET_NAME')