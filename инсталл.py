import subprocess
import sys

# Команда для установки aiogram прямо из кода
subprocess.check_call([sys.executable, "-m", "pip", "install", "aiogram"])

print("Установка завершена успешно!")
