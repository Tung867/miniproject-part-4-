from flask import jsonify, request

users = [
    {"id": 1, "name": "Tung", "major": "Computer Science"},
    {"id": 2, "name": "Minh", "major": "AI"}
]

def register_routes(app):

    @app.route("/")
    def home():
        return jsonify({"message": "Flask API is running"})


    # Get all users
    @app.route("/api/users", methods=["GET"])
    def get_users():
        """
        Get all users
        ---
        tags:
          - Users

        responses:
          200:
            description: List of users
        """
        return jsonify(users)


    # Get user by ID
    @app.route("/api/users/<int:user_id>", methods=["GET"])
    def get_user(user_id):
        """
        Get user by ID
        ---
        tags:
          - Users

        parameters:
          - name: user_id
            in: path
            type: integer
            required: true
            description: User ID

        responses:
          200:
            description: User found
          404:
            description: User not found
        """

        for user in users:
            if user["id"] == user_id:
                return jsonify(user)

        return jsonify({"error": "User not found"}), 404


    # Add user
    @app.route("/api/users", methods=["POST"])
    def add_user():
        """
        Add new user
        ---
        tags:
          - Users

        parameters:
          - name: user
            in: body
            required: true
            schema:
              type: object
              properties:
                name:
                  type: string
                major:
                  type: string

        responses:
          201:
            description: User created
        """

        data = request.json

        new_user = {
            "id": len(users) + 1,
            "name": data["name"],
            "major": data["major"]
        }

        users.append(new_user)

        return jsonify(new_user), 201


    # Update user
    @app.route("/api/users/<int:user_id>", methods=["PUT"])
    def update_user(user_id):
        """
        Update user
        ---
        tags:
          - Users

        parameters:
          - name: user_id
            in: path
            type: integer
            required: true

          - name: user
            in: body
            required: true
            schema:
              type: object
              properties:
                name:
                  type: string
                major:
                  type: string

        responses:
          200:
            description: Updated
          404:
            description: Not found
        """

        data = request.json

        for user in users:
            if user["id"] == user_id:
                user["name"] = data["name"]
                user["major"] = data["major"]
                return jsonify(user)

        return jsonify({"error": "User not found"}), 404


    # Delete user
    @app.route("/api/users/<int:user_id>", methods=["DELETE"])
    def delete_user(user_id):
        """
        Delete user
        ---
        tags:
          - Users

        parameters:
          - name: user_id
            in: path
            type: integer
            required: true

        responses:
          200:
            description: Deleted
          404:
            description: Not found
        """

        for user in users:
            if user["id"] == user_id:
                users.remove(user)
                return jsonify({"message": "Deleted"})

        return jsonify({"error": "User not found"}), 404