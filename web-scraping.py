import os
import time
import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from PIL import Image
from io import BytesIO

chrome_options = Options()
chrome_options.add_argument("--headless")  # Run without GUI
chrome_options.add_argument("--no-sandbox")  # Bypass OS security model
chrome_options.add_argument("--disable-dev-shm-usage")

# Set up Selenium WebDriver
chrome_driver_path = "/usr/bin/chromedriver"  # Change this to your chromedriver path
service = Service(chrome_driver_path)
driver = webdriver.Chrome(service=service, options=chrome_options)

# Search for Lethal Company gameplay images
search_query = "lethal company hoarding bug"
url = f"https://www.google.com/search?q={search_query}&source=lnms&tbm=isch"
driver.get(url)

# Scroll to load more images
for _ in range(3):  # Adjust scroll range if needed
    driver.find_element(By.TAG_NAME, "body").send_keys(Keys.END)
    time.sleep(2)

# Get image elements
image_elements = driver.find_elements(By.CSS_SELECTOR, "img")

# Create folder for images
os.makedirs("images", exist_ok=True)

# Download images
for i, img in enumerate(image_elements[:20]):  # Adjust number of images
    img_url = img.get_attribute("src")
    if img_url and img_url.startswith("http"):
        response = requests.get(img_url)
        try:
            image = Image.open(BytesIO(response.content))
            image.verify()  # Ensure it's a real image
            image = Image.open(BytesIO(response.content))  # Reload to use
            image.save(f"images/lethal_company_{i}.png")
            print(f"Downloaded: lethal_company_{i}.png")
        except Exception as e:
            print(f"Skipping corrupted image: {img_url}, error: {e}")


# Close browser
driver.quit()
