#!/usr/bin/env python3
import json
import os.path
from requests_html import HTMLSession
from datetime import datetime
from logger.loggingConfig import logger

url = "https://www.worldometers.info/ru"
file_path = "world_data.json"



def saveData(names, counts, path) -> None:
    if not names or not counts:
        logger.error("Нет данных для записи!")
        return
    data = {}
    for name, count in zip(names, counts):
        count_text = count.text.replace(",", "").replace('\n',' ').strip()
        name_text = name.text.replace(",", "").replace('\n',' ').strip()
        data[name_text] = count_text

    with open(path, 'w', encoding='utf8') as f:
        time_now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        data["timeParsed"] = time_now
        json.dump(data, f, ensure_ascii=False, indent=4)


    logger.info(f"Данные сохранены в JSON-файл в {time_now}.")


def ParseWorldometersData():
    session = HTMLSession()
    page = session.get(url)
    page.raise_for_status()

    try:
        page.html.render(timeout=20)
    except Exception as e:
        logger.error(f"Ошибка при рендеринге страницы: {e}")
        return

    counts = page.html.find('.counter-number')
    names = page.html.find('span.counter-item-double, span.counter-item')

    if not counts or not names:
        logger.error("Невозможно выбрать данные!")
        return
    saveData(names, counts, file_path)

    with open(file_path, encoding='utf-8') as f:
        data = json.load(f)

    return os.path.abspath(file_path)


if __name__ == "__main__":
    aa = ParseWorldometersData()