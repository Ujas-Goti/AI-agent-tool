from flask import Blueprint, render_template, request, jsonify, session
from .agent import run_agent
from .utils import sanitize

bp = Blueprint("routes", __name__)

@bp.route("/", methods=["GET"])
def index():
    if "chat" not in session:
        session["chat"] = []
    return render_template("index.html")

@bp.route("/api/chat", methods=["POST"])
def api_chat():
    data = request.get_json(force=True)
    user_msg = sanitize(data.get("message", ""))
    if not user_msg:
        return jsonify({"error": "Empty message."}), 400

    # init session chat log
    chat = session.get("chat", [])

    # append user message
    chat.append({"role": "user", "content": user_msg})

    # run agent
    reply = run_agent(chat)

    # append assistant reply
    chat.append({"role": "assistant", "content": reply})
    session["chat"] = chat

    return jsonify({"reply": reply, "history": chat[-10:]})

@bp.route("/api/reset", methods=["POST"])
def api_reset():
    session["chat"] = []
    return jsonify({"ok": True})
