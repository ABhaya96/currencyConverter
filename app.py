from flask import Flask, render_template, request, jsonify
import requests

app = Flask(__name__)

# Exchange Rate API (free, no API key required)
EXCHANGE_API_BASE_URL = 'https://api.exchangerate-api.com/v4/latest'

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
        
        # Make API request to Exchange Rate API
        api_url = f"{EXCHANGE_API_BASE_URL}/{from_currency}"
        
        # Debug: Print the request details
        print(f"🔍 Debug - API Request:")
        print(f"  URL: {api_url}")
        print(f"  From Currency: {from_currency}")
        print(f"  To Currency: {to_currency}")
        print(f"  Amount: {amount}")
        
        response = requests.get(api_url)
        
        # Debug: Print response details
        print(f"🔍 Debug - API Response:")
        print(f"  Status: {response.status_code}")
        print(f"  URL: {response.url}")
        print(f"  Content: {response.text[:200]}...")
        
        response.raise_for_status()
        
        result = response.json()
        
        if response.status_code == 200 and 'rates' in result:
            # Calculate conversion
            base_rate = result['rates'].get(to_currency)
            if base_rate:
                converted_amount = float(amount) * base_rate
                return jsonify({
                    'success': True,
                    'result': converted_amount,
                    'from_currency': from_currency,
                    'to_currency': to_currency,
                    'amount': amount,
                    'rate': base_rate
                })
            else:
                return jsonify({
                    'success': False,
                    'error': f'Currency {to_currency} not found in rates'
                }), 400
        else:
            return jsonify({
                'success': False,
                'error': 'Failed to fetch exchange rates'
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