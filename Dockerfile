# Выбор базового образа
FROM python:3.9

# Копирование файлов проекта в контейнер
WORKDIR /app
COPY . /app

# Установка зависимостей (если есть requirements.txt)
RUN pip install -r requirements.txt

# Команда для запуска приложения
CMD ["python", "app.py"]

