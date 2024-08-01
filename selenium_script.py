from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import json

# Setup WebDriver (Ensure ChromeDriver or appropriate WebDriver is installed)
driver = webdriver.Chrome()  # or use webdriver.Firefox() if using Firefox

try:
    # Open the local web server
    driver.get("http://localhost:5000")
    
    # Find the input field and submit button
    ip_range_input = driver.find_element(By.ID, "ipRange")
    submit_button = driver.find_element(By.XPATH, "//button[@type='submit']")
    
    # Enter IP range and submit the form
    ip_range_input.send_keys("192.168.212.1/24")
    submit_button.click()
    
    # Wait for results to load
    time.sleep(5)
    
    # Extract the results
    results = driver.find_element(By.TAG_NAME, 'pre').text
    results_json = json.loads(results)
    
    # Print the results
    for client in results_json:
        print(f"IP: {client['ip']}, MAC: {client['mac']}")

finally:
    driver.quit()
