# Scrap.TF Raffle Bot

### NOTE: This tool was created for educational purposes only. Usage may result in a permanent ban of your Steam account from the Scrap.TF service. Use at your own risk.

---

Automation tool that enters item raffles on [Scrap.TF](https://scrap.tf/raffles), a bot trading site for Valve's Team Fortress 2.

This version uses the **Brave (Chromium)** browser together with **[undetected-chromedriver](https://pypi.org/project/undetected-chromedriver/)** in order to bypass detection.

---

## Installation & Usage

### Requirements
* Python 3.10+
* Selenium + undetected-chromedriver libraries  
  ```bash
  pip install selenium undetected-chromedriver
  ```
* Brave browser (Chromium-based)

---

### Running the script
Navigate into the project directory and run:

```
python main.py
```

You can also specify a custom interval (in seconds) for how often the bot checks for new raffles:

```
python main.py 120
```

The example above checks every 120 seconds (2 minutes).

On the first run you will be prompted to log in through Steam manually in the Brave browser.  
Once logged in and returned to the raffles page, press **Enter** in the console to continue.  
Your login will then be saved into a cookie file (`scr_session`) and will be automatically loaded in future runs.

---

## Features
* Save cookies to retain persistent login (**Completed**)
* Option to run for long periods of time with new raffle detection (**Completed**)
* Detect raffles that have been won, skip them and inform user (**Completed**)
* Random sleep intervals between actions to mimic human behavior
* Supports headless mode (invisible browser)

---

## Developed and tested with
* Windows 10
* Python 3.13
* Brave (Chromium)
* undetected-chromedriver 3.x
* Selenium 4.x
