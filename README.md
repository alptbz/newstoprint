# Demo project - Fetch, Translate, and Output News

This minimal script is designed for demonstration purposes, showcasing how simple code can be structured.

To focus on simplicity, the applied structure has been intentionally streamlined and includes several code smells. These are deliberately introduced to keep the code concise and straightforward for demonstration purposes.

The script fetches news from the [Spaceflight News API](https://spaceflightnewsapi.net/) translates it using the [deep-translator](https://github.com/nidhaloff/deep-translator) library and output the news to [Webhook.site](https://webhook.site) and a [ESC/POS Printers](https://github.com/python-escpos/python-escpos)

## Requirements
 - Python3 3.9.* or newer
 - pip3

# Preparation
 - Clone repository to your device
```
git clone https://github.com/alptbz/newstoprint
```

 - Change into repository
```bash
cd newstoprint
```
 - Create venv
```bash
python -m venv env
```
 - Activate enviroment
```bash
# Linux:
source env/bin/activate

# Windows (PowerShell):
.\env\Scripts\activate

# Windows (bash):
source env/Scripts/activate
```
 - Install requirements
```bash
python -m pip install -r requirements.txt
```
 - Create own config.py and insert credentials and connection information
```bash
cp config.example.py config.py
vim config.py
```
 - Run
```bash
python main.py
```
## Notes
 - Use `python3` instead of `python` if you're using Linux

## License
<a rel="license" href="http://creativecommons.org/licenses/by-nc-sa/4.0/"><img alt="Creative Commons License" style="border-width:0" src="https://i.creativecommons.org/l/by-nc-sa/4.0/88x31.png" /></a><br />This work is licensed under a <a rel="license" href="http://creativecommons.org/licenses/by-nc-sa/4.0/">Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International License</a> and [GNU GENERAL PUBLIC LICENSE version 3](https://www.gnu.org/licenses/gpl-3.0.en.html). If there are any contradictions between the two licenses, the Attribution-NonCommercial-ShareAlike 4.0 International license governs. 
  
