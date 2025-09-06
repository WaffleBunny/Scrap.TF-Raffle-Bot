import random
import time
import os.path

def random_sleep(time_min: float, time_max: float) -> None:
    '''
    Sleep for a random amount of time within an interval.

    Parameters:
        time_min (float): Lower time interval bound
        time_max (float): Upper time interval bound
    '''

    time_to_sleep = random.uniform(time_min, time_max)
    time.sleep(time_to_sleep)


def cookie_read(filename: str):
    '''
    Reads a list of cookies (dictionaries) from a file. If the file does
    not exist, the function will return None.

    Parameters:
        filename (str): Path to the cookie file
    
    Returns:
        list: List of cookies that can be loaded using Selenium's add_cookie()
    ''' 

    if not os.path.exists(filename):
        return None

    with open(filename, 'r') as cookie_file:
        cookie_data = eval(cookie_file.read())

    if not isinstance(cookie_data, list):
        raise Exception('Cookie file ' + filename + ' could not be evaluated to a list of cookies')

    return cookie_data
    

def cookie_write(filename: str, cookies: list) -> None:
    '''
    Writes a list of cookies (dictionaries) to a file. If the file does
    not exist, it will be created. If a file already exists, it will be
    overwritten.

    Parameters:
        filename (str): Path to the cookie file
        cookies (list): List of cookie dictionaries
    '''

    with open(filename, 'w') as cookie_file:
        cookie_file.write(str(cookies))
