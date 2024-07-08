from googletrans import Translator
from langdetect import detect

class CLIPTextAutoTranslate:
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
                translator = Translator()
                text = translator.translate(text, dest='en').text
        tokens = clip.tokenize(text)
        cond, pooled = clip.encode_from_tokens(tokens, return_pooled=True)
        return ([[cond, {"pooled_output": pooled}]], )



# Daftar node yang ingin diekspor dengan nama mereka
NODE_CLASS_MAPPINGS = {
    "CLIP Text Encode (Auto Translate)": CLIPTextAutoTranslate
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "CLIPTextAutoTranslate": "CLIP Text Encode (Auto Translate)",
}
