import streamlit as st
import pandas as pd
from datetime import datetime as dt
import datetime
import scrapy


st.title("🎈 백종원 메이커!")
st.write(
    "백종원 메이커에 오신걸 환영합니다."
    "요리 어렵지 않습니다."
)

mbti = st.selectbox(
    "어떤 종류의 요리를 좋아하시나요?",
    ("한식", "중식", "양식", "잡식"))

if mbti == "한식":
    st.write("한식데이터")
elif mbti == "중식": 
    st.write("중식데이터")
elif mbti == "양식": 
    st.write("양식데이터")
elif mbti == "잡식": 
    st.write("돼지새끼")


class RecipeItem(scrapy.Item):
    recipe_name = scrapy.Field()
    ingredients = scrapy.Field()
    instructions = scrapy.Field()

class RecipeSpider(scrapy.Spider):
    name = "recipe_spider"
    start_urls = [
        'https://www.10000recipe.com/recipe/list.html'
    ]

    def parse(self, response):
        # 레시피 정보를 추출
        recipe_name = response.css('h1::text').get()
        ingredients = response.css('.listinfo .ingredients::text').get()
        instructions = response.css('.listinfo .instructions::text').get()

        yield {
            'recipe_name': recipe_name,
            'ingredients': ingredients,
            'instructions': instructions
        }
