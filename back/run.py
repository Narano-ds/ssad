from flask.helpers import get_debug_flag

from src.app import boot
from src.settings import DevSettings, ProdSettings

app = boot(settings=DevSettings if get_debug_flag() else ProdSettings)

if __name__ == "__main__":
    app.run(use_reloader=True)
