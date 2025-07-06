# Currency Converter

A modern, responsive web application for converting currencies using real-time exchange rates from the Exchange Rate API.

## Features

- 🎨 **Modern UI**: Beautiful, responsive design with smooth animations
- 💱 **Real-time Conversion**: Live currency conversion using Fixer.io API
- 🔄 **Quick Swap**: One-click currency swap functionality
- 📱 **Mobile Friendly**: Responsive design that works on all devices
- ⚡ **Fast**: Optimized for quick conversions
- 🛡️ **Error Handling**: Comprehensive error handling and user feedback

## Screenshots

The application features a clean, modern interface with:
- Gradient background with glassmorphism effect
- Intuitive form controls
- Real-time conversion results
- Loading states and error handling

## Prerequisites

- Python 3.7 or higher
- No API key required (uses free Exchange Rate API)

## Installation

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd currencyConverter
   ```

2. **Create a virtual environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Ready to run!** No API key setup required.

## Usage

1. **Start the application**
   ```bash
   python app.py
   ```

2. **Open your browser**
   Navigate to `http://localhost:8080`

3. **Convert currencies**
   - Select the source currency
   - Enter the amount
   - Select the target currency
   - Click "Convert" or use the swap button to reverse currencies

## API Endpoints

- `GET /` - Main application page
- `POST /convert` - Convert currency (requires JSON payload)
- `GET /currencies` - Get list of available currencies

### Convert Currency Example

```bash
curl -X POST http://localhost:8080/convert \
  -H "Content-Type: application/json" \
  -d '{
    "from_currency": "USD",
    "to_currency": "EUR",
    "amount": 100
  }'
```

## Supported Currencies

The application supports 20 major currencies including:
- USD (US Dollar)
- EUR (Euro)
- GBP (British Pound)
- JPY (Japanese Yen)
- AUD (Australian Dollar)
- CAD (Canadian Dollar)
- CHF (Swiss Franc)
- CNY (Chinese Yuan)
- INR (Indian Rupee)
- And many more...

## Project Structure

```
currencyConverter/
├── app.py              # Main Flask application
├── templates/
│   └── index.html      # Frontend template
├── requirements.txt    # Python dependencies
├── env.example         # Environment variables template
├── .env               # Your environment variables (create this)
└── README.md          # This file
```

## Technologies Used

- **Backend**: Python Flask
- **Frontend**: HTML5, CSS3, JavaScript (ES6+)
- **API**: Exchange Rate API (free, no key required)
- **Styling**: Custom CSS with modern design patterns
- **Icons**: Font Awesome
- **Fonts**: Inter (Google Fonts)

## Development

To run in development mode with auto-reload:

```bash
export FLASK_ENV=development
python app.py
```

## Error Handling

The application includes comprehensive error handling for:
- Invalid API responses
- Network errors
- Missing or invalid input
- API rate limiting

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Test thoroughly
5. Submit a pull request

## License

This project is open source and available under the [MIT License](LICENSE).

## Support

If you encounter any issues:
1. Verify your internet connection
2. Ensure all dependencies are installed
3. Check the browser console for any JavaScript errors
4. The Exchange Rate API is free and doesn't require authentication

## Future Enhancements

- [ ] Historical exchange rates
- [ ] Currency charts and graphs
- [ ] Offline mode with cached rates
- [ ] Multiple currency conversion
- [ ] Export conversion history
- [ ] Dark mode toggle