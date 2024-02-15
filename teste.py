import os

from dotenv import load_dotenv

load_dotenv()

email = os.environ.get('USUARIO_EMAIL')

print(email)