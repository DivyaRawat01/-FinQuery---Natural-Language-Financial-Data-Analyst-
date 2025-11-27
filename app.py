import streamlit as st
import pandas as pd
import google.generativeai as genai
import matplotlib.pyplot as plt
import io
import sys

# ------------------------------------------------------------
# CONFIG
# ------------------------------------------------------------
GEMINI_API_KEY = "Your API KEy"
MODEL_NAME = "gemini-2.5-flash-lite"

st.set_page_config(layout="wide", page_title="FinQuery Dashboard")

# ------------------------------------------------------------
# Header
# ------------------------------------------------------------
st.title("💰 FinQuery - Financial Dashboard")
st.write("Upload your CSV file to analyze your expenses")
st.divider()

# ------------------------------------------------------------
# File Upload
# ------------------------------------------------------------
uploaded = st.file_uploader("Upload CSV File", type=["csv"])

if uploaded:
    df = pd.read_csv(uploaded)
    
    # Find important columns
    amount_col = None
    for col in df.columns:
        if "amount" in col.lower() or "price" in col.lower() or "cost" in col.lower():
            amount_col = col
            break
    
    date_col = None
    for col in df.columns:
        if "date" in col.lower():
            date_col = col
            break
    
    cat_col = None
    for col in df.columns:
        if "category" in col.lower():
            cat_col = col
            break
    
    # Quick Stats
    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric("Total Rows", f"{len(df):,}")
    with col2:
        st.metric("Columns", len(df.columns))
    if amount_col:
        with col3:
            st.metric("Total Amount", f"${df[amount_col].sum():,.2f}")
    
    st.divider()
    
    # ------------------------------------------------------------
    # Tabs for Organization
    # ------------------------------------------------------------
    tab1, tab2, tab3 = st.tabs(["📊 Charts", "🤖 AI Questions", "📁 Data"])
    
    # TAB 1: CHARTS
    with tab1:
        if not amount_col:
            st.warning("No amount column found in your CSV")
        else:
            col1, col2 = st.columns(2)
            
            # Monthly Spending Chart
            with col1:
                if date_col:
                    st.subheader("Monthly Spending")
                    df[date_col] = pd.to_datetime(df[date_col], errors="coerce")
                    df["Month"] = df[date_col].dt.to_period("M").astype(str)
                    monthly = df.groupby("Month")[amount_col].sum()
                    
                    fig, ax = plt.subplots(figsize=(5, 4))
                    monthly.plot(kind="bar", ax=ax, color='steelblue')
                    ax.set_ylabel("Amount ($)")
                    ax.set_xlabel("Month")
                    plt.xticks(rotation=45)
                    plt.tight_layout()
                    st.pyplot(fig)
                    plt.close()
                else:
                    st.info("Add a 'date' column to see monthly trends")
            
            # Category Breakdown Chart
            with col2:
                if cat_col:
                    st.subheader("Spending by Category")
                    category_sum = df.groupby(cat_col)[amount_col].sum().sort_values(ascending=False)
                    
                    fig, ax = plt.subplots(figsize=(5, 4))
                    category_sum.plot(kind="pie", ax=ax, autopct="%1.1f%%")
                    ax.set_ylabel("")
                    plt.tight_layout()
                    st.pyplot(fig)
                    plt.close()
                else:
                    st.info("Add a 'category' column to see breakdown")
    
    # TAB 2: AI ASSISTANT
    with tab2:
        st.subheader("Ask Questions About Your Data")
        
        st.write("**Try asking:**")
        suggestions = [
            "What is the total amount spent?",
            "Show average expense by category",
            "What was the highest expense?",
            "List transactions over $50",
            "Which category has most spending?",
            "Show top 5 expensive transactions"
        ]
        
        for s in suggestions:
            st.write(f" {s}")
        
        st.write("")
        user_query = st.text_input("Your question:")

        if st.button("Get Answer"):
            if not user_query:
                st.warning("Please enter a question")
            else:
                with st.spinner("Thinking..."):
                    try:
                        genai.configure(api_key=GEMINI_API_KEY)
                        model = genai.GenerativeModel(MODEL_NAME)

                        prompt = f"""
You are a Python Pandas expert. Generate ONLY executable Python code.
Dataset columns: {list(df.columns)}
User question: "{user_query}"
Rules:
- Use the DataFrame 'df'
- If visualization needed, use matplotlib
- Print results or show dataframe
- Use f-strings for money formatting
- No backticks, no imports
"""

                        response = model.generate_content(prompt)
                        code = response.text.strip()

                        if "```" in code:
                            code = code.replace("```python", "").replace("```", "").strip()

                        with st.expander("See Generated Code"):
                            st.code(code, language="python")

                        st.write("**Result:**")

                        stdout_buffer = io.StringIO()
                        sys_stdout_original = sys.stdout
                        sys.stdout = stdout_buffer

                        exec_globals = {"df": df, "pd": pd, "plt": plt, "st": st, "__builtins__": __builtins__}
                        exec_locals = {}

                        try:
                            exec(code, exec_globals, exec_locals)
                            sys.stdout = sys_stdout_original

                            output_text = stdout_buffer.getvalue()
                            if output_text.strip():
                                st.text(output_text)

                            fig = plt.gcf()
                            if fig.get_axes():
                                st.pyplot(fig)
                                plt.close()

                        except Exception as e:
                            sys.stdout = sys_stdout_original
                            st.error(f"Error: {e}")

                    except Exception as e:
                        st.error(f"Error: {e}")
    
    # TAB 3: DATA VIEW
    with tab3:
        st.subheader("Your Data")
        st.dataframe(df, use_container_width=True)
        
        csv = df.to_csv(index=False).encode('utf-8')
        

else:
    st.info("👆 Upload a CSV file to get started")
    st.write("")
    st.write("**What FinQuery does:**")
    st.write("* Automatically visualize your spending")
    st.write("* Ask questions in plain English")
    st.write("* Get instant insights about your finances")
