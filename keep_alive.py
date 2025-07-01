from flask import Flask, redirect

app = Flask(__name__)

# Dein Dictionary mit Kurzlinks
links = {
    "discord": "https://grabify.link/JQI7A0",
    # hier weitere Kürzel hinzufügen
}

@app.route('/')
def home():
    return "URL Shortener läuft!"

@app.route('/<code>')
def redirect_to(code):
    url = links.get(code)
    if url:
        return redirect(url)  # Direkte Weiterleitung ohne Zwischenseite
    else:
        return "Link nicht gefunden", 404

if _name_ == "_main_":
    app.run(host="0.0.0.0", port=5000)
