# GRE Writing Pool Question Extractor

The official GRE site offers pool of 'Issue' and 'Argue' topics for writing section.  
- [Issue pool](https://www.ets.org/gre/revised_general/prepare/analytical_writing/issue/pool)
- [Argue pool](https://www.ets.org/gre/revised_general/prepare/analytical_writing/argument/pool)

```
This page contains the Argument topics for the Analytical Writing section of the GRE® General Test.
When you take the test, you will be presented with one Argument topic from this pool.
```

## Purpose

It is hard to practice all of the questions which total 338.  
However, it is worth reading all the topics before the test because there may be some confusing words or meanings to foreigners like me (Korean).  
So I made this naive extracting and translating codes to assist you guys whose native language is not English.

## Getting Started

0. Installation
    ```bash
    pip install -r requirements.txt
    ```

1. Extract topics from official GRE site  
  Actually I already extracted all of the topics and saved to below files.
    - data/argue_pool.txt
    - data/issue_pool.txt

2. Select your target language to be translated in codes

    change the 'target_language' parameter with your language
    ```python
    ## translate_GRE_issue_txt.py

    filepath = 'data/issue_pool.txt'
    target_language = 'ko'  # 'ja' for japan
    save_txt = f'result/issue_pool_{target_language}.txt'
    ...
    ```

3. Run translate scipt

    ```bash
    python translate_GRE_argue_txt.py
    python translate_GRE_issue_txt.py
    ```