import json

import requests
import streamlit as st

from config import OPENAI_API_KEY, ES_ENDPOINT, ES_USERNAME, ES_PASSWORD
from recipe_generator import RecipeGenerator

# RecipeGenerator 초기화
generator = RecipeGenerator(OPENAI_API_KEY)

# 일래스틱서치 조회
def elasticsearch_query(query):
    headers = {'Content-Type': 'application/json'}
    response = requests.get(ES_ENDPOINT, headers=headers, data=json.dumps(query), auth=(ES_USERNAME, ES_PASSWORD))

    result = {
        "name": response.json()["hits"]["hits"][0]["_source"]["name"],
        "group": response.json()["hits"]["hits"][0]["_source"]["group"],
        "ingredient": response.json()["hits"]["hits"][0]["_source"]["ingredient"],
    }
    return result

# 나머지 Streamlit 코드
with open("style.css") as f:
    st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

st.markdown(
    """
        <style>
    @font-face {
        font-family: 'Inconsolata';
        src: url(https://fonts.googleapis.com/css?family=Inconsolata);
    }

    html, body, [class*="css"]  {
    font-family: 'Incosolata', monospace !important;
    color: #fff;

    }
    </style>

    """,
    unsafe_allow_html=True,
)


st.title('CookBot')
st.caption('당신의 개인 요리 도우미')
col1, col2 = st.columns([1, 6])
with col1:
    st.image("https://i.ibb.co/bWDhmTg/Screenshot-2023-07-28-at-11-06-56-PM.png")
with col2:
    input_text = st.text_input(" ", placeholder="요리에 대해 궁금한 것이 있다면 무엇이든 물어보세요.")

    if input_text:
        query = {
            "sub_searches": [
                {
                    "query": {
                        "match": {
                            "ingredient": {
                                "query": input_text,
                                "operator": "and"
                            }
                        }
                    }
                },
                {
                    "query": {
                        "text_expansion": {
                            "ml.tokens": {
                                "model_id": ".elser_model_2",
                                "model_text": input_text
                            }
                        }
                    }
                }
            ],
            "rank": {
                "rrf": {
                    "window_size": 50,
                    "rank_constant": 20
                }
            }
        }

        recipe = elasticsearch_query(query)
        st.write(recipe)
        st.write(generator.generate(recipe))
