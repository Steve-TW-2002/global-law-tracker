from deep_translator import GoogleTranslator

def translate_laws(data):
    translator = GoogleTranslator(source='zh-tw', target='en')
    for item in data:
        try:
            item["英文標題"] = translator.translate(item['法案名稱'])
        except Exception as e:
            item["英文標題"] = "翻譯失敗"
            print(f"翻譯錯誤：{item['法案名稱']} → {e}")
    return data
