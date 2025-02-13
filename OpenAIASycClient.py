import asyncio
from baml_client.async_client import b
from baml_client.types import Resume
from openai import OpenAI, AsyncOpenAI
import os
# importing necessary functions from dotenv library
from dotenv import load_dotenv, dotenv_values 
# loading variables from .env file
load_dotenv() 
# For asynchronous usage
async_client = AsyncOpenAI(
    api_key=os.getenv("OPENAI_API_KEY")
)
async def test_extract_resume_async():
    # Sample resume text
    sample_resume = """
    John Doe
    Software Engineer
    
    Experience:
    - Senior Developer at Tech Corp (2018-Present)
    - Software Engineer at StartupX (2015-2018)
    """
    
    try:
        # Make the async API call using BAML
        response = await b.ExtractResume(sample_resume)
        
        # Process the response
        print("Extracted Resume Data:", response)
        return response
        
    except Exception as e:
        print(f"Error during extraction: {str(e)}")
        return None

# Run the async test
if __name__ == "__main__":
    asyncio.run(test_extract_resume_async())