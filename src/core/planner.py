from langchain_core.messages import HumanMessage,AIMessage
from src.chain.itinerary_chain import generate_itinerary
from src.utils.logger import get_logger
from src.utils.custom_exception import CustomException

logger = get_logger(__name__)

class TravelPlanner:
    def __init__(self):
        self.messages = []
        self.city = ""
        self.interests = []
        self.itinerary = ""

        logger.info("Initialized TravelPlanner instance")

    def set_city(self,city:str):
        try:
            self.city = city
            self.messages.append(HumanMessage(content=city))
            logger.info("City set Successfully!")
        except Exception as e:
            logger.error(f"Error while setting city: {str(e)}")
            raise CustomException("Failed to set city", str(e))
        
    def set_interests(self, interests_str:str):
        try:
            self.interests = [i.strip() for i in interests_str.split(",")]
            self.messages.append(HumanMessage(content=interests_str))
            logger.info("Interest also set successfully!!")
        except Exception as e:
            logger.error(f"error failed to set interests:{str(e)}")
            raise CustomException("Failed to set interests",str(e))
    
    def create_itinerary(self):
        try:
            logger.info(f"Generating itinerary for {self.city} and for interest {self.interests}")
            itinerary = generate_itinerary(self.city,self.interests)
            self.itinerary = itinerary
            self.messages.append(AIMessage(content=itinerary))
            logger.info("Itinerary generated successfully..")
            return self.itinerary
        except Exception as e:
            logger.error(f"error failed to generate itinerary:{str(e)}")
            raise CustomException("Failed to generate itinerary",str(e))