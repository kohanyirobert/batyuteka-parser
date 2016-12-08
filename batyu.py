from urllib.request import urlopen
from bs4 import BeautifulSoup
import re
from datetime import datetime


URL = 'http://batyuteka.hu/etelrendeles'


def get_menu_html():
    response = urlopen(URL)
    html = response.read()
    return html


def normalize_cell(cell):
    return ' '.join(cell.text.strip().split())


def get_day_index():
    return datetime.today().weekday()


def remove_kcal(food):
    return re.sub(r'^(.*?)\s+[\d]+\s+kcal.*$', r'\1', food)


def get_foods(day_index, rows):
    return [get_food(day_index, row) for row in rows]


def get_food(day_index, row):
    cells = row.select('td')
    cells = cells[1:]
    cell = cells[day_index]
    return remove_kcal(normalize_cell(cell))


def get_rows(html):
    soup = BeautifulSoup(html, 'lxml')
    tables = soup.select('table.table-menu')
    first_table = tables[0]
    rows = first_table.select('tr')
    return rows[2::2]


def get_menu(day_index = get_day_index()):
    if day_index < 0 or day_index > 5:
        return []
    menu_html = get_menu_html()
    rows = get_rows(menu_html)
    return get_foods(day_index, rows)
