from dotenv import load_dotenv
import os

load_dotenv()

class Config:
    OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')
    MAX_RETRIES = 3
    RATE_LIMIT = 10  # requests per minute
    IMAGE_MAX_SIZE = (800, 800)
    IMAGE_QUALITY = 85 