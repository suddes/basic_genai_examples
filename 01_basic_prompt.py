from langchain.chat_models.openai import ChatOpenAI
from langchain.prompts import  PromptTemplate
import os
os.environ['OPENAI_API_KEY'] = '<YOUR_KEY>'

llm = ChatOpenAI()

response = llm.predict("What date Titanic boat sink ?")
print(f"Response : {response}")

# Basic Example of a Prompt Template.
prompt_template = PromptTemplate.from_template(
    "List {n} recent movie names from {film_industry} with its date of release."
)
prompt = prompt_template.format(n=3, film_industry="bollywood")
print(f"Templated Prompt: {prompt}")

response = llm.predict(prompt)
print(f"Response: {response}")