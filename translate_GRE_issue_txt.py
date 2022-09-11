import numpy as np
from googletrans import Translator


filepath = 'data/issue_pool.txt'
target_language = 'ko'  # 'ja' for japan
save_txt = f'result/issue_pool_{target_language}.txt'

with open(filepath, 'r', encoding='utf-8') as f:
    lines = f.readlines()

save_txt = open(save_txt, 'w', encoding='utf-8')

translator = Translator()

start_idx = 0
count = 1
for i, line in enumerate(lines):
    if line.split(' ')[0] == 'Write':
        sentences = lines[start_idx:i-1]
        lengths = [len(sentence) for sentence in sentences]
        sentence = sentences[np.argmax(lengths)].replace('\n', '')
        translated = translator.translate(
            text=sentence, dest=target_language).text
        save_txt.write(f'{count}. {sentence}\n{translated}\n\n')
        start_idx = i + 2
        count += 1

save_txt.close()