from flask import Flask, render_template, request
from flask_debugtoolbar import DebugToolbarExtension

from stories import silly_story

app = Flask(__name__)
app.config['SECRET_KEY'] = "secret"

debug = DebugToolbarExtension(app)


@app.get("/")
def show_questions():
    """Render question form"""

    prompts = silly_story.prompts

    # TypeError: Story object is not subscriptable
    # prompts = silly_story["prompts"]

    return render_template("questions.html",
                           prompts=prompts)


@app.get("/results")
def show_results():
    """Render complete story on the results endpoint"""

    # use the get_result_text to complete the story with the input
    complete_story = silly_story.get_result_text(request.args)

    return render_template("results.html", complete_story=complete_story)
