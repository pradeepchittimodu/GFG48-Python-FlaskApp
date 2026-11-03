from flask import Flask

def create_app():
    app = Flask(__name__)
    print("inside create_app function")
    @app.route('/')
    def home():
        print("inside home function")
        return 'Hi hi 26-09-2026abcd12345 gbbvdfjv kv vvbvvu vv vuvbrbrv rv rur vr vrv rbh v rv rbvjjv v bru vv rv vbrv rv r'





    return app


if __name__ == '__main__':
    app = create_app()

    app.run(host='0.0.0.0', port=80, debug=True)
