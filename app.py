from flask import Flask, render_template, request, jsonify
import requests
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

app = Flask(__name__)

# Get API key from environment variable
FIXER_API_KEY = os.getenv('FIXER_API_KEY', 'your_api_key_here')
FIXER_BASE_URL = 'http://data.fixer.io/api/convert'

@app.route('/')
def index():
    """Main page with currency converter interface"""
    return render_template('index.html')

@app.route('/convert', methods=['POST'])
def convert_currency():
    """Handle currency conversion requests"""
    try:
        data = request.get_json()
        from_currency = data.get('from_currency')
        to_currency = data.get('to_currency')
        amount = data.get('amount')
        
        if not all([from_currency, to_currency, amount]):
            return jsonify({'error': 'Missing required parameters'}), 400
        
        # Make API request to Fixer.io
        params = {
            'access_key': FIXER_API_KEY,
            'from': from_currency,
            'to': to_currency,
            'amount': amount
        }
        
        # Debug: Print the request details
        print(f"🔍 Debug - API Request:")
        print(f"  URL: {FIXER_BASE_URL}")
        print(f"  Params: {params}")
        print(f"  API Key: {FIXER_API_KEY[:10]}..." if len(FIXER_API_KEY) > 10 else f"  API Key: {FIXER_API_KEY}")
        
        response = requests.get(FIXER_BASE_URL, params=params)
        
        # Debug: Print response details
        print(f"🔍 Debug - API Response:")
        print(f"  Status: {response.status_code}")
        print(f"  URL: {response.url}")
        print(f"  Content: {response.text[:200]}...")
        
        response.raise_for_status()
        
        result = response.json()
        
        if result.get('success'):
            return jsonify({
                'success': True,
                'result': result.get('result'),
                'from_currency': from_currency,
                'to_currency': to_currency,
                'amount': amount
            })
        else:
            return jsonify({
                'success': False,
                'error': result.get('error', {}).get('info', 'Conversion failed')
            }), 400
            
    except requests.exceptions.RequestException as e:
        return jsonify({'error': f'API request failed: {str(e)}'}), 500
    except Exception as e:
        return jsonify({'error': f'Server error: {str(e)}'}), 500

@app.route('/currencies')
def get_currencies():
    """Get list of available currencies"""
    currencies = {
        'USD': 'US Dollar',
        'EUR': 'Euro',
        'GBP': 'British Pound',
        'JPY': 'Japanese Yen',
        'AUD': 'Australian Dollar',
        'CAD': 'Canadian Dollar',
        'CHF': 'Swiss Franc',
        'CNY': 'Chinese Yuan',
        'INR': 'Indian Rupee',
        'BRL': 'Brazilian Real',
        'MXN': 'Mexican Peso',
        'SGD': 'Singapore Dollar',
        'HKD': 'Hong Kong Dollar',
        'NZD': 'New Zealand Dollar',
        'SEK': 'Swedish Krona',
        'KRW': 'South Korean Won',
        'RUB': 'Russian Ruble',
        'TRY': 'Turkish Lira',
        'ZAR': 'South African Rand',
        'PLN': 'Polish Złoty'
    }
    return jsonify(currencies)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8080) 