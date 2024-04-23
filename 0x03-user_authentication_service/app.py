#!/usr/bin/env python3
"""Basic Flask App"""

from flask import Flask, jsonify, request, abort, redirect, url_for

app = Flask(__name__)


@app.route('/', methods=['GET'], strict_slashes=False)
def index() -> str:
    """starting point for flask app"""
    return jsonify({"message": "Bienvenue"})


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
