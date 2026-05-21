import requests
import time
import json
import os
import statistics

# Configuration
BASE_URL = "http://127.0.0.1:8000"
NUM_REQUESTS = 5
RESULTS_FILE = "performance_results.json"

# Define endpoints to test
# Note: Adjust the URLs below to match your actual Django endpoints
ENDPOINTS = [
    # 1. Measure how fast user requests are loading on the website
    {"name": "1. Website Home Page", "url": f"{BASE_URL}/", "method": "GET"},
    
    # 2. Test how fast the API is returning data
    # Testing an actual API endpoint in this project
    {"name": "2. API Data Return Speed (Profile)", "url": f"{BASE_URL}/api/profile/", "method": "GET"},
    
    # 3. Identify problems if the e-commerce checkout page is slow
    # (Placeholder endpoint: change this to your actual checkout URL if you add e-commerce functionality)
    {"name": "3. E-commerce Checkout Page", "url": f"{BASE_URL}/checkout/", "method": "POST", "payload": {"item_id": 1, "quantity": 1}},
]

def measure_speed(endpoint):
    print(f"\n--- Testing: {endpoint['name']} ---")
    times = []
    errors = 0
    
    for i in range(NUM_REQUESTS):
        start_time = time.time()
        try:
            if endpoint['method'] == "GET":
                response = requests.get(endpoint['url'], timeout=5)
            elif endpoint['method'] == "POST":
                payload = endpoint.get('payload', {})
                response = requests.post(endpoint['url'], json=payload, timeout=5)
            
            # Record errors if response status is 4xx or 5xx, but still count the time
            if not response.ok:
                errors += 1
                
        except requests.RequestException as e:
            errors += 1
            
        end_time = time.time()
        duration = end_time - start_time
        times.append(duration)
        
    avg_time = statistics.mean(times)
    max_time = max(times)
    min_time = min(times)
    
    print(f"Results for {endpoint['name']}:")
    print(f"  Average Time: {avg_time:.4f} seconds")
    print(f"  Max Time:     {max_time:.4f} seconds")
    print(f"  Min Time:     {min_time:.4f} seconds")
    print(f"  Errors:       {errors}/{NUM_REQUESTS} requests failed or returned error status")
    
    # 3. Identify problems if the e-commerce checkout page is slow
    if "Checkout" in endpoint['name'] and avg_time > 1.0:
         print(f"  [!] PROBLEM IDENTIFIED: The checkout page is very slow! Average time is over 1 second.")
         print(f"  -> Suggestions: Check database query optimization, external payment gateway latency, or caching.")
         
    return {
        "avg_time": avg_time,
        "max_time": max_time,
        "min_time": min_time,
        "errors": errors
    }

def run_tests():
    print("Starting Performance Tests...")
    current_results = {}
    
    for endpoint in ENDPOINTS:
        results = measure_speed(endpoint)
        current_results[endpoint['name']] = results
        
    return current_results

def compare_results(current_results):
    print("\n=======================================================")
    print("4. Comparing Speeds (Before vs After Optimization)")
    print("=======================================================")
    
    if not os.path.exists(RESULTS_FILE):
        print(f"No previous results found.")
        print(f"Saving current results to '{RESULTS_FILE}' as the 'before optimization' baseline.")
        with open(RESULTS_FILE, 'w') as f:
            json.dump(current_results, f, indent=4)
        print("Run this script again after optimizing your code to compare the speeds!")
        return
        
    with open(RESULTS_FILE, 'r') as f:
        previous_results = json.load(f)
        
    for name, current in current_results.items():
        if name in previous_results:
            prev = previous_results[name]
            diff = current['avg_time'] - prev['avg_time']
            diff_pct = (diff / prev['avg_time']) * 100 if prev['avg_time'] > 0 else 0
            
            status = "slower \u25bc" if diff > 0 else "faster \u25b2"
            
            print(f"\n{name}:")
            print(f"  Before: {prev['avg_time']:.4f}s")
            print(f"  After:  {current['avg_time']:.4f}s")
            print(f"  Result: {abs(diff):.4f}s {status} ({abs(diff_pct):.2f}%)")
        else:
            print(f"\n{name}: No previous data to compare.")
            
    print("\nDo you want to update the baseline with these new results for future tests?")
    print("If yes, delete 'performance_results.json' and run again, or modify the script to overwrite it.")

if __name__ == "__main__":
    # Ensure requests library is installed (pip install requests)
    try:
        import requests
    except ImportError:
        print("Please install the 'requests' library by running: pip install requests")
        exit(1)
        
    results = run_tests()
    compare_results(results)
