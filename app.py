from flask import Flask, render_template, request
from flask_debugtoolbar import DebugToolbarExtension

from stories import silly_story

app = Flask(__name__)
app.config['SECRET_KEY'] = "secret"

debug = DebugToolbarExtension(app)


@app.get("/")
def show_questions():
    """Render question form"""
    # grab prompts from stories;
    # send to questions page
    prompts = silly_story.prompts

    print(prompts)

    return render_template("questions.html",
                           prompts=prompts)


# TODO: Add a route, /results, that shows the resulting story for those answers
@app.get("/results")
def show_results():
    # TODO: add docstring
    """"""

    ...
