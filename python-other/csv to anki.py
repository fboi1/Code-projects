import pandas as pd

def create_anki_import_file(excel_file, output_csv):
    # Read the Excel file
    df = pd.read_excel(excel_file)

    # Create a new DataFrame for Anki import
    anki_df = pd.DataFrame()

    # Combine 'Hiragana' and 'Meaning' columns for the back of the flashcard
    anki_df['Front'] = df['Kanji']
    anki_df['Back'] = df['Hiragana'] + "<br>" + df['Meaning']  # Adding a line break between Hiragana and Meaning

    # Write to CSV (Anki import file)
    anki_df.to_csv(output_csv, index=False, header=False)

# Replace 'your_file.xlsx' with the path to your Excel file and 'output.csv' with your desired output file name
create_anki_import_file(r'C:\firaas\500-kanji-python.xlsx', r'C:\firaas\500-kanji-ankideck.xlsx')
