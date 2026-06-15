# 💱 Advanced Currency Converter

A Python-based currency converter that fetches real-time exchange rates and supports conversion between multiple international currencies using the Frankfurter Exchange Rate API.

## 🚀 Features

* Real-time currency conversion
* Supports dozens of international currencies
* Displays all available currency codes
* User-friendly command-line interface (CLI)
* Input validation
* Network and API error handling
* Lightweight and easy to use

## 📂 Project Structure

```bash
.
├── sit.py
├── requirements.txt
└── README.md
```

## 🛠️ Technologies Used

* Python 3
* Requests Library
* Frankfurter Exchange Rate API

## 📦 Installation

### Clone the Repository

```bash
git clone https://github.com/yourusername/advanced-currency-converter.git
cd advanced-currency-converter
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

## ▶️ Usage

Run the application:

```bash
python sit.py
```

You will see:

```text
====================================
      ADVANCED CURRENCY CONVERTER
====================================
1. Convert Currency
2. Show Available Currency Codes
3. Exit
```

### Example Conversion

```text
Enter amount: 100
From Currency Code: USD
To Currency Code: INR
```

Output:

```text
100.00 USD
↓
8550.00 INR
```

## 🌍 Supported Currencies

The application automatically fetches supported currencies from the API, including:

* USD – United States Dollar
* INR – Indian Rupee
* EUR – Euro
* GBP – British Pound
* JPY – Japanese Yen
* AUD – Australian Dollar
* CAD – Canadian Dollar

and many more.

## ⚠️ Error Handling

The application handles:

* Invalid currency codes
* Invalid numeric input
* Internet connectivity issues
* API timeouts
* Unexpected API errors

## 🔗 API Used

Frankfurter Exchange Rate API

https://www.frankfurter.app/

## 📈 Future Improvements

* GUI using Tkinter or PyQt
* FastAPI REST API version
* Historical exchange rate analysis
* Currency trend visualization
* AI-based exchange rate prediction
* Voice-based currency conversion

## 🤝 Contributing

Contributions are welcome.

1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Push to your branch
5. Open a Pull Request

## 📄 License

This project is open-source and available under the MIT License.

## 👨‍💻 Author

Swaroop
