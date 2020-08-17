from flaskblog import create_app
# The below command will only be true if we are running the run.py directly


app = create_app()
if __name__ == '__main__':
    app.run(debug=True)
