import openai
import openpyxl
import pandas as pd

prompt_do_chata = "5 click-worthy post ideas about AI"
openai.api_key = "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"

def generate_post_ideas(num_ideas):
     
    post_ideas = []
    for _ in range(num_ideas):
        response = openai.Completion.create(
            engine="text-davinci-003",
            prompt=prompt_do_chata,
            max_tokens=50,
            n=1,
            stop=None,
            temperature=0.7
        )

        idea = response.choices[0].text.strip()
        post_ideas.append(idea)

    return post_ideas

def save_ideas_to_excel(ideas):
    workbook = openpyxl.Workbook()
    sheet = workbook.active
    sheet['A1'] = 'Post Idea'

    row = 2
    for idea in ideas:
        if idea.startswith('\n'):
            idea = idea[1:]  # Usuń znak nowej linii z początku
            row += 1

        sheet.cell(row=row, column=1, value=idea)
        row += 1

    workbook.save('post_ideas.xlsx')
    print("Pomysły na posty zostały zapisane w pliku post_ideas.xlsx.")

num_ideas = 10
ideas = generate_post_ideas(num_ideas)
save_ideas_to_excel(ideas)
