# freepbx_openai_tts
Custom Text to Speech Engines for Freepbx


modify /var/www/html/admin/modules/tts/agi-bin/propolys-tts.agi

mkdir /var/lib/asterisk/sounds/tts

chown asterisk:asterisk /var/lib/asterisk/sounds/tts

save openai.py to PATH like:
/etc/asterisk/tts/openai.py #change your PATH in propolys-tts.agi

INPUT your openai URL and KEY into openai.py!!!!

find your python path
/usr/bin/python3

go to admin website
https://www.abc.com/admin/config.php?display=ttsengines

settings >> Text to Speech Engines >> Add TTS Engine >> Engine Name >> Select [Custom] >> input [openai] >> Engine Path >> input [your python3 path] >> submit
