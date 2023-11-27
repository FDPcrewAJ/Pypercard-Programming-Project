"""
Simple exploration of the functionalities of PyperCard.
"""
from pypercard import App, Card

# Create the app while ensuring the counter is reset.
madlib_app = App(
    name="PyperCard Madlib"
)

@madlib_app.transition("card1", "click", "go_2")
def go_2(app, card): 
    app.datastore["user_name"] = card.get_by_id("user_name").value
    return "card2"

@madlib_app.transition("card2", "click", "go_3")
def go_3(app, card):
    app.datastore["n_1"] = card.get_by_id("n_1").value
    return "card3"

@madlib_app.transition("card3", "click", "go_4")
def go_4(app, card):
    app.datastore["v_1"] = card.get_by_id("v_1").value
    return "card4"

@madlib_app.transition("card4", "click", "go_5")
def go_5(app, card):
    app.datastore["a_1"] = card.get_by_id("a_1").value
    return "card5"

@madlib_app.transition("card5", "click", "go_6")
def go_6(app,card):
    app.datastore["ad_1"] = card.get_by_id("ad_1").value
    return "card6"

@madlib_app.transition("card6", "click", "restart")
def restart(app,card):
    return "card1"

#reset(carousel_app, "card1")

madlib_app.start("card1")