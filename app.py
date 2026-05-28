import streamlit as st
import pandas as pd
import re
from datetime import date
from database import conn, cursor
from ml_model import predict_health

# App Title
st.title("Health Prediction Application")

# Sidebar Menu
menu = ["Add Patient", "View Patients", "Update Patient", "Delete Patient"]

choice = st.sidebar.selectbox("Menu", menu)

# =========================
# ADD PATIENT
# =========================

if choice == "Add Patient":

    st.subheader("Add Patient")

    # Input Fields
    name = st.text_input("Full Name")

    dob = st.date_input(
        "Date of Birth",
        min_value=date(1950, 1, 1),
        max_value=date.today()
    )

    email = st.text_input("Email Address")

    glucose = st.number_input(
        "Glucose",
        min_value=0.0,
        format="%.2f"
    )

    haemoglobin = st.number_input(
        "Haemoglobin",
        min_value=0.0,
        format="%.2f"
    )

    cholesterol = st.number_input(
        "Cholesterol",
        min_value=0.0,
        format="%.2f"
    )

    # Email Validation Function
    def valid_email(email):
        pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
        return re.match(pattern, email)

    # Save Button
    if st.button("Save Patient"):

        # Validation
        if name == "":
            st.error("Please enter Full Name")

        elif not valid_email(email):
            st.error("Invalid Email Address")

        elif dob > date.today():
            st.error("DOB cannot be future date")

        else:

            try:

                # AI Prediction
                remarks = predict_health(
                    glucose,
                    haemoglobin,
                    cholesterol
                )

                # Save into Database
                cursor.execute("""
                INSERT INTO patients
                (name, dob, email, glucose, haemoglobin, cholesterol, remarks)
                VALUES (?, ?, ?, ?, ?, ?, ?)
                """, (
                    name,
                    str(dob),
                    email,
                    glucose,
                    haemoglobin,
                    cholesterol,
                    remarks
                ))

                conn.commit()

                st.success("Patient Added Successfully")

                st.info(f"AI Prediction: {remarks}")

            except Exception as e:
                st.error(f"Error: {e}")

# =========================
# VIEW PATIENTS
# =========================

elif choice == "View Patients":

    st.subheader("Patient Records")

    cursor.execute("SELECT * FROM patients")

    rows = cursor.fetchall()

    if rows:

        df = pd.DataFrame(rows, columns=[
            "ID",
            "Name",
            "DOB",
            "Email",
            "Glucose",
            "Haemoglobin",
            "Cholesterol",
            "Remarks"
        ])

        st.dataframe(df)

    else:
        st.warning("No patient records found")

# =========================
# UPDATE PATIENT
# =========================

elif choice == "Update Patient":

    st.subheader("Update Patient")

    patient_id = st.number_input(
        "Enter Patient ID",
        min_value=1,
        step=1
    )

    new_name = st.text_input("New Name")

    if st.button("Update"):

        cursor.execute("""
        UPDATE patients
        SET name=?
        WHERE id=?
        """, (
            new_name,
            patient_id
        ))

        conn.commit()

        st.success("Patient Updated Successfully")

# =========================
# DELETE PATIENT
# =========================

elif choice == "Delete Patient":

    st.subheader("Delete Patient")

    patient_id = st.number_input(
        "Enter Patient ID to Delete",
        min_value=1,
        step=1
    )

    if st.button("Delete"):

        cursor.execute(
            "DELETE FROM patients WHERE id=?",
            (patient_id,)
        )

        conn.commit()

        st.success("Patient Deleted Successfully")