"""
Парсинг карточек объявлений BN.ru – надёжное извлечение цены
"""
import re
from typing import Optional, Dict, Any
from bs4 import BeautifulSoup

def extract_numeric(text: str) -> Optional[float]:
    if not text:
        return None
    # Удаляем все виды пробелов и меняем запятую на точку
    cleaned = text.replace(" ", "").replace("\xa0", "").replace(",", ".")
    match = re.search(r'\d+\.?\d*', cleaned)
    return float(match.group()) if match else None

def parse_listing_card(html_or_element, debug_first: bool = False) -> Dict[str, Any]:
    if hasattr(html_or_element, 'get_attribute'):
        html = html_or_element.get_attribute('outerHTML')
    else:
        html = html_or_element
    soup = BeautifulSoup(html, 'html.parser')

    data = {
        "title": None,
        "price": None,
        "address": None,
        "area": None,
        "rooms": None,
        "floor": None,
        "link": None,
    }

    # Ссылка
    link_el = soup.select_one("a.catalog-item")
    if link_el:
        href = link_el.get("href")
        if href:
            if href.startswith("/"):
                data["link"] = "https://www.bn.ru" + href
            else:
                data["link"] = href

    # Заголовок
    title_el = soup.select_one("div.catalog-item__headline")
    if title_el:
        data["title"] = title_el.get_text(strip=True)

    # Цена – пробуем несколько вариантов
    price_el = soup.select_one("div.catalog-item__price")
    if not price_el:
        # Ищем любой элемент с классом, содержащим 'price', но не 'unit', 'firm', 'description'
        price_el = soup.select_one("[class*='price']:not([class*='unit']):not([class*='firm']):not([class*='description'])")
    if not price_el:
        # Попробуем найти span с классом price
        price_el = soup.select_one("span[class*='price']")
    if price_el:
        price_text = price_el.get_text(strip=True)
        data["price"] = extract_numeric(price_text)
        if debug_first:
            print(f"[DEBUG] Цена из '{price_text}' -> {data['price']}")

    # Адрес
    address_el = soup.select_one("div.catalog-item__address")
    if address_el:
        data["address"] = address_el.get_text(strip=True)

    # Площадь и комнаты из заголовка
    if data["title"]:
        title_text = data["title"]
        area_match = re.search(r'(\d+[,.]?\d*)\s*м[2²]', title_text)
        if area_match:
            data["area"] = extract_numeric(area_match.group(1))
        if 'студия' in title_text.lower():
            data["rooms"] = 0
        else:
            rooms_match = re.search(r'(\d+)\s*[-к]', title_text)
            if not rooms_match:
                rooms_match = re.search(r'(\d+)\s*комн', title_text)
            if rooms_match:
                data["rooms"] = int(rooms_match.group(1))

    # Этаж
    param_spans = soup.select("span.catalog-item__param")
    for param in param_spans:
        text = param.get_text(strip=True)
        if 'этаж' in text:
            value_el = param.select_one("span.catalog-item__param-value")
            if value_el:
                data["floor"] = value_el.get_text(strip=True)
            else:
                match = re.search(r'(\d+/\d+)', text)
                if match:
                    data["floor"] = match.group(1)
            break

    return data

