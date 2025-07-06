#!/usr/bin/env python3
"""
Simple test script for the Currency Converter application
"""

import requests
import json
import time

def test_currencies_endpoint():
    """Test the currencies endpoint"""
    print("Testing /currencies endpoint...")
    try:
        response = requests.get('http://localhost:8080/currencies')
        if response.status_code == 200:
            currencies = response.json()
            print(f"✅ Success! Found {len(currencies)} currencies")
            print(f"Sample currencies: {list(currencies.keys())[:5]}")
            return True
        else:
            print(f"❌ Failed with status code: {response.status_code}")
            return False
    except requests.exceptions.ConnectionError:
        print("❌ Could not connect to server. Make sure the app is running.")
        return False

def test_convert_endpoint():
    """Test the convert endpoint (without API key)"""
    print("\nTesting /convert endpoint...")
    try:
        data = {
            'from_currency': 'USD',
            'to_currency': 'EUR',
            'amount': 100
        }
        response = requests.post(
            'http://localhost:8080/convert',
            json=data,
            headers={'Content-Type': 'application/json'}
        )
        
        if response.status_code == 200:
            result = response.json()
            if result.get('success'):
                print("✅ Conversion successful!")
                print(f"Result: {result.get('result')}")
                return True
            else:
                print(f"❌ Conversion failed: {result.get('error')}")
                return False
        else:
            print(f"❌ Request failed with status code: {response.status_code}")
            return False
    except requests.exceptions.ConnectionError:
        print("❌ Could not connect to server. Make sure the app is running.")
        return False

def main():
    """Run all tests"""
    print("🧪 Testing Currency Converter Application")
    print("=" * 50)
    
    # Wait a moment for the server to start
    print("Waiting for server to be ready...")
    time.sleep(2)
    
    # Test endpoints
    currencies_ok = test_currencies_endpoint()
    convert_ok = test_convert_endpoint()
    
    print("\n" + "=" * 50)
    if currencies_ok and convert_ok:
        print("🎉 All tests passed! Application is working correctly.")
    else:
        print("⚠️  Some tests failed. Check the application setup.")
    
    print("\nNote: The convert test may fail if no API key is configured.")
    print("This is expected behavior for security reasons.")

if __name__ == '__main__':
    main() 