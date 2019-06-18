from flask_restful import Resource, reqparse
from flask_jwt import jwt_required
from flask_mail import Message
from app.tools.body import bodybuilder
from app import mail, db, app

class Contact(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument(
        "email",
        type=str,
        required=True
    )
    parser.add_argument(
        "name",
        type=str,
        required=True
    )
    parser.add_argument(
        "message",
        type=str,
        required=True
    )


    @jwt_required()
    def post(self):
        data = Contact.parser.parse_args()
        with app.app_context():
            msg = Message(
                subject="Contact from my Portfolio Page",
                recipients=["alvesefomm@gmail.com"],
                html=bodybuilder(email=data["email"], name=data["name"], message=data["message"])
                )
            mail.send(msg)
        return {"contact_data": data}