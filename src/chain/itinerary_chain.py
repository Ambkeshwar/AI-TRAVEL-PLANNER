from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate
from src.config.config import GROQ_API_KEY

llm = ChatGroq(groq_api_key = GROQ_API_KEY,model="llama-3.3-70b-versatile",temperature = 0.3)

itinerary_prompt = ChatPromptTemplate([
    ("system" , "You are a helpful travel asssistant. Create a day trip itinerary for {city} based on user's interest : {interests}. Provide a brief , bulleted itineary"),
    ("human" , "Create a itinerary for my day trip")
])

def generate_itinerary(city:str , interests:list[str]) -> str:
    response = llm.invoke(
        itinerary_prompt.format_messages(city=city,interests=', '.join(interests))
    )

    return response.content