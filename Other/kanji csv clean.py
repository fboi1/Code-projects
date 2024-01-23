import pandas as pd
import requests
import time

def get_reading_and_meaning(kanji):
    url = f"https://jisho.org/api/v1/search/words?keyword={kanji}"
    response = requests.get(url)
    if response.status_code != 200:
        return None, None

    data = response.json()
    try:
        japanese = data['data'][0]['japanese'][0]
        reading = japanese.get('reading', '')
        senses = data['data'][0]['senses'][0]
        meanings = ', '.join(senses['english_definitions'])
        return reading, meanings
    except (IndexError, KeyError):
        return None, None

def populate_excel(file_path):
    df = pd.read_excel(file_path)
    df['Hiragana'] = ''
    df['Meaning'] = ''

    for index, row in df.iterrows():
        kanji = row['Kanji']
        reading, meaning = get_reading_and_meaning(kanji)
        df.at[index, 'Hiragana'] = reading if reading else 'N/A'
        df.at[index, 'Meaning'] = meaning if meaning else 'N/A'
        time.sleep(0.5)
        print(df.head())

    df.to_excel(file_path, index=False)

# Replace 'your_file.xlsx' with the path to your Excel file
populate_excel(r'C:\firaas\500-kanji-python.xlsx')
