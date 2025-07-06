# Currency Converter

A modern, responsive web application for converting currencies using real-time exchange rates from the Fixer.io API.

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
- A Fixer.io API key (free tier available)

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

4. **Set up environment variables**
   ```bash
   cp env.example .env
   ```
   
   Edit `.env` and add your Fixer.io API key:
   ```
   FIXER_API_KEY=your_actual_api_key_here
   ```

## Getting an API Key

1. Visit [Fixer.io](https://fixer.io/)
2. Sign up for a free account
3. Get your API key from the dashboard
4. Add it to your `.env` file

## Usage

1. **Start the application**
   ```bash
   python app.py
   ```

2. **Open your browser**
   Navigate to `http://localhost:5000`

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
curl -X POST http://localhost:5000/convert \
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
- **API**: Fixer.io Currency API
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
1. Check that your API key is correctly set in the `.env` file
2. Verify your internet connection
3. Ensure all dependencies are installed
4. Check the browser console for any JavaScript errors

## Future Enhancements

- [ ] Historical exchange rates
- [ ] Currency charts and graphs
- [ ] Offline mode with cached rates
- [ ] Multiple currency conversion
- [ ] Export conversion history
- [ ] Dark mode toggle