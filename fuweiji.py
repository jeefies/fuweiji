import os
from app import create_app

app = create_app(os.getenv("FLASK_CONFIG", 'default'))

@app.shell_context_processor
def make():
    return dict(app = app)


@app.cli.command()
def Command():
    "A simple test command"
    print("Command Run")

@app.cli.command()
def RunIn5040():
    "To run the web framework"
    app.run('0.0.0.0', 5040)
