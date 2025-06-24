from nicegui import ui
import ollama

LANGUAGES = ['Python', 'Java', 'C++', 'JavaScript', 'C#']

def convert_code(code: str, source_lang: str, target_lang: str) -> str:
    prompt = (
        f"Convert the following {source_lang} code to {target_lang}:\n\n"
        f"### {source_lang} code:\n{code}\n\n"
        f"### {target_lang} version:"
    )
    try:
        response = ollama.chat(
            model='starcoder',
            messages=[{'role': 'user', 'content': prompt}]
        )
        return response['message']['content'].strip()
    except Exception as e:
        return f"❌ Error: {e}"

ui.label('💻 Code Language Converter using StarCoder').classes('text-2xl font-bold my-4 text-center')

with ui.row().classes('w-full justify-between items-start'):

    with ui.column().classes('w-1/2 px-4'):
        ui.label('🔡 Input Code').classes('text-lg font-semibold')
        input_code = ui.textarea(label='Your Code', placeholder='Paste your code here...').classes('w-full')
        from_lang = ui.select(LANGUAGES, label='From Language').classes('w-full')

    with ui.column().classes('w-1/2 px-4'):
        ui.label('🧾 Converted Code').classes('text-lg font-semibold')
        converted_code = ui.textarea(label='').classes('w-full')
        to_lang = ui.select(LANGUAGES, label='To Language').classes('w-full')

def on_convert():
    if not input_code.value:
        converted_code.value = "❗ Please enter some code to convert."
    elif from_lang.value == to_lang.value:
        converted_code.value = "❗ Source and target languages must be different."
    else:
        converted_code.value = convert_code(input_code.value, from_lang.value, to_lang.value)

ui.button('🔁 Convert', on_click=on_convert, color='green').classes('my-4')

ui.run(title='Code Language Converter')
