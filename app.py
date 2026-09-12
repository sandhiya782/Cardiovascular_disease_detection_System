import streamlit as st
import mysql.connector
from fpdf import FPDF
from io import BytesIO
import base64
import pandas as pd
from joblib import load
# Load model
model = load("heart_disease_model.joblib")


# Use CSS to set a background image from URL
def set_bg_image_from_url(image_url):
    css = f"""
    <style>
    .stApp {{
        background-image: url("{image_url}");
        background-size: cover;
        background-repeat: no-repeat;
        background-attachment: fixed;
    }}
    </style>
    """
    st.markdown(css, unsafe_allow_html=True)

# Example: free medical background image
image_url = "https://media.istockphoto.com/id/1448453929/photo/cardiogram-pulse-trace-with-red-heart-on-pastel-blue-background.jpg?s=612x612&w=0&k=20&c=vROYnUeWCFJQ7uAV0Z_H1gQcwtBTygDg0aIB2YggbY0="
set_bg_image_from_url(image_url)

st.title("🩺 HEART DISEASE PREDICTION SYSTEM")
st.markdown("### 👤 Enter Your Health Information Below")



# Connect to MySQL database
#def create_connection():
# return mysql.connector.connect(
#  host="localhost",
#       user="root",
#       password="San@782005",  # Change this
#    database="heart_db"
# # )

