# Tuya LED Controller (Python)

CLI-утилита на Python для управления умной светодиодной лентой / гирляндой через Tuya Cloud API
(устройства Smart Life / Tuya).

Проект позволяет:
- включать и выключать ленту
- менять режимы работы
- управлять цветом (HSV)
- включать музыкальный режим
- ставить таймер выключения
- получать и парсить текущий статус устройства

## Возможности

- Object-Oriented архитектура (всё управление в классе)
- CLI-меню через input()
- Каждая команда — отдельный метод
- Парсер статуса устройства
- Работа через официальный Tuya Cloud API

## Поддерживаемые функции устройства

На основе спецификации Tuya (category: dd):

| Функция     | 	Описание                            |
|-------------|--------------------------------------|
| switch_led  | 	Вкл / выкл                          |
| work_mode   | 	Режим (white, colour, scene, music) |
| colour_data | 	Цвет (HSV)                          |
| music_data  | 	Музыкальный режим                   |
| countdown   | 	Таймер выключения                   |

## Требования

- Python 3.8+
- Аккаунт Tuya / Smart Life
- Созданный Tuya Cloud Project
- Привязанный аккаунт приложения к Cloud Project

## Установка
1. Клонировать репозиторий
```bash
git clone https://github.com/batMaxCom/TuyaLedController.git
cd tuya-led-controller
```

2. Установить зависимости
```bash
pip install -r requirements.txt
```

## Настройка Tuya Cloud

1. Перейти на https://iot.tuya.com

2. Создать Cloud Project

3. Выбрать регион (обычно Europe)

4. Привязать аккаунт Smart Life

5. Скопировать:
    - Access ID (Client ID)
    - Access Secret (Client Secret)

6. Получить device_id нужного устройства
7. Включить API (Service API):
   - IoT Core
   - Authorization Token Management

## Виртуальные переменные
```
ACCESS_ID=(Access ID/Client ID)
ACCESS_KEY=(Access Secret/Client Secret)
DEVICE_ID=(Device ID)
API_ENDPOINT=(в зависимости от региона, например "https://openapi.tuyaeu.com")
```

# CLI-меню
```diff
=== УПРАВЛЕНИЕ LED ЛЕНТОЙ ===
1 — Включить
2 — Выключить
3 — Установить цвет (HSV)
4 — Сменить режим
5 — Музыкальный режим
6 — Таймер выключения
7 — Показать статус
0 — Выход
```