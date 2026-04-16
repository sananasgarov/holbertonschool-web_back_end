#!/usr/bin/env python3
""" Session authentication view """
from api.v1.views import app_views
from flask import request, jsonify, make_response
from models.user import User
import os


@app_views.route('/auth_session/login', methods=['POST'], strict_slashes=False)
def login():
    """Handle login with session auth"""

    # email və password götür
    email = request.form.get('email')
    password = request.form.get('password')

    # email yoxdursa
    if email is None or email == "":
        return jsonify({"error": "email missing"}), 400

    # password yoxdursa
    if password is None or password == "":
        return jsonify({"error": "password missing"}), 400

    # user tap
    users = User.search({"email": email})
    if not users or len(users) == 0:
        return jsonify({"error": "no user found for this email"}), 404

    user = users[0]

    # password check
    if not user.is_valid_password(password):
        return jsonify({"error": "wrong password"}), 401

    # ⚠️ circular import olmasın deyə burada import edirik
    from api.v1.app import auth

    # session yarat
    session_id = auth.create_session(user.id)

    # response
    response = make_response(jsonify(user.to_json()))

    # cookie adı env-dən götürülür
    session_name = os.getenv("SESSION_NAME")
    response.set_cookie(session_name, session_id)

    return response
def destroy_session(self, request=None):
    """Deletes the user session / logout"""

    # request yoxdursa
    if request is None:
        return False

    # cookie-dən session_id götür
    session_id = self.session_cookie(request)
    if session_id is None:
        return False

    # session_id user-a bağlıdır?
    user_id = self.user_id_for_session_id(session_id)
    if user_id is None:
        return False

    # session sil
    if session_id in self.user_id_by_session_id:
        del self.user_id_by_session_id[session_id]
        return True

    return False