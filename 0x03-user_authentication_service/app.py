#!/usr/bin/env python3
"""Basic Flask App"""

from flask import Flask, jsonify, request, abort, redirect, url_for
from auth import Auth

app = Flask(__name__)
AUTH = Auth()


@app.route('/', methods=['GET'], strict_slashes=False)
def index() -> str:
    """starting point for flask app"""
    return jsonify({"message": "Bienvenue"})


@app.route('/users', methods=['POST'], strict_slashes=False)
def reg_user() -> str:
    """registers or creates a user"""
    email = request.form.get("email")
    password = request.form.get("password")

    try:
        new_user = AUTH.register_user(email, password)
        return jsonify({"email": email, "message": "user created"})
    except ValueError:
        return jsonify({"message": "email already registered"})


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
