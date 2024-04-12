# CookBot : 당신의 개인 요리 도우미

CookBot은 OpenAI의 GPT-4 모델, 일래스틱서치, Streamlit을 기반으로 작동하며, 사용자의 질문에 맞는 레시피를 찾고 단계별 가이드를 통해 상호작용형 요리를 하는 것을 목표로 합니다.


## 기술 요구 사항

개발 환경이 아래 요구 사항을 만족하는지 먼저 확인해 주세요.

- Python 3.8 또는 그 이상
- [Elasticsearch](https://www.elastic.co/guide/en/elasticsearch/reference/current/install-elasticsearch.html)
- [Streamlit](https://docs.streamlit.io/library/get-started/installation)

필요한 파이썬 라이브러리는 아래와 같습니다.

- `openai`
- `streamlit`
- `elasticsearch`
- `requests`

라이브러리는 pip를 통해 설치할 수 있습니다.

```bash
pip install openai streamlit elasticsearch requests
```

## 시작하기

### 저장소 복제

먼저 저장소를 로컬 환경에 복제하세요. 

```bash
git clone https://github.com/your-username/CookBot.git
cd CookBot
```

### 환경 설정
가상 환경을 만들고 활성화 하세요.

```bash
python3 -m venv env
source env/bin/activate
```

### 필요한 의존성 설치

```bash
pip install -r requirements.txt
```


### 환경 변수 설정

OpenAI API 키를 환경 변수로 설정하세요. 

```bash
export OPENAI_API_KEY='your-api-key'
```

`'your-api-key'`를 실제 OpenAI API 키로 바꾸세요.

### 애플리케이션 실행

Streamlit 서버를 시작하려면 아래와 같이 입력하세요.

```bash
streamlit run app.py
```

Streamlit 앱은 `http://localhost:8501`에서 동작합니다. 이 URL을 웹 브라우저에서 열어 CookBot을 사용하세요.

## 사용법

요리 관련 질문을 입력 상자에 입력하면 CookBot이 관련 레시피를 찾고 그 정보를 바탕으로 단계별 가이드를 생성합니다.