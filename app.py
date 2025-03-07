from flask import Flask, jsonify, request
from flask_cors import CORS
import os
import json
from datetime import datetime

app = Flask(__name__, static_folder='build', static_url_path='/')
CORS(app)

# Данные для API
features = [
    {
        "id": 1,
        "title": "Современный дизайн",
        "description": "Элегантный и отзывчивый интерфейс с плавными анимациями",
        "icon": "design"
    },
    {
        "id": 2,
        "title": "Темная тема",
        "description": "Комфортный просмотр в любое время суток с автоматическим переключением",
        "icon": "dark_mode"
    },
    {
        "id": 3,
        "title": "Быстрая загрузка",
        "description": "Оптимизированная производительность для мгновенного отклика",
        "icon": "speed"
    },
    {
        "id": 4,
        "title": "Адаптивный дизайн",
        "description": "Идеальное отображение на любых устройствах и экранах",
        "icon": "devices"
    },
    {
        "id": 5,
        "title": "Интерактивность",
        "description": "Динамические элементы для улучшенного взаимодействия с пользователем",
        "icon": "touch_app"
    },
    {
        "id": 6,
        "title": "Безопасность",
        "description": "Защищенные соединения и современные протоколы безопасности",
        "icon": "security"
    }
]

testimonials = [
    {
        "id": 1,
        "name": "Алексей Петров",
        "position": "CEO, TechStart",
        "text": "Этот сайт превзошел все наши ожидания. Современный дизайн и отличная функциональность!",
        "avatar": "avatar1"
    },
    {
        "id": 2,
        "name": "Мария Иванова",
        "position": "Дизайнер, CreativeStudio",
        "text": "Потрясающий UI/UX. Каждая деталь продумана до мелочей. Браво!",
        "avatar": "avatar2"
    },
    {
        "id": 3,
        "name": "Дмитрий Сидоров",
        "position": "CTO, InnovateTech",
        "text": "Скорость работы и отзывчивость интерфейса на высшем уровне. Рекомендую!",
        "avatar": "avatar3"
    }
]

# API эндпоинты
@app.route('/api/hello', methods=['GET'])
def hello():
    return jsonify({
        "message": "Добро пожаловать на наш современный сайт!",
        "status": "success",
        "timestamp": datetime.now().isoformat()
    })

@app.route('/api/features', methods=['GET'])
def get_features():
    return jsonify({
        "data": features,
        "status": "success",
        "count": len(features)
    })

@app.route('/api/testimonials', methods=['GET'])
def get_testimonials():
    return jsonify({
        "data": testimonials,
        "status": "success",
        "count": len(testimonials)
    })

@app.route('/api/contact', methods=['POST'])
def contact():
    data = request.json
    # В реальном приложении здесь был бы код для сохранения данных
    return jsonify({
        "message": "Ваше сообщение успешно отправлено!",
        "status": "success",
        "received_data": data
    })

# Обслуживание React приложения
@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def serve(path):
    if path != "" and os.path.exists(app.static_folder + '/' + path):
        return app.send_static_file(path)
    return app.send_static_file('index.html')

if __name__ == '__main__':
    app.run(debug=True, port=5000) 