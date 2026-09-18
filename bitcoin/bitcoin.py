import sys
import requests

try:
    n = float(sys.argv[1])
    response = requests.get("https://rest.coincap.io/v3/assets/bitcoin?apiKey=1189101973f54867c39a0b8435c2b3b90cc9a894e2651090b8fd2b8afda3442d")
    obj = response.json()
    price = float(obj["data"]["priceUsd"])
    print(f"${price * n :,.4f}")

except IndexError:
    sys.exit("Missing command-line argument")
except ValueError:
    sys.exit("Command-line argument is not a number")
except requests.RequestException:
    sys.exit("API request failed")
except KeyError:
    sys.exit("Invalid API response")
