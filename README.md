# Flask Application

Это простое приложение на Flask, которое выполняет базовые операции с API.

## Запуск локально

1. Клонируйте репозиторий.
2. Создайте виртуальное окружение:
    ```bash
    python3 -m venv venv
    source venv/bin/activate
    ```
3. Установите зависимости:
    ```bash
    pip install -r requirements.txt
    ```
4. Запустите приложение:
    ```bash
    python app.py
    ```

## Развертывание с Docker

1. Построить Docker-образ:
    ```bash
    docker build -t flask-app .
    ```
2. Запустите контейнер:
    ```bash
    docker-compose up
    ```

## CI/CD

Этот проект настроен с использованием GitLab CI для автоматического тестирования, сборки и деплоя.

