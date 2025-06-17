# app.py
import streamlit as st
import re
import random
import mysql.connector as mc
import pandas as pd
from prediction import predict_url

# Database connection
def get_db_connection():
    try:
        connection = mc.connect(
            host='localhost',
            user='root',
            password='rajnandhu04',
            database='detect_phishing'
        )
        db_cursor = connection.cursor()
        
        # Create table if not exists
        create_sql = '''CREATE TABLE IF NOT EXISTS `blocked_urls`
                      ( `url_id` int(11) NOT NULL AUTO_INCREMENT, 
                       `url_text` varchar(100) NOT NULL,
                       `url_ip` varchar(45) DEFAULT NULL, 
                       PRIMARY KEY (`url_id`))
                       ENGINE=InnoDB AUTO_INCREMENT=12 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;'''
        
        db_cursor.execute(create_sql)
        return connection, db_cursor
    except Exception as e:
        st.error(f"Database connection error: {e}")
        return None, None

# Insert URL to database
def insert_to_db(url_val):
    connection, db_cursor = get_db_connection()
    if connection and db_cursor:
        try:
            ip = ".".join('%s' % random.randint(10, 190) for i in range(4))
            db_cursor.execute(
                "INSERT INTO blocked_urls (url_text, url_ip) VALUES (%s, %s);",
                (url_val, ip)
            )
            connection.commit()
            st.success("URL blocked successfully!")
        except Exception as e:
            st.error(f"Error inserting to database: {e}")
        finally:
            db_cursor.close()
            connection.close()

# Fetch blocked URLs
def fetch_blocked_urls():
    connection, db_cursor = get_db_connection()
    if connection and db_cursor:
        try:
            db_cursor.execute('SELECT * FROM blocked_urls;')
            rows = db_cursor.fetchall()
            return rows
        except Exception as e:
            st.error(f"Error fetching data: {e}")
            return []
        finally:
            db_cursor.close()
            connection.close()
    return []

# Main app
def main():
    st.title("Phishing Detection using Machine Learning")
    
    
    # URL input
    url_input = st.text_input("Enter URL to check:", "")
    
    if st.button("Check URL"):
        if not url_input:
            st.warning("Please enter a URL")
        else:
            # Validate URL format
            url_valid = re.findall(
                'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\), ]|(?:%[0-9a-fA-F][0-9a-fA-F]))+',
                url_input
            )
            
            if not url_valid:
                st.error("Please enter a valid URL")
            else:
                # Predict URL
                predicted_value = predict_url(url_input)
                url_status = predicted_value[0].lower()
                
                # Display result
                if url_status == 'good':
                    st.success(f"Entered URL: {url_input} is legitimate")
                elif url_status == 'bad':
                    st.error(f"Entered URL: {url_input} is malicious")
                    if st.button("Block URL"):
                        insert_to_db(url_input)
                else:
                    st.warning("A problem was encountered while checking the URL")
    
    # Display blocked URLs
    st.subheader("Blocked URLs")
    blocked_urls = fetch_blocked_urls()
    if blocked_urls:
        df = pd.DataFrame(blocked_urls, columns=["ID", "URL", "IP Address"])
        st.dataframe(df)
    else:
        st.info("No URLs have been blocked yet")

if __name__ == "__main__":
    main()
