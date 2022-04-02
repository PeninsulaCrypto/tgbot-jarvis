import os
from dotenv import load_dotenv, dotenv_values

from jarvis import main

dotenv_path = os.path.join(os.path.dirname(__file__), '.env')
if os.path.exists(dotenv_path):
    load_dotenv(dotenv_path)

if __name__ == '__main__':
    main(app_config={
        **dotenv_values('.env'),
        **os.environ,
    })
