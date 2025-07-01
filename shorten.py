from flask import Flask, redirect, abort, request, jsonify

app = Flask(__name__)

# Ein simples Dictionary als "Datenbank"
links = {
    "abc": "https://grabify.link/JQI7A0",
}

@app.route('/')
def index():
    return "URL-Shortener läuft! Nutze /<code> zum Weiterleiten."

@app.route('/<code>')
def redirect_code(code):
    url = links.get(code)
    if url:
        return redirect(url)
    else:
        abort(404)

# Optional: API, um Links dynamisch hinzuzufügen (POST JSON: {"code": "...", "url": "..."})
@app.route('/add', methods=['POST'])
def add_link():
    data = request.get_json()
    if not data or 'code' not in data or 'url' not in data:
        return jsonify({"error": "Feld 'code' und 'url' sind erforderlich."}), 400
    code = data['code'].strip()
    url = data['url'].strip()
    if code in links:
        return jsonify({"error": "Code existiert bereits."}), 400
    links[code] = url
    return jsonify({"message": f"Link {code} hinzugefügt."}), 201

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
