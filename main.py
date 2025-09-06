import sys
import util
import undetected_chromedriver as uc
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import time

# Time parameters
wait_page_load = 10
wait_between_raffles_min = 3.5
wait_between_raffles_max = 9.5

check_interval = 300

if len(sys.argv) > 1:
    try:
        check_interval = int(sys.argv[1])
    except ValueError:
        print("Invalid interval provided, using default 300 seconds.")

options = uc.ChromeOptions()
options.binary_location = r"C:\Program Files\BraveSoftware\Brave-Browser\Application\brave.exe"

undetected-chromedriver
driver = uc.Chrome(options=options)

def login_and_load():
    driver.get('https://scrap.tf/raffles')
    found_cookie = None
    try:
        found_cookie = util.cookie_read('scr_session')
    except Exception:
        print("Cookie file is invalid or missing. Will create a new one after login.")

    if not found_cookie:
        print('Please sign in through Steam, then press enter to begin...')
        input()
        found_cookie = driver.get_cookies()
        util.cookie_write('scr_session', found_cookie)
        print('Saved login to cookie file, scr_session')
    else:
        print('Found login cookie file.')
        for c in found_cookie:
            driver.add_cookie(c)

    driver.refresh()

    if not driver.find_elements(By.XPATH, '//li[@class="dropdown nav-userinfo"]'):
        print('Steam login not detected!', file=sys.stderr)
        sys.exit(1)

def load_all_raffles():
    while not driver.find_elements(By.XPATH, '//*[contains(text(), "That\'s all, no more!")]')[0].is_displayed():
        print('Loading more raffles...')
        driver.execute_script('window.scrollTo(0, document.body.scrollHeight - 200)')
        util.random_sleep(0.5, 1.5)

    anchor_list = driver.find_elements(By.XPATH, '//div[@class="panel-raffle "]/div/div/a')
    return [anchor.get_attribute('href') for anchor in anchor_list]

def process_raffles(raffles):
    print('\nFound', len(raffles), 'unentered raffles!')
    for raffle in raffles:
        driver.get(raffle)

        # Skip raffles already won
        if driver.find_elements(By.XPATH, '//div[contains(@class, "raffle-won")]'):
            print(f"Skipping {raffle} - already won.")
            continue

        try:
            WebDriverWait(driver, wait_page_load).until(
                EC.element_to_be_clickable((By.XPATH, '//div[contains(@class, "enter-raffle-btns")][1]'))
            ).click()
        except TimeoutException:
            print(f'Raffle entry button could not be found for {raffle}...', file=sys.stderr)
            continue
        except Exception as exception:
            print(f'Unexpected exception on {raffle}...', str(exception), file=sys.stderr)
        else:
            print(f'Entered raffle: {raffle}')

        util.random_sleep(wait_between_raffles_min, wait_between_raffles_max)

print(f"Starting raffle bot in long-running mode. Checking every {check_interval} seconds.")
login_and_load()

while True:
    raffles = load_all_raffles()
    process_raffles(raffles)
    print("\nCycle complete. Waiting for new raffles...")
    time.sleep(check_interval)
    driver.get('https://scrap.tf/raffles')
