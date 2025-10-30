1. django 프로젝트를 생성하고 시작해서 웹사이트를 보는것
2. 이 프로젝트를 위한 파이썬 가상 환경을 생성한다.
  - 반드시 가상환경 생성 전에 gitignore 먼저 만들어야 한다.
  - gitignore.io 사이트에서 만들거나, 기존에 만들어 뒀던 파일을 복사해 온다.
3. 이 프로젝트를 위한 패키지를 모두 설치했으면, 그 버전을 `requirements.txt` 파일에 기록 해주자.
```bash
$ code .gitignore
$ python -m venv {folder_name}
$ source venv/Scripts/Activate
$ pip list
$ pip install django
$ pip freeze > requirements.txt

# 다음에 프로젝트 진행하는 새로운 환경에서는
# 이 메모장에 적힌 버젼들을 `읽어서` 설치 할 수 있다.
$ pip install -r requirements.txt
```

3. django 프로젝트를 생성 한다.
```bash
$ django-admin startproject {project_name} {path}
$ python manage.py startapp articles
```

4. 내가 생성한 이 프로젝트는, 그 후에 만든 app에 대해서 알까?
  - django는 새로 만든 앱 이름을 모르니, 등록 해 줘야한다.
  - 어디에?? 등록이란걸 해야할까?
  - 내 프로젝트의 설정

5. 기능을 만든다.
  - 웹페이지를 만든다.
  - 머릿속으로 생각한다. 웹사이트를 쓰는 방법을
    - 구글을 킨다. 네이버에 들어가고 싶다.
    - 뭐가필요하다?
      - 뭘로 검색해야 네이버 페이지로 이동 할 수 있음?
      - 네이버 주소를 검색한다. <- URL
      - www.naver.com
    - www.edu.ssafy.com/lecture

  1. 나는 우리 홈페이지의 메인 페이지를 사용자에게 보여주고싶어.
  2. 그러면, 어디로 요청을 보내야 하는지를 먼저 정한다.