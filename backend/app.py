from flask import Flask, jsonify, request
from flask_cors import CORS
from services import AdviceService, Board, DashboardManager, Note

app = Flask(__name__)
CORS(app)

board = Board("Pizarra Dashboard")
board.add_note(Note("Bienvenida", "Esta es tu pizarra interactiva."))
board.add_note(Note("Tarea", "Crea, edita y elimina notas fácilmente."))

dashboard_manager = DashboardManager("Desarrollador")
advice_service = AdviceService()

@app.route("/api/board", methods=["GET"])
def get_board():
    return jsonify(board.to_dict())

@app.route("/api/time", methods=["GET"])
def get_time_data():
    return jsonify(dashboard_manager.get_current_time_data())

@app.route("/api/advice", methods=["GET"])
def get_advice():
    return jsonify(advice_service.fetch_random_advice())

@app.route("/api/notes", methods=["POST"])
def add_note():
    data = request.get_json() or {}
    title = data.get("title", "Nota sin título")
    content = data.get("content", "")
    note = Note(title, content)
    board.add_note(note)
    return jsonify(note.to_dict()), 201

@app.route("/api/notes/<int:note_id>", methods=["DELETE"])
def delete_note(note_id):
    success = board.remove_note_by_id(note_id)
    if success:
        return jsonify({"message": "Nota eliminada"})
    return jsonify({"error": "Nota no encontrada"}), 404

if __name__ == "__main__":
    app.run(debug=True, port=5000)
