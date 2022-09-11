import numpy as np
import pandas as pd
from googletrans import Translator


filepath = 'data/issue_pool.txt'
target_language = 'ko'  # 'ja' for japan
save_xlsx = f'result/issue_pool_{target_language}.xlsx'

questions = {
    'English': [],
    target_language: []
}
with open(filepath, 'r', encoding='utf-8') as f:
    lines = f.readlines()

translator = Translator()

start_idx = 0
for i, line in enumerate(lines):
    if line.split(' ')[0] == 'Write':
        sentences = lines[start_idx:i-1]
        lengths = [len(sentence) for sentence in sentences]
        sentence = sentences[np.argmax(lengths)].replace('\n', '')
        translated = translator.translate(
            text=sentence, dest=target_language).text
        questions['English'].append(sentence)
        questions[target_language].append(translated)
        start_idx = i + 2

df = pd.DataFrame(questions)
df.to_excel(save_xlsx, index=False, encoding='utf-8')