from ariadne import graphql_sync
from ariadne.constants import PLAYGROUND_HTML
from flask import Blueprint, jsonify, redirect, request

from .graphql import schema

graphql_routes = Blueprint("graphql_routes", __name__)


@graphql_routes.route("/", methods=["GET"])
def graphql_playground_redirect():
    return redirect("/graphql")


@graphql_routes.route("/graphql", methods=["GET"])
def graphql_playground():
    # On GET request serve GraphQL Playground
    # You don't need to provide Playground if you don't want to
    # but keep on mind this will not prohibit clients from
    # exploring your API using desktop GraphQL Playground app.
    return PLAYGROUND_HTML, 200


@graphql_routes.route("/graphql", methods=["POST"])
def graphql_server():
    # GraphQL queries are always sent as POST
    data = request.get_json()

    # Note: Passing the request to the context is optional.
    # In Flask, the current request is always accessible as flask.request
    success, result = graphql_sync(
        schema,
        data,
        context_value=request,
    )

    status_code = 200 if success else 400
    return jsonify(result), status_code
