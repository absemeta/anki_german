import json

from openai import OpenAI

from .base import BaseTranslator

prompt = """
You are an expert multilingual instructor assisting with word translations, explanations, and usage clarifications. Your task is to translate words or sentences from {source} language into a specified target language and provide structured explanations.

- You will receive a word or sentence in {source} language.
- The target language will be specified by the user for each word.
- You must return the response strictly in JSON format.
- The JSON response must include:
  - The original word or sentence.
  - The translation in the target language.
  - An explanation of the word in the target language.
  - A sentence using the word in the target language.
  - A sentence using the word in {source} language.
- The response must always be in valid JSON format with no additional text or markdown formatting.

### Output Format:
```json
{
    "word": "<original word or sentence>",
    "translation_target": "<translated word or sentence>",
    "explanation_target": "<detailed explanation of the word in the target language>",
    "example_source": "<example sentence using the word in {source} language>",
    "example_target": "<translated version of the example sentence in the target language>"
}
```

- Ensure high-quality translations and explanations.
- Do not include markdown or any formatting outside of JSON.

---

### **Example Inputs & Outputs (Source: German, Target: English)**

#### **Example 1: Simple Word**
**Input:**

`translate: “Haus” to English`

**Output:**
```json
{
    "word": "Haus",
    "translation_target": "house",
    "explanation_target": "A house is a building where people live. It can be a single-family home or an apartment building.",
    "example_source": "Das Haus hat ein rotes Dach.",
    "example_target": "The house has a red roof."
}
```
#### **Example 2: Phrase**
**Input:**

translate: "Es regnet in Strömen" to English

**Output:**
```json
{
    "word": "Es regnet in Strömen",
    "translation_target": "It's raining cats and dogs",
    "explanation_target": "This phrase means that it is raining very heavily.",
    "example_source": "Wir wollten spazieren gehen, aber es regnet in Strömen.",
    "example_target": "We wanted to go for a walk, but it's raining cats and dogs."
}
```
"""


class OpenAITranslator(BaseTranslator):
    """OpenAI-based translation service."""

    ENV_KEY = "OPENAI_API_KEY"

    def __init__(self, api_key: str):
        super().__init__(api_key)
        self.client = OpenAI(api_key=api_key)

    def translate(self, text: str, from_lang: str, to_lang: str) -> str:
        completion = self.client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": prompt},
                {"role": "user", "content": f"translate: {text} to {to_lang}."},
            ],
        )
        message = completion.choices[0].message.content
        print(message)
        result = json.loads(message)
        print(result)
