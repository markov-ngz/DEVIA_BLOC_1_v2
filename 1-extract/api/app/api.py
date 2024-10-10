import pandas as pd
import requests
import time
import os
from datetime import datetime


URL = "https://api-inference.huggingface.co/models/facebook/mbart-large-50-many-to-many-mmt"
API_TOKEN = os.getenv("AUTH_TOKEN_HF_API")
CSV_PATH = os.getenv("CSV_PATH")


def api_extraction()->pd.DataFrame:
    """
    Make an API call to Hugging face API 
    """

    # get french data 
    df = pd.read_csv(CSV_PATH)
    sentences_fr = df.french_text.values

    # container 
    language_dict = {
        "french_text":sentences_fr,
        "polish_text":[]
    }

    # requests params

    headers = {"Authorization": f"Bearer {API_TOKEN}"}

    # make a translation request every sentence
    for sentence in language_dict["french_text"]:

        # Content
        payload ={
        "inputs": sentence,
        "parameters":{
            "src_lang":"fr_XX",
            "tgt_lang":"pl_PL"
        }}

        # post request -> json -> dict
        response_json = requests.post(URL, headers=headers, json=payload)

        # extract the content 
        polish_translation = response_json.json()[0]["translation_text"]
        
        # append it
        language_dict["polish_text"].append(polish_translation)

        time.sleep(1) # to dodge the limit rate

    df = pd.DataFrame(language_dict)
    df["created_at"] = datetime.now().strftime("%Y-%m-%d")
    df["source"] = URL
    df["source_type"] = "API"

    return df

if __name__=='__main__':
    df = api_extraction()
    print(df.head())