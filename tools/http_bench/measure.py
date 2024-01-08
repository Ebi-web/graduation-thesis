from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from concurrent.futures import ThreadPoolExecutor, as_completed
import numpy as np
import time


def load_website_and_measure(url):
    try:
        options = webdriver.ChromeOptions()
        options.add_argument('--headless')
        driver = webdriver.Chrome(options=options)
        start_time = time.time()

        try:
            driver.get(url)
            WebDriverWait(driver, 10).until(
                EC.visibility_of_all_elements_located((By.TAG_NAME, "img"))
            )
        finally:
            driver.quit()

        return time.time() - start_time, None
    except Exception as e:
        return None, e


def calculate_statistics(load_times, errors):
    load_times_array = np.array([time for time in load_times if time is not None])
    mean = np.mean(load_times_array)
    variance = np.var(load_times_array)
    throughput = len(load_times_array) / np.sum(load_times_array)
    failures = len(errors)

    print(f"Average Load Time: {mean} seconds")
    print(f"Variance of Load Time: {variance} seconds^2")
    print(f"Throughput: {throughput} requests/second")
    print(f"Number of Failures: {failures}")


def main():
    test_url = "http://localhost:8081"
    num_requests = 1000
    num_parallel = 50

    load_times = []
    errors = []
    with ThreadPoolExecutor(max_workers=num_parallel) as executor:
        future_to_url = {executor.submit(load_website_and_measure, test_url): url for url in range(num_requests)}
        for future in as_completed(future_to_url):
            load_time, error = future.result()
            if load_time is not None:
                load_times.append(load_time)
            if error is not None:
                errors.append(error)

    calculate_statistics(load_times, errors)


if __name__ == "__main__":
    main()
