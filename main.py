"""
Simple exploration of the functionalities of PyperCard.
"""
from pypercard import App, Card

# Create the app while ensuring the counter is reset.
carousel_app = App(
    name="PyperCard carousel"
)

@carousel_app.transition("card1", "click", "go_2")
def go_2(app, card): 
    app.datastore["user_name"] = card.get_by_id("user_name").value
    return "card2"

@carousel_app.transition("card2", "click", "reset")
def reset(app, card):
    return "card1"

@carousel_app.transition("card2", "click", "go_3")
def go_3(app, card):
    return "card3"

@carousel_app.transition("card3", "click", "go_1")
def go_1(app, card):
    return "card1"

@carousel_app.transition("card3", "click", "go_4")
def go_4(app, card):
    return "card4"

@carousel_app.transition("card4", "click", "restart")
def restart(app, card1):
    return "card1"

#reset(carousel_app, "card1")

carousel_app.start("card1")