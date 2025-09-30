
from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from typing import List, Optional, Annotated
from pydantic import BaseModel,Field
from typing_extensions import Literal

load_dotenv()

# load model
model = ChatGoogleGenerativeAI(model='models/gemini-2.0-flash-exp')

# schema define
class Review(BaseModel):
    summary: str = Field(..., description="Short summary of the review")
    sentiment: Literal["positive", "negative", "neutral"] = Field(..., description="Sentiment of the review")
    key_themes: List[str] = Field(..., description="Main themes or topics mentioned in the review")
    pros: Optional[List[str]] = Field(default=None, description="Positive aspects mentioned in the review")
    cons: Optional[List[str]] = Field(default=None, description="Negative aspects mentioned in the review")
    annotated: Optional[str] = Field(default=None, description="Structured and highlighted version of the review")


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
