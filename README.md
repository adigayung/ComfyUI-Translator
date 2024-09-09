
# ComfyUI Translator Node

This repository contains a custom node for **ComfyUI** that allows you to translate any input language into English, enabling seamless processing through ComfyUI. With this node, users can input text in any language, and it will be automatically translated to English before being passed to ComfyUI for further processing.

## Key Features
- **Multi-language Input**: Supports input in various languages, automatically detecting the input language.
- **Translation to English**: Utilizes the **Google Translator** API to translate text from any language to English.
- **Seamless Integration with ComfyUI**: The translated text is then processed by ComfyUI, making this node an essential tool for multi-language support.

## Installation

To install this node for use with **ComfyUI**, follow the steps below:

### For ComfyUI Embedded Python

1. Navigate to the directory where the custom node is located:
   ```bash
   cd custom_nodes\ComfyUI-Translator
   ```

2. Install the required dependencies using the embedded Python in ComfyUI:
   ```bash
   ..\..\..\python_embeded\python.exe -m pip install -r requirements.txt
   ```

The installation process will install the necessary packages such as `deep_translator` and `langdetect`, which are required for the translation functionality.

## Dependencies

The script relies on the following Python packages:

- **deep_translator**: This is used to interact with Google Translate and perform the translation.
- **langdetect**: This is used to detect the input language before translating it.
- **traceback**: For handling errors and debugging in case of translation failures.

You can find these dependencies listed in the `requirements.txt` file, and they will be installed automatically during the installation process.

## How It Works

1. **Language Detection**: The node first detects the input language using the `langdetect` package.
2. **Translation**: Once the input language is detected, the text is translated into English using **Google Translator** via the `deep_translator` package.
3. **Error Handling**: In case of any issues during translation (such as a connection error or unsupported language), the script utilizes `traceback` to log the error and proceed gracefully.
4. **Integration with ComfyUI**: After translation, the English text is passed to ComfyUI for further processing as usual.

### Example Code Snippet

```python
from deep_translator import GoogleTranslator
from langdetect import detect
import traceback

def translate_input(text):
    try:
        # Detect the language of the input text
        detected_language = detect(text)
        print(f"Detected language: {detected_language}")

        # Translate the text to English
        translated_text = GoogleTranslator(source='auto', target='en').translate(text)
        print(f"Translated text: {translated_text}")
        
        return translated_text
    except Exception as e:
        print("An error occurred during translation:")
        traceback.print_exc()
        return text  # Return the original text in case of failure
```

This example demonstrates how the node detects and translates input language, handling errors if something goes wrong.

## Usage

Once installed, this node can be used within ComfyUI to allow inputs in various languages. When a non-English input is provided, it will be translated to English and then passed on for further processing by ComfyUI's workflow.

## Future Improvements

- **Multi-target Translation**: In future versions, we may introduce the ability to translate to other languages based on user preferences.
- **Improved Error Handling**: Enhance the robustness of error handling to cover more edge cases during translation.

## Contributing

Contributions are welcome! If you would like to contribute to the development of this node, feel free to open a pull request or submit issues for bug reports or feature requests.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.
