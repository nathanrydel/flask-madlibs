from flask import Flask, render_template, request
from flask_debugtoolbar import DebugToolbarExtension

from stories import silly_story

app = Flask(__name__)
app.config['SECRET_KEY'] = "secret"

debug = DebugToolbarExtension(app)

# TODO: create a route for the homepage that shows a form asking for madlibs
# DO NOT hardcode the form asking these exact questions


@app.get("/")
def index():
    """Render homepage form"""
    #grab prompts from stories;
    #send to questions page
    prompts = silly_story["prompts"]

    return render_template("questions.html",
                           prompts=prompts
                           )
    # print("html is: ", html)

    # return html


# TODO: Add a route, /results, that shows the resulting story for those answers
@app.get("/results")
def show_results():
    # TODO: add docstring
    """"""

    ...
