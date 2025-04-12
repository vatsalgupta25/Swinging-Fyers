import os
import webbrowser
from dotenv import load_dotenv
from fyers_apiv3 import fyersModel

load_dotenv()
appSession = fyersModel.SessionModel(
    client_id = os.environ['CLIENT_ID'], 
    secret_key=os.environ['SECRET_ID'],
    redirect_uri = os.environ['REDIRECT_URI'],
    response_type="code",
    state="login",
    grant_type="authorization_code"
)

generateTokenUrl = appSession.generate_authcode()
webbrowser.open(generateTokenUrl)