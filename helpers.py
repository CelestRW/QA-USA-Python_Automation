import time
import json
from selenium.webdriver.common.by import By



def is_url_reachable(url):
    from urllib.request import urlopen
    try:
        response = urlopen(url)
        return response.status == 200
    except:
        return False

def retrieve_phone_code(driver):
    time.sleep(3)
    logs = driver.get_log("performance")

    for log in logs:
        message = json.loads(log["message"])["message"]
        if(
            message["method"] == "Network.responseReceived"
            and "sms-code" in str(message)
        ):
            try:
                url = message["params"]["response"]["url"]
                if "sms-code" in url:
                    code = url.split("sms-code=")[-1][:4]
                    return code
            except:
                pass
    return None
