import json
import logging
import os
from datetime import datetime

from dotenv import load_dotenv
from tuya_connector import TuyaOpenAPI, TUYA_LOGGER


class TuyaLEDController:
    def __init__(self, access_id, access_key, device_id, endpoint):
        self.device_id = device_id
        self.openapi = TuyaOpenAPI(endpoint, access_id, access_key)
        self.openapi.connect()

    # ---------- НИЗКОУРОВНЕВАЯ ОТПРАВКА ----------
    def _send_command(self, commands):
        return self.openapi.post(
            f"/v1.0/devices/{self.device_id}/commands",
            {"commands": commands}
        )

    # ---------- СТАТУС ----------
    def _get_status(self):
        return self.openapi.get(f"/v1.0/devices/{self.device_id}")

    def _parse_device_status(self, api_response: dict) -> dict:
        """
        Преобразует ответ Tuya API в удобный словарь состояния устройства
        """
        result = api_response.get("result", {})
        status_list = result.get("status", [])

        parsed = {
            "device_name": result.get("name"),
            "online": result.get("online"),
            "ip": result.get("ip"),
            "last_update": datetime.fromtimestamp(result.get("update_time", 0)),
            "power": None,
            "mode": None,
            "color": None,
            "countdown": None
        }

        for item in status_list:
            code = item.get("code")
            value = item.get("value")

            if code == "switch_led":
                parsed["power"] = "ON" if value else "OFF"

            elif code == "work_mode":
                parsed["mode"] = value

            elif code == "colour_data":
                if isinstance(value, str):
                    value = json.loads(value)
                parsed["color"] = {
                    "h": value.get("h"),
                    "s": value.get("s"),
                    "v": value.get("v")
                }

            elif code == "countdown":
                parsed["countdown"] = value

        return parsed

    def print_status(self):
        response = self._get_status()
        status = self._parse_device_status(response)
        print("\n=== СТАТУС УСТРОЙСТВА ===")
        print(f"Имя:        {status['device_name']}")
        print(f"Онлайн:     {'Да' if status['online'] else 'Нет'}")
        print(f"IP:         {status['ip']}")
        print(f"Обновлено:  {status['last_update']}")
        print(f"Питание:    {status['power']}")
        print(f"Режим:      {status['mode']}")

        if status["color"]:
            c = status["color"]
            print(f"Цвет (HSV): H={c['h']} S={c['s']} V={c['v']}")

        print(f"Таймер:     {status['countdown']} сек")

    # ---------- КОМАНДЫ ----------
    def power_on(self):
        self._send_command([{"code": "switch_led", "value": True}])
        print("✔ Лента включена")

    def power_off(self):
        self._send_command([{"code": "switch_led", "value": False}])
        print("✔ Лента выключена")

    def set_work_mode(self, mode):
        if mode not in ["white", "colour", "scene", "music"]:
            print("❌ Неверный режим")
            return
        self._send_command([{"code": "work_mode", "value": mode}])
        print(f"✔ Режим установлен: {mode}")

    def set_colour(self, h, s, v):
        self.set_work_mode("colour")
        self._send_command([{
            "code": "colour_data",
            "value": {"h": h, "s": s, "v": v}
        }])
        print(f"✔ Цвет установлен (H:{h} S:{s} V:{v})")

    def set_music_mode(self, h, s, v, bright, change_mode="direct"):
        self.set_work_mode("music")
        self._send_command([{
            "code": "music_data",
            "value": {
                "change_mode": change_mode,
                "bright": bright,
                "h": h,
                "s": s,
                "v": v
            }
        }])
        print("✔ Музыкальный режим активирован")

    def set_countdown(self, seconds):
        self._send_command([{"code": "countdown", "value": seconds}])
        print(f"✔ Таймер установлен: {seconds} сек")

    # ---------- CLI ----------
    def run_cli(self):
        if input("Включить отладку? (y/n): ").lower() == 'y':
            TUYA_LOGGER.setLevel(logging.DEBUG)
            print(f"✔ Отладка включена.")

        self.print_status()

        while True:
            print("\n=== УПРАВЛЕНИЕ LED ЛЕНТОЙ ===")
            print("1 — Включить")
            print("2 — Выключить")
            print("3 — Установить цвет (HSV)")
            print("4 — Сменить режим")
            print("5 — Музыкальный режим")
            print("6 — Таймер выключения")
            print("7 — Статус")
            print("0 — Выход")

            choice = input("Выбор: ")

            if choice == "1":
                self.power_on()

            elif choice == "2":
                self.power_off()

            elif choice == "3":
                h = int(input("Hue (0–360): "))
                s = int(input("Saturation (0–1000): "))
                v = int(input("Value (0–1000): "))
                self.set_colour(h, s, v)

            elif choice == "4":
                mode = input("Режим (white / colour / scene / music): ")
                self.set_work_mode(mode)

            elif choice == "5":
                h = int(input("Hue (0–360): "))
                s = int(input("S (0–255): "))
                v = int(input("V (0–255): "))
                bright = int(input("Яркость (0–1000): "))
                self.set_music_mode(h, s, v, bright)

            elif choice == "6":
                seconds = int(input("Через сколько секунд выключить: "))
                self.set_countdown(seconds)
            elif choice == "7":
                self.print_status()
            elif choice == "0":
                print("Выход...")
                break

            else:
                print("❌ Неверный выбор")

if __name__ == "__main__":
    load_dotenv()

    controller = TuyaLEDController(
        access_id=os.getenv("ACCESS_ID"),
        access_key=os.getenv("ACCESS_KEY"),
        device_id=os.getenv("DEVICE_ID"),
        endpoint=os.getenv("API_ENDPOINT")
    )
    controller.run_cli()