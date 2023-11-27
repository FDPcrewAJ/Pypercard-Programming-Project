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
    app.datastore["a_1"] = card.get_by_id("a_1").value
    return "card4"

@madlib_app.transition("card4", "click", "go_5")
def go_5(app, card):
    app.datastore["n_2"] = card.get_by_id("n_2").value
    return "card5"

@madlib_app.transition("card5", "click", "go_6")
def go_6(app,card):
    app.datastore["av_1"] = card.get_by_id("av_1").value
    return "card6"

@madlib_app.transition("card6", "click", "go_7")
def go_6(app,card):
    app.datastore["v_1"] = card.get_by_id("v_1").value
    return "card7"

@madlib_app.transition("card7", "click", "go_8")
def go_6(app,card):
    app.datastore["n_3"] = card.get_by_id("n_3").value
    return "card8"

@madlib_app.transition("card8", "click", "go_9")
def go_6(app,card):
    app.datastore["v_2"] = card.get_by_id("v_20").value
    return "card9"

@madlib_app.transition("card9", "click", "go_10")
def go_6(app,card):
    app.datastore["n_4"] = card.get_by_id("n_4").value
    return "card10"

@madlib_app.transition("card10", "click", "go_11")
def go_6(app,card):
    app.datastore["a_2"] = card.get_by_id("a_2").value
    return "card11"

@madlib_app.transition("card11", "click", "go_12")
def go_6(app,card):
    app.datastore["a_3"] = card.get_by_id("a_3").value
    return "card12"

@madlib_app.transition("card12", "click", "go_13")
def go_6(app,card):
    app.datastore["v_3"] = card.get_by_id("v_3").value
    return "card13"

@madlib_app.transition("card13", "click", "go_14")
def go_6(app,card):
    app.datastore["v_4"] = card.get_by_id("v_4").value
    return "card14"

@madlib_app.transition("card14", "click", "go_15")
def go_6(app,card):
    app.datastore[""] = card.get_by_id("").value
    return "card15"

@madlib_app.transition("card15", "click", "go_16")
def go_6(app,card):
    app.datastore[""] = card.get_by_id("").value
    return "card16"

@madlib_app.transition("card16", "click", "go_17")
def go_6(app,card):
    app.datastore[""] = card.get_by_id("").value
    return "card17"

@madlib_app.transition("card17", "click", "go_18")
def go_6(app,card):
    app.datastore[""] = card.get_by_id("").value
    return "card18"

@madlib_app.transition("card18", "click", "go_19")
def go_6(app,card):
    app.datastore[""] = card.get_by_id("").value
    return "card19"

@madlib_app.transition("card19", "click", "go_20")
def go_6(app,card):
    app.datastore[""] = card.get_by_id("").value
    return "card20"

@madlib_app.transition("card20", "click", "go_21")
def go_6(app,card):
    app.datastore[""] = card.get_by_id("").value
    return "card21"

@madlib_app.transition("card21", "click", "restart")
def restart(app,card):
    return "card1"

#reset(carousel_app, "card1")

madlib_app.start("card1")