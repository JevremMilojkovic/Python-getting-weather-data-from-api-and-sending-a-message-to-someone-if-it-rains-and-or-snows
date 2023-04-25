import requests
import Email

OW_api ="https://api.openweathermap.org/data/2.5/forecast"
api_key = "your api key"
from_email = "sender_email@gmail.com"
to_email = "receiver_email@gmail.com"
from_gmail_password = "dxdbvvgtcpkjtoal"

"""
    OW_api: Link to openweather site,
    api_key: Your generated API key,
    from_email: Sender email,
    password: !!! sender email password(not your mail password you need to go to manage your account settings and turn on 2 step authentication 
    under security after which u add app password that u will use here. The mail provider will give u a 16 digit
    password u will use here). If u dont do this, google will block your program from sending message.
    to_email: To who u are sending, the program lets u send multiple emails by adding them as a list.
    example for 2 receivers: mail_to=[to_email, to_email1]
    
"""



weather_params = {
    "lat": 44.786568,
    "lon": 20.448921,
    "appid": api_key
}
"""
  Lan and lon of location the user is interested in
"""

response = requests.get(OW_api, params=weather_params)
response.raise_for_status()
weather_data = response.json()
weather_slice = weather_data["list"][:7]

print(weather_slice)

will_rain = False
will_snow = False
will_rain_message = "Its not gonna rain today."
will_snow_message = "There is not snow today."
for data in weather_slice:
    condition_code = data["weather"][0]["id"]    
    if int(condition_code) < 600:
        will_rain = True
        will_rain_message = "Its gonna rain, bring a umbrella."
    if int(condition_code) < 700 and int(condition_code) >= 600:
        will_snow = True
        will_snow_message = "Also its gonna snow."


if will_rain or will_snow:
    my_email = Email.Email(server='smtp.gmail.com', port=465, address=from_email, password=from_gmail_password)
    """
        server: the code for your email provider like smtp.yahoo.com
        port: 465 is for sending emails
        address: sender email
        password: 16 digits password for apps your provider gave u    
    """

    my_email.send_email(
        mail_to=[to_email],
        subject= will_rain_message,
        body= will_snow_message,
        html=True,
        use_ssl=True,
    )

    """
        html: If true it will send email as html,
        use_ssl: Encrypts the message if true. Keep True unless u know what you are doing.
    """