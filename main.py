import requests
from colorama import Fore

def check_ltc_balance(address, api_token):
    if not address:
        return "Error: Litecoin address is required."
    
    url = f"https://api.blockcypher.com/v1/ltc/main/addrs/{address}/balance?token={api_token}"
    
    try:
        response = requests.get(url)
        response.raise_for_status()  
        data = response.json()
        balance = data.get("balance", 0) / 1e8  # หน่วย satoshi -> LTC
        return balance
    except requests.exceptions.HTTPError as http_err:
        return f"HTTP error occurred: {http_err}"
    except Exception as err:
        return f"Other error occurred: {err}"
    
ltc_address = input('Your LTC Address: ')
api_token = ""

balance = check_ltc_balance(ltc_address, api_token)
print(f"Balance for {Fore.LIGHTYELLOW_EX}{ltc_address}{Fore.RESET} = {Fore.GREEN}{balance}{Fore.RESET} LTC")
