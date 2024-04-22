import streamlit as st
from PIL import Image

img = Image.open("bpimage.jpg")
img

st.title("BLOOD PRESSURE CALCULATOR")
st.subheader("Check Blood pressure Status")
st.write("Blood pressure is measured using two numbers:\n The first number, called systolic blood pressure, measures the pressure in your arteries when your heart beats.\n The second number called diastolic blood pressure, measures the pressure in your arteries when your heart rests between beats")
def check_blood_pressure(systolic, diastolic):
    if systolic <= 90 and diastolic < 60:
        return "Hypotension"
    if systolic < 120 and diastolic < 80:
        return "Normal"
    elif 120 < systolic <= 129 and diastolic < 80:
        return "Elevated"
    elif 130 < systolic <= 139 or 80 < diastolic <= 89:
        return "Stage 1 Hypertension"
    elif systolic >= 140 or diastolic >=90:
        return "Stage 2 Hypertention"
    elif systolic >= 180 or diastolic >= 120:
        return "Hypertension Crisis!!!"
    
    systolic_bp = st.input("what is your systolic blood pressure in mmHg", step=1) 
    diastolic_bp = st.input ("what is your diastolic blood pressure in mmHg")


def main():
    st.title("Blood Pressure Calculator")

    st.write("Enter your systolic and diastolic blood pressure values below:")

    systolic_bp = st.number_input("What is your systolic blood pressure in mmHg?", step=1)
    diastolic_bp = st.number_input("What is your diastolic blood pressure in mmHg?", step=1)

    if st.button("Calculate"):
        blood_pressure = check_blood_pressure(systolic_bp, diastolic_bp)
        st.write(f"Your blood pressure status is: {blood_pressure}")



if __name__ == "__main__":
    main()



