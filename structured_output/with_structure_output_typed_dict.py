# -------------------->not supported in new version<--------------------------------------------
from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from typing import TypedDict

load_dotenv()

# load model
model = ChatGoogleGenerativeAI(model='models/gemini-2.0-flash-exp')

# schema define
class Review(TypedDict):
    summary: str
    sentiment: str

# wrap model for structured output
structure_model = model.with_structured_output(Review)

# invoke model
result = structure_model.invoke(
    """
    Product Review:

    I recently purchased the Wireless Earbuds, and I’m really impressed. 
    The sound quality is crystal clear with deep bass, and the battery life easily lasts through the day. 
    The Bluetooth connection is stable, and pairing was seamless. 
    The design is lightweight and comfortable for long use. 
    Only downside is the case feels a little delicate, but overall it’s a great value for money.
    Highly recommended!
    """
)

print(result)
