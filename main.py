import pandas as pd
import random
from datetime import datetime
from docx import Document

file_path = 'example_members_2024_final.xlsx'

df = pd.read_excel(file_path)

non_winners = df[df['Won'] == False]

won = non_winners.sample(n=3)

df.loc[won.index, 'Won'] = True


df.to_excel(file_path, index=False)

doc = Document('Lotterimall.docx')

winners = won['Name'].tolist()


for paragraph in doc.paragraphs:
    for run in paragraph.runs:
        if 'Person1' in run.text:
            run.text = run.text.replace('Person1', winners[0])
        if 'Person2' in run.text:
            run.text = run.text.replace('Person2', winners[1])
        if 'Person3' in run.text:
            run.text = run.text.replace('Person3', winners[2])

current_month = datetime.now().strftime("%B")

new_file_name = f'Medlemslotteri vinnare {current_month}.docx'
doc.save(new_file_name)

print(f"De tre vinnarna är {winners}")
print(f"Resultatet har sparats i filen: {new_file_name}.")