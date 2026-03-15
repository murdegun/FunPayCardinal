from flask import Flask
import threading
import os

app = Flask(__name__)

@app.route('/')
def hello():
    return "Cardinal is alive!"

def run_bot():
    os.system("python3 main.py") # Запуск самого бота

if __name__ == "__main__":
    # Запускаем бота в отдельном потоке, чтобы веб-сервер не блокировал его
    threading.Thread(target=run_bot).start()
    # Запускаем веб-сервер на порту, который даст Render
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
