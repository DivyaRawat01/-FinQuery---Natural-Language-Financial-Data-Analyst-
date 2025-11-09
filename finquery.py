
import pandas as pd
import google.generativeai as genai

# Configure Gemini API
GEMINI_API_KEY = "AIzaSyDIfVhj5aM0RCKje9mzqSqcdhniaBG6JCA"
genai.configure(api_key=GEMINI_API_KEY)
model = genai.GenerativeModel('gemini-2.0-flash-exp')

# Load your CSV file 
df = pd.read_csv(r"E:\project\Sem project DS\Python\expenses.csv")

SUGGESTIONS = [
    "What is the total amount spent?",
    "Show me the average expense by category.",
    "What was the highest single expense?",
    "List all transactions where the amount is over $50.",
    "Show the total expenses for the 'Food' category.",
    "Group expenses by category and show totals",
    "What percentage of spending is on groceries?",
    "Show me the top 3 most expensive transactions"
]

print("=" * 60)
print("FinQuery - Ask questions about your financial data")
print("=" * 60)
print(f"\nLoaded: {len(df)} rows")
print(f"Columns: {list(df.columns)}")
print()

while True:
    print("\n" + '*'*200)
    print("👉 Try these sample queries:")
    suggestion = ""
    for i, suggestion in enumerate(SUGGESTIONS, 1):
        print(f"  {i}. {suggestion}")
    print("=" * 60)
    
    # Get user query
    query = input("\n💬 Ask a question (or 'quit' to exit): ").strip()
    # Check if user entered a number
    if query.isdigit():
        num = int(query)
        if 1 <= num <= len(SUGGESTIONS):
            query = SUGGESTIONS[num - 1]
            print(f"✅ Selected: {query}")
        else:
            print(f"❌ Invalid number. Please enter 1-{len(SUGGESTIONS)}")
            continue
    if query.lower() in ['quit', 'exit', 'q']:
        print("\n👋 Goodbye!")
        break
    
    if not query:
        continue
    
    # Create prompt for Gemini
    prompt = f"""You are a Python Pandas expert. Generate ONLY executable Python code.

Dataset columns: {list(df.columns)}
Sample data: {df.head(2).to_dict('records')}

User question: "{query}"

Generate Python code that:
- Uses the DataFrame variable 'df'
- Answers the user's question
- Prints the result with nice formatting
- Uses f-strings for currency formatting
- Handles errors gracefully

Return ONLY the code, no explanations or markdown blocks.

Example format:
result = df['amount'].sum()
print(f'Total: ${{result:,.2f}}')
"""
    
    try:
        print("\n🤖 Generating code with Gemini AI...")
        
        # Get code from Gemini
        response = model.generate_content(prompt)
        code = response.text.strip()
        
        # Clean up markdown if present
        if '```python' in code:
            code = code.split('```python')[1].split('```')[0].strip()
        elif '```' in code:
            code = code.split('```')[1].split('```')[0].strip()
        
        
        # Execute code
        print("\n📊 Result:")
        print("-" * 60)
        exec(code, {'df': df, 'pd': pd})
        print("-" * 60)
        
    except Exception as e:
        print(f"\n❌ Error: {e}")
        print("Try rephrasing your question or use one of the suggestions above.\n")