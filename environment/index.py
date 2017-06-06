from flask import Flask
from user import user_page
from resource import resource_page

app = Flask(__name__)
app.register_blueprint(user_page)
app.register_blueprint(resource_page)

if __name__ == "__main__":
    app.run()
