import os
import requests
from twilio.rest import Client
from twilio.http.http_client import TwilioHttpClient

parameters = {
    "lat": 53.173180,
    "lon": 6.602950,
    "exclude": "current,minutely,daily,alerts",
    "appid": os.environ.get("OWM_API_KEY"),
}

proxy_client = TwilioHttpClient()
proxy_client.session.proxies = {'https': os.environ['https_proxy']}

account_sid = os.environ.get("TWI_API_SID")
auth_token = os.environ.get("TWI_AUTH_TOKEN")
client = Client(account_sid, auth_token, http_client=proxy_client)

response = requests.get(url="https://api.openweathermap.org/data/2.5/onecall", params=parameters)
response.raise_for_status()

weather_data = response.json()["hourly"]


def send_rain_alert():
    message = client.messages.create(
        body=" It's going to rain today. Bring an umbrella.️",
        from_=os.environ.get("FROM_PHONE"),
        to=os.environ.get("TO_PHONE")
    )

    print(message.status)


for x in range(12):
    if weather_data[x]["weather"][0]["id"] < 700:
        send_rain_alert()
        break
