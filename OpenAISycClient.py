# importing necessary functions from dotenv library
from dotenv import load_dotenv, dotenv_values 
# loading variables from .env file
load_dotenv() 

from baml_client.sync_client import b
from baml_client.types import Resume

def test_extract_resume():
    # Sample resume text
    sample_resume = """
    John Doe
    Software Engineer
    
    Experience:
    - Senior Developer at Tech Corp (2018-Present)
    - Software Engineer at StartupX (2015-2018)
    """
    
    try:
        # Make the API call using BAML
        response = b.ExtractResume(sample_resume)
        
        # Process the response
        print("Extracted Resume Data:", response)
        return response
        
    except Exception as e:
        print(f"Error during extraction: {str(e)}")
        return None

test_extract_resume()