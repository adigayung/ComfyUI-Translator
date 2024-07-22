from deep_translator import GoogleTranslator
from langdetect import detect
import traceback

class AT_CLIPTextAutoTranslate:
    @classmethod
    def INPUT_TYPES(s):
        return {"required": {"text": ("STRING", {"multiline": True, "dynamicPrompts": True}), "clip": ("CLIP", )}}
    RETURN_TYPES = ("CONDITIONING",)
    FUNCTION = "encode"
    CATEGORY = "conditioning"

    def encode(self, clip, text):
        if text.strip():
            detected_lang = detect(text)
            if detected_lang != 'en':
                try:
                    translator = GoogleTranslator(source='auto', target='en')
                    text = translator.translate(text)
                except Exception as e:
                    print(f"Translation error: {e}")
                    traceback.print_exc()
                    # Anda bisa memilih untuk melanjutkan dengan teks asli jika terjadi error
        tokens = clip.tokenize(text)
        cond, pooled = clip.encode_from_tokens(tokens, return_pooled=True)
        return ([[cond, {"pooled_output": pooled}]], )

class AT_PromptText:
    @classmethod
    def INPUT_TYPES(s):
        return {"required": {"prompt": ("STRING", {"default": "prompt", "multiline": True})}}
    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("prompt",)
    FUNCTION = "get_value"
    CATEGORY = "conditioning"

    def get_value(self, prompt):
        if prompt.strip():
            detected_lang = detect(prompt)
            if detected_lang != 'en':
                try:
                    translator = GoogleTranslator(source='auto', target='en')
                    prompt = translator.translate(prompt)
                except Exception as e:
                    print(f"Translation error: {e}")
                    traceback.print_exc()
        return (prompt,)

# Daftar node yang ingin diekspor dengan nama mereka
NODE_CLASS_MAPPINGS = {
    "CLIP Text Encode (Auto Translate)": AT_CLIPTextAutoTranslate,
    "Prompt Text (Auto Translate)": AT_PromptText,
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "AT_CLIPTextAutoTranslate": "CLIP Text Encode (Auto Translate)",
    "AT_PromptText": "Prompt Text (Auto Translate)",
}
