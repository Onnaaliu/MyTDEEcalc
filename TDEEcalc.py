import streamlit as st

from PIL import Image

from PIL import Image
img = Image.open("Getfit.png")
st.image(img, width=500)



st.title('BMR AND TDEE CALCULATOR')
st.subheader('Welcome to your best weight management advisory plug!')

st.markdown('Basal Metabolic Rate (BMR) is how many calories you burn when your body is resting')
st.markdown('Total Daily Energy Expenditure (TDEE) is an estimation of how many calories you burn each day, including physical activity.')

st.markdown('This should be used with a food log to achieve weight loss or weight gain. A TDEE calculator helps you determine how much calories you need daily to shed excess weight and live healthily. For weight loss, aim for calorie deficit while you should aim for a calorie surplus to gain weight')

st.warning('A pound(0.45kg) is about 500 calories')

weight = st.number_input("Enter your weight (in kg)")
height = st.number_input("Enter your height (in cm)")
age = st.number_input("Enter your age (in years)")
Gender = st.radio('Gender: ',('Male', 'Female'))

def BMR_calculator(weight, height, age, gender):
    BMR = 0
if Gender == 'Male':
    BMR = ((10*weight) + float(6.25*height)-(5*age)+5);
elif Gender == 'Female': 
    BMR = (int((10*weight) + float(6.25*height)-(5*age))-int(161))
else:
    st.text("Enter correct details")
    quit()
BMR = round(BMR)

if(st.button('Calculate BMR')):
    st.text("Your BMR is {}.".format(BMR))
    
if(st.button('Click here to continue')):
    st.markdown("Please choose Activity level")
    st.markdown("Activity level A - Sedentary (little or no exercise):\n")
    st.markdown("Activity level B - Lightly active (light exercise 1-3 days a week):\n")
    st.markdown("Activity level C - Moderately active (moderate exercise 1-3 days a week):\n")
    st.markdown("Activity level D - Very active (Heavy exercise 6-7 days a week):\n")
    st.markdown("Activity level E - Extremely active (Vert heavy exercise, hard labour job or training 2x a day)") 
    
Activitylevel = st.selectbox('Activity Level: ', ('Choose Activity Level','A', 'B', 'C', 'D', 'E'))

def multiply(BMR, multiplier):
    return (BMR*multiplier)

BMR = float(BMR)

if Activitylevel == 'Choose Activity Level':
    st.error("Choose Activity Level")
    
elif Activitylevel == 'A':
    multiplier = float(1.2)
    st.warning("A sedentary lifestyle is bad for your heart health. Try to move more!")
elif Activitylevel == 'B':
    multiplier = float(1.375)
    st.markdown("You can improve your Activity level by adding some cardio and Strenght training to your routine; then aim to cut 500cal daily to achieve a weight loss of one pound a week")
elif Activitylevel == 'C':
    multiplier = float(1.55)
    st.markdown("If weight loss is your goal; increase your TDEE with strenght and resistant training; then aim to cut 500cal daily to achieve a weight loss of one pound a week")
elif Activitylevel == 'D':
    multiplier = float(1.725)
    st.markdown("You are pretty fit! if you want to lose weight, aim to cut 500cal daily to achieve a weight loss of one pound a week")
elif Activitylevel == 'E':
    multiplier = float(1.9)
    st.markdown("You extremely fit! Ensure you consume enough calories in accordance with your TDEE so as no to risk muscle loss.")
else:
    quit()
    st.warning("Enter valid Activity Level")
    
if(st.button('Calculate TDEE')):
    st.text("Your TDEE is: \n")
    st.text(round(multiply(BMR, multiplier)))

st.code('Calculations were made using Mifflin-St Jeor Formular')
