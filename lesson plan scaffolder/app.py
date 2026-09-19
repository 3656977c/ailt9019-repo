"""
Flask web server for the Lesson Plan Scaffolder UI.
"""

from flask import Flask, request, jsonify, send_from_directory
from pathlib import Path
import sys

# Ensure scaffolder package is importable
sys.path.insert(0, str(Path(__file__).parent))

from scaffolder.planner import generate_lesson_plan
from scaffolder.formatter import format_markdown

app = Flask(__name__, static_folder="web")


@app.route("/")
def index():
    return send_from_directory("web", "index.html")


@app.route("/api/generate", methods=["POST"])
def api_generate():
    data = request.get_json(force=True)
    topic = data.get("topic", "").strip()
    duration = data.get("duration", 60)
    notes = data.get("notes", "").strip() or None

    if not topic:
        return jsonify({"error": "Topic is required."}), 400

    try:
        duration = int(duration)
    except (ValueError, TypeError):
        duration = 60

    plan = generate_lesson_plan(topic=topic, notes=notes, duration_minutes=duration)
    markdown = format_markdown(plan)

    return jsonify({
        "success": True,
        "plan": plan,
        "markdown": markdown,
    })


@app.route("/api/export", methods=["POST"])
def api_export():
    data = request.get_json(force=True)
    markdown = data.get("markdown", "")
    filename = data.get("filename", "lesson_plan.md")

    output_dir = Path(__file__).parent / "output"
    output_dir.mkdir(exist_ok=True)

    filepath = output_dir / filename
    filepath.write_text(markdown, encoding="utf-8")

    return jsonify({"success": True, "filepath": str(filepath)})


if __name__ == "__main__":
    app.run(debug=True, port=5000)