# Create table if not exists
def initialize_database():
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS patient_history (
            id INT AUTO_INCREMENT PRIMARY KEY,
            name VARCHAR(100),
            address VARCHAR(255),
            mobile VARCHAR(20),
            age INT,
            sex INT,
            cp INT,
            trestbps INT,
            chol INT,
            fbs INT,
            restecg INT,
            thalach INT,
            exang INT,
            oldpeak FLOAT,
            slope INT,
            ca INT,
            thal INT,
            result VARCHAR(50)
        )
    """)
    conn.commit()
    conn.close()
    

    
def generate_pdf_report(data):
    pdf = FPDF()
    pdf.add_page()

    pdf.set_font("Arial", 'B', 16)
    pdf.cell(200, 10, "Heart Disease Prediction Report", ln=True, align='C')

    pdf.set_font("Arial", '', 12)
    pdf.ln(10)

    # Patient Information
    patient_fields = ['Name', 'Address', 'Mobile', 'Age', 'Sex']
    pdf.set_font("Arial", 'B', 14)
    pdf.cell(200, 10, "Patient Details:", ln=True)
    pdf.set_font("Arial", '', 12)

    for field in patient_fields:
        pdf.cell(50, 10, f"{field}:", ln=0)
        pdf.cell(100, 10, str(data.get(field, 'N/A')), ln=1)

    # Medical Info
    pdf.ln(5)
    medical_fields = ['CP', 'Trestbps', 'Chol', 'FBS', 'RestECG', 'Thalach', 'Exang', 'Oldpeak', 'Slope', 'CA', 'Thal']
    pdf.set_font("Arial", 'B', 14)
    pdf.cell(200, 10, "Medical Details:", ln=True)
    pdf.set_font("Arial", '', 12)

    for field in medical_fields:
        pdf.cell(50, 10, f"{field}:", ln=0)
        pdf.cell(100, 10, str(data.get(field, 'N/A')), ln=1)

    # Prediction Result
    pdf.ln(5)
    pdf.set_font("Arial", 'B', 14)
    pdf.cell(200, 10, "Prediction Result:", ln=True)
    pdf.set_font("Arial", '', 12)
    pdf.cell(50, 10, "Result:", ln=0)
    pdf.cell(100, 10, str(data.get('Result', 'N/A')), ln=1)

    # Convert to bytes
    pdf_output = BytesIO()
    pdf.output(pdf_output)
    pdf_output.seek(0)
    return pdf_output


def insert_patient_history(name, address, mobile, age, sex, cp, trestbps, chol, fbs, restecg,
                        thalach, exang, oldpeak, slope, ca, thal, result):
    conn = create_connection()
    cursor = conn.cursor()
    
    query = """
    INSERT INTO patient_history (name, address, mobile, age, sex, cp, trestbps, chol, fbs, restecg,
                                thalach, exang, oldpeak, slope, ca, thal, result)
    VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
    """
    
    values = (name, address, mobile, age, sex, cp, trestbps, chol, fbs, restecg,
            thalach, exang, oldpeak, slope, ca, thal, result)
    
    cursor.execute(query, values)
    conn.commit()
    conn.close()
    
# Initialize database
#initialize_database()


# Input fields
name = st.text_input("Patient Name")
address = st.text_input("Address")
mobile = st.text_input("Mobile Number")
age = st.number_input("Age", min_value=1)
sex = st.selectbox("Sex", ["Male", "Female"])
sex_val = 1 if sex == "Male" else 0
cp = st.selectbox("Chest Pain Type (0: typical angina, 1: atypical angina, 2: non-anginal pain, 3: asymptomatic)", [0, 1, 2, 3])
trestbps = st.number_input("Resting Blood Pressure", min_value=0)
chol = st.number_input("Cholesterol", min_value=0)
fbs = st.selectbox("Fasting Blood Sugar > 120 mg/dl (1 = True; 0 = False)", [0, 1])
restecg_option = st.selectbox(
    "Resting ECG Results",
    [
        "0 - Normal",
        "1 - ST-T wave abnormality",
        "2 - Left ventricular hypertrophy"
    ]
)
restecg = int(restecg_option.split(" - ")[0])

thalach = st.number_input("Max Heart Rate Achieved", min_value=0)
exang = st.selectbox("Exercise Induced Angina (1 = yes; 0 = no)", [0, 1])
oldpeak = st.number_input("ST depression induced by exercise", min_value=0.0)
slope_option = st.selectbox(
    "Slope of the Peak Exercise ST Segment",
    [
        "0 - Upsloping",
        "1 - Flat",
        "2 - Downsloping"
    ]
)
slope = int(slope_option.split(" - ")[0])
ca = st.selectbox("Number of major vessels (0-3)", [0, 1, 2, 3])
thal = st.selectbox("Thalassemia (1 = normal; 2 = fixed defect; 3 = reversible defect)", [1, 2, 3])


# Prediction
if st.button("Predict"):
    features = [[age, sex_val, cp, trestbps, chol, fbs, restecg,
                thalach, exang, oldpeak, slope, ca, thal]]
    
    result = model.predict(features)
    result_label = "Heart Disease Detected" if result[0] == 1 else "Low Risk"
    
    # Show result to user
    st.success(f"Prediction: {result_label}")
    
    
    if chol > 240:
            st.markdown("⚠️ Your cholesterol is high. Consider a low-fat diet and regular exercise.")
    if age > 60 and exang == 1:
        st.markdown("🧓 Age and angina suggest you should consult a cardiologist.")

# Insert into database
    #insert_patient_history(name, address, mobile, age, sex_val, cp, trestbps, chol, fbs, restecg,
    #                  thalach, exang, oldpeak, slope, ca, thal, result_label)


st.info("Patient result saved to database.")


# Show history
if st.button("Show Patient History"):
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM patient_history ORDER BY id DESC")
    records = cursor.fetchall()
    conn.close()


    if records:
        st.subheader("Patient History")
    df = pd.DataFrame(records, columns=[
        'ID', 'Name', 'Address', 'Mobile', 'Age', 'Sex', 'CP', 'Trestbps', 'Chol',
        'FBS', 'RestECG', 'Thalach', 'Exang', 'Oldpeak', 'Slope', 'CA', 'Thal',
        'Result', 'Timestamp'  
    ])
    st.dataframe(df)
    st.subheader("Download Patient Report")

    if not df.empty:
        selected_id = st.selectbox("Select Patient ID", df['ID'])

    selected_data = df[df['ID'] == selected_id].iloc[0].to_dict()

    pdf_file = generate_pdf_report(selected_data)

    st.download_button(
        label="📄 Download Report as PDF",
        data=pdf_file,
        file_name=f"Patient_Report_{selected_id}.pdf",
        mime='application/pdf'
    )
        
    
else:
        st.warning("No history found.")
        st.markdown("### 🗑️ Delete Patient History")


if st.button("Delete All History"):
    try:
        conn = create_connection()
        if conn:
            cursor = conn.cursor()
            cursor.execute("DELETE FROM patient_history")
            conn.commit()
            st.success(" All patient history deleted successfully!")
            conn.close()
    except Exception as e:
        st.error(f" Error deleting data: {e}")

        st.markdown("### 🗑️ Delete Specific Patient History")

delete_name = st.text_input("Enter the patient name to delete")

if st.button("Delete Patient Record"):
    if delete_name:
        try:
            conn = create_connection()
            if conn:
                cursor = conn.cursor()
                cursor.execute("DELETE FROM patient_history WHERE name = %s", (delete_name,))
                conn.commit()
                if cursor.rowcount > 0:
                    st.success(f" Patient record for '{delete_name}' deleted successfully!")
                else:
                    st.warning(f"⚠️ No record found for '{delete_name}'.")
                conn.close()
                
            

        except Exception as e:
            st.error(f" Error deleting data: {e}")
    else:
        st.warning("⚠️ Please enter a patient name.")




