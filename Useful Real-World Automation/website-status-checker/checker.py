import requests

url = input("Enter website URL: ")

try:
    response = requests.get(url)

    if response.status_code == 200:
        print("✅ Website is UP")
    else:
        print("⚠️ Website returned status code:", response.status_code)

except requests.exceptions.RequestException:
    print("❌ Website is DOWN or unreachable")