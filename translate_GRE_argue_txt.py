import numpy as np
from googletrans import Translator


filepath = 'data/argue_pool.txt'
target_language = 'ko'  # 'ja' for japan
save_txt = f'result/argue_pool_{target_language}.txt'

with open(filepath, 'r', encoding='utf-8') as f:
    lines = f.readlines()

save_txt = open(save_txt, 'w', encoding='utf-8')

translator = Translator()

start_idx = 0
count = 1
for i, line in enumerate(lines):
    if line.split(' ')[0] == 'Write':
        sentences = ''.join(lines[start_idx:i-1])
        translated = translator.translate(
            text=sentences, dest=target_language).text
        sentences = sentences.replace('\n\n', '\n')
        translated = translated.replace('\n\n', '\n')
        save_txt.write(f"{count}. {sentences}{translated}\n\n")
        start_idx = i + 2
        count += 1

save_txt.close()