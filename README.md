# -FinQuery---Natural-Language-Financial-Data-Analyst-
AI-powered financial data analyst - Ask questions in natural language, get Pandas code &amp; results
# 💰 FinQuery - Natural Language Financial Data Analyst

[![Python 3.8+](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![Streamlit](https://img.shields.io/badge/Streamlit-1.28+-FF4B4B.svg)](https://streamlit.io)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

Ask questions about your financial data in plain English and get instant Pandas code + results powered by Google Gemini AI!

![FinQuery Demo](https://via.placeholder.com/800x400/1E88E5/FFFFFF?text=FinQuery+Demo)

## 🌟 Features

- 🤖 **AI-Powered Analysis** - Uses Google Gemini AI to understand natural language queries
- 📊 **Instant Results** - Get Pandas code and analysis results in seconds
- 💡 **Smart Suggestions** - Pre-built queries for common financial questions
- 📜 **Query History** - Track all your previous analyses
- 🎨 **Beautiful UI** - Clean, modern Streamlit interface
- 🔒 **Secure** - Your data stays local, only queries are sent to Gemini

## 🚀 Quick Start

### Prerequisites

- Python 3.8 or higher
- Gemini API key ([Get it free here](https://makersuite.google.com/app/apikey))

### Installation

1. **Clone the repository**
```bash
git clone https://github.com/yourusername/finquery.git
cd finquery
```

2. **Install dependencies**
```bash
pip install -r requirements.txt
```

3. **Run the Streamlit app**
```bash
streamlit run app.py
```

4. **Or run the CLI version**
```bash
python finquery.py
```

## 📁 Project Structure

```
finquery/
├── app.py              # Streamlit web application
├── finquery.py         # CLI version
├── expenses.csv        # Sample financial data
├── requirements.txt    # Python dependencies
└── README.md          # This file
```

## 💻 Usage

### Web App (Streamlit)

1. Launch the app: `streamlit run app.py`
2. Enter your Gemini API key in the sidebar
3. Upload your CSV file
4. Ask questions or use quick suggestions
5. View generated code and results!

### CLI Version

1. Update API key in `finquery.py`
2. Run: `python finquery.py`
3. Type questions or enter numbers (1-8) for suggestions
4. Type `quit` to exit

## 📊 Sample Queries

- "What is the total amount spent?"
- "Show me the average expense by category"
- "What was the highest single expense?"
- "List all transactions where the amount is over $50"
- "Show the total expenses for the 'Food' category"
- "Group expenses by category and show totals"
- "What percentage of spending is on groceries?"
- "Show me the top 3 most expensive transactions"

## 📄 CSV Format

Your CSV file should have these columns:

```csv
date,description,amount,category
2024-01-05,Starbucks Coffee,6.50,Food
2024-01-07,Shell Gas Station,45.00,Transport
2024-01-08,Walmart Groceries,120.75,Groceries
```

**Required columns:**
- `date` - Transaction date
- `description` - Transaction description
- `amount` - Transaction amount (numeric)
- `category` - Expense category

## 🛠️ Technologies Used

- **Python 3.8+** - Programming language
- **Streamlit** - Web framework
- **Pandas** - Data analysis
- **Google Gemini AI** - Natural language processing
- **NumPy** - Numerical computing

## 📦 Dependencies

```txt
streamlit>=1.28.0
pandas>=2.0.0
google-generativeai>=0.3.0
numpy>=1.24.0
```

## 🔑 Getting Gemini API Key

1. Visit [Google AI Studio](https://makersuite.google.com/app/apikey)
2. Sign in with your Google account
3. Click "Create API Key"
4. Copy your API key
5. Paste it in the app sidebar or update `finquery.py`

**Note:** The API key is free with usage limits. Check [pricing](https://ai.google.dev/pricing) for details.

## 🎯 Use Cases

- 📈 Personal finance tracking
- 💳 Credit card expense analysis
- 🏦 Bank statement analysis
- 📊 Budget monitoring
- 💰 Spending pattern discovery
- 🎓 Learning Pandas through examples

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 👨‍💻 Author

**Your Name**
- GitHub: [GitHub](https://github.com/DivyaRawat01/)
- LinkedIn:[LinkedIn](https://www.linkedin.com/in/divya-rawat-053940341/)

## 🙏 Acknowledgments

- Google Gemini AI for powering the natural language processing
- Streamlit for the amazing web framework
- Pandas community for the powerful data analysis tools

## 📧 Contact

Have questions or suggestions? Feel free to reach out!

- Email: rawatdivya072@gmail.com
- GitHub Issues: [Create an issue](https://github.com/divyarawat01/finquery/issues)

---

⭐ If you found this project helpful, please give it a star!

Made with ❤️ by Divya
