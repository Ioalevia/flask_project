# from blog.app import create_app
from blog.app import app

if __name__ == "__main__":
    app.run(
        host="0.0.0.0",
        debug=True,
    )

# app = create_app()
