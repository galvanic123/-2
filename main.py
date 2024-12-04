from src.api_modul import HhJobService

hh = HhJobService("https://api.hh.ru/vacancies")
print(hh.get_jobs(params={"per_page": 1}))

with open("text.json", "w") as f:
    f.write(hh.get_jobs(params={"per_page": 1}))


# URL = 'https://api.hh.ru/vacancies'
# res = requests.get(URL, params={'text': 'Python'})
#
# print(res.status_code)
# print(res.json())