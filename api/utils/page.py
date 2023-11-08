import requests
import base64


BASE_URL = "https://static-editions.manoramaonline.com/EMagazineDocRoot/MMBalarama/{year}/{month}/{day}/MMBalarama_{year}_{month}_{day}_{page}_PR.jpg"
REF_URL = "https://ebalarama.manoramaonline.com/"

header = {
    "referer": REF_URL
}

def get_page(page: int):
  num = str(page)
  return f"{'0'*(3-len(num))}{num}"

def get_url(page: int, year, month ,day):
  page = get_page(page)

  day = str(day)
  if len(day) == 1:
    day = f"0{day}"

  url = BASE_URL.format(page=page, year=year, month=month, day=day)
  return url


def get_image(page: int, year: int, month: int, day: int):
    s = requests.Session()
    s.headers.update(header)
    url = get_url(page=page, year=year, month=month, day=day)

    resp = s.get(url)
    return {
        "data": base64.b64encode(resp.content).decode('ascii')
    }