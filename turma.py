import requests
from bs4 import BeautifulSoup
import re

def get_courses_page(html):
    soup = BeautifulSoup(html.text, 'html.parser')

    lines = soup.find_all('td')

    courses = []

    for i, td in enumerate(lines):
        if td.get_text(strip=True) == "Curso:":
            course = lines[i+1].get_text(strip=True)
            course = re.sub(r'\D', '', course)
            courses.append(course)
    return courses

def get_course(code: str, letter: str):
    pass