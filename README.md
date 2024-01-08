# freepbx_openai_tts
Custom Text to Speech Engines for Freepbx


modify /var/www/html/admin/modules/tts/agi-bin/propolys-tts.agi

mkdir /var/lib/asterisk/sounds/tts
chown asterisk:asterisk /var/lib/asterisk/sounds/tts

save openai.py

which python3 find python path
/usr/bin/python3

go to website
https://www.abc.com/admin/config.php?display=ttsengines

settings >> Text to Speech Engines >> Add TTS Engine >> Engine Name >> Select [Custom] >> input [openai] >> Engine Path >> input [your python3 path] >> submit
