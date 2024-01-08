import requests
import os
import sys

def info():
    # check 2 args
    if len(sys.argv) != 3:
        print("2 args")
        sys.exit(1)

    # args
    text_tts = sys.argv[1]
    engine_tts_hash = sys.argv[2]


    return text_tts, engine_tts_hash

    # openai tts
def openai_TTS(text_tts, engine_tts_hash):
    open_ai_api_base = 'OPENAI_URL'#offical or your own both ok
    open_ai_api_key = "OPENAI_KEY"  # Replace with your OpenAI API key
    text_to_voice_model = "tts-1"
    tts_voice_id = "onyx"
    headers = {'Authorization': 'Bearer ' + open_ai_api_key}
    data = {'model': text_to_voice_model, 'input': text_tts, 'voice': tts_voice_id}

    response = requests.post(open_ai_api_base, headers=headers, json=data)
    file_path = f"/var/lib/asterisk/sounds/tts/{engine_tts_hash}.mp3"

    with open(file_path, 'wb') as f:
        f.write(response.content)

    sln_path = file_path.replace(".mp3", "")
    os.system(f"/usr/bin/sox {file_path} -t raw -r 8000 -b 16 -c 1 {sln_path}.sln")

# run
if __name__ == '__main__':
    text_tts, engine_tts_hash = info()
    openai_TTS(text_tts, engine_tts_hash)
