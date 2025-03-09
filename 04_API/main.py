from fastapi import FastAPI
import random

app = FastAPI()

# side_hustles
# money_quotes

side_hustles = [
    "Freelance Writing",
    "Online Tutoring",
    "Social Media Management",
    "Virtual Assistant",
    "Web Development",
    "Graphic Design",
    "Photography",
    "Food Delivery",
    "Ride-sharing",
    "Pet Sitting",
    "Dropshipping",
    "YouTube Content Creation",
    "Online Course Creation",
    "Affiliate Marketing",
    "Personal Training"
]
money_quotes =[
    "Money is a terrible master but an excellent servant. - P.T. Barnum",
    "The more you learn, the more you earn. - Warren Buffett",
    "Don't work for money; make money work for you. - Robert Kiyosaki",
    "Wealth is not about having a lot of money; it's about having a lot of options. - Chris Rock",
    "Money is only a tool. It will take you wherever you wish, but it will not replace you as the driver. - Ayn Rand",
    "The goal isn't more money. The goal is living life on your terms. - Chris Brogan",
    "Time is more valuable than money. You can get more money, but you cannot get more time. - Jim Rohn",
    "Money looks better in the bank than on your feet. - Sophia Amoruso",
    "Don't tell me what you value, show me your budget, and I'll tell you what you value. - Joe Biden",
    "The best investment you can make is in yourself. - Warren Buffett",
    "Money is like gasoline during a road trip. You don't want to run out of gas on your trip, but you're not doing a tour of gas stations. - Tim O'Reilly",
    "Never spend your money before you have earned it. - Thomas Jefferson",
    "It's not how much money you make, but how much money you keep. - Robert Kiyosaki",
    "Money is a great servant but a bad master. - Francis Bacon",
    "The lack of money is the root of all evil. - Mark Twain"
]

# it code no password 
@app.get("/side_hustles")
def get_side_hustles():
    """ Returns a random side hustles idea
    """
    return {"side_hustle": random.choice(side_hustles)}

@app.get("/money_quotes")
def get_money_quotes():
    """Return a random money quotes"""
    return {"money_quote":random.choice(money_quotes)}




# it code with password
# @app.get("/side_hustles")
# def get_side_hustles(apiKey: str):
#     """ Returns a random side hustles idea
#     """
#     if apiKey != "1234567890":
#         return{"error": "Invalid API Key"}
#     return {"side_hustle": random.choice(side_hustles)}

# @app.get("/money_quotes")
# def get_money_quotes(apiKey: str):
#     """Return a random money quotes"""
#     if apiKey != "1234567890":
#         return{"error": "Invalid API Key"}
#     return {"money_quote":random.choice(money_quotes)}
