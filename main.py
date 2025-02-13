# Synchronous usage
from baml_client.sync_client import b
from baml_client.types import Resume

def example(raw_resume: str) -> Resume:
    response = b.ExtractResume(raw_resume)
    return response

# Asynchronous usage
from baml_client.async_client import b
from baml_client.types import Resume

async def example(raw_resume: str) -> Resume:
    response = await b.ExtractResume(raw_resume)
    return response
