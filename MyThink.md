# selenium-livechat-keyword-blocking
0. selenium을 통해 동적 웹페이지를 크롤링 할 수 있음, 속도는 매우 느림.
다른 방법과 병행하여 사용할 수 있음.

1. 유튜브 생방송 라이브 채팅 중 설정한 키워드를 포함한 댓글을 차단하는 앱을 python-selenium을 통해 만드려고 함.

2. selenium의 driver.find_elements_by_css_selector('#message') (#message 는 실시간 댓글의 css selector) 로 메시지 리스트를 만들어 출력하는 방식으로 실험해 보려 했지만 어떤 채팅도 얻을 수 없었음.

3. https://hashcode.co.kr/questions/9433/%EC%9C%A0%ED%8A%9C%EB%B8%8C-%EC%8B%A4%EC%8B%9C%EA%B0%84-%EC%B1%84%ED%8C%85-%ED%8C%8C%EC%9D%B4%EC%8D%AC%EC%9C%BC%EB%A1%9C-%ED%81%AC%EB%A1%A4%EB%A7%81-%EB%AA%BB%ED%95%98%EB%82%98%EC%9A%94 검색을 통해 채팅창이 iframe으로 되어 있고, json으로 데이터를 보여주는 구조라는 것을 알게 되었음.
직접 개발자 도구로 보니 iframe으로 감싸져 있었음.

4. selenium에서 iframe 내의 element를 추출하는 방법이 따로 있다는 것을 알게 됨.

5. https://dejavuqa.tistory.com/198 , https://m.blog.naver.com/PostView.nhn?blogId=kiddwannabe&logNo=221253004219&proxyReferer=https:%2F%2Fwww.google.com%2F 그 방법에 관한 내용임.
  - iframe은 html 안에 또 다른 html이 오는 경우이기 때문에 swich_to_frame()함수를 사용해 iframe 안에 있는 element를 확인 할 수 있게 해줘야 함.
  - iframe태그에 name 속성이 있다면 driver.switch_to_frame("iframe name 값")dmfh 해당 iframe으로 focus를 맞춰 줄 수 있음. (2번째 글에선 switch_to.frame()이라고 함)
  - id 선택자 있길래 id 선택자로도 선택 가능한지 검색해봄
  - 
    ```
    iframes = driver.find_elements_by_css_selector('iframe')
    for iframe in iframes:
      print(iframe.get_attribute('id'))
    ``` 으로 하니까 id 하나 출력됨 'chatframe' 개발자 도구로 확인한 것과 같음.
    
  -driver.switch_to.frame("chatframe") 해봄.
  -일단 오류는 안뜸. print(driver.page_source)로 해보니 vscode에서는 줄이 너무 길어서 다 안나오고 python idle로 하니 전체 html 나옴. 성공.
  -
6. live 챗만 따로 모으는 방법도 있음(pytchat라이브러리) 쓸모는 없음.

7.
