import streamlit as st
from db import db_utils

def main():
    st.title('LTE KPI Dashboard')

    conn = db_utils.get_connection()
    conn.close()

if __name__ == "__main__":
    main()
