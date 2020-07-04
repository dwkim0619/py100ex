# 로봇 배제 표준 
#   - 웹 사이트에 로봇이 접근하는 것을 방지하기 위한 규약
#   - 일반적으로 접근 제한에 대한 설명을 robots.txt에 기술

#   - 웹 페이지에 접근하기 전에 반드시 로봇 배제 표준을 확인하고 가이드라인을 준수할 필요
#   - 웹 서버에 무리가 갈 만큼 반복적으로 웹 페이지를 요청하는 것과 같이 
#     서비스 안정성을 해칠 수 있는 행위를 하지 않아야 한다.
#   - 크롤링으로 취득한 자료를 임의로 배포하거나 변경하는 등의 행위는
#     저작권을 침해할 수 있으므로 저작권 규정을 준수해야 한다.

# https://www.python.org/robots.txt

import requests

urls = ["https://www.naver.com/", "https://www.python.org/"]
filename = "robots.txt"

for url in urls:
    filepath = url + filename
    print(filepath)

    resp = requests.get(filepath)
    print(resp.text)
    print("\n")

