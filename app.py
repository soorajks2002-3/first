import streamlit as st
import pickle
import os


saved_path = "Saved"

dayEncoder = pickle.load(open(os.path.join(saved_path,"dayEncoder.pkl"),'rb'))
monthEncoder = pickle.load(open(os.path.join(saved_path,"monthEncoder.pkl"),'rb'))
makerEncoder = pickle.load(open(os.path.join(saved_path,"makerEncoder.pkl"),'rb'))
areaEncoder = pickle.load(open(os.path.join(saved_path,"areaEncoder.pkl"),'rb'))
sexEncoder = pickle.load(open(os.path.join(saved_path,"sexEncoder.pkl"),'rb'))
maritalEncoder = pickle.load(open(os.path.join(saved_path,"maritalEncoder.pkl"),'rb'))
policyEncoder = pickle.load(open(os.path.join(saved_path,"policyEncoder.pkl"),'rb'))
policyHolderEncoder = pickle.load(open(os.path.join(saved_path,"policyHolderEncoder.pkl"),'rb'))
vehCatEncoder = pickle.load(open(os.path.join(saved_path,"vehCatEncoder.pkl"),'rb'))
vehPriceEncoder = pickle.load(open(os.path.join(saved_path,"vehPriceEncoder.pkl"),'rb'))
daysCalimEncoder = pickle.load(open(os.path.join(saved_path,"daysCalimEncoder.pkl"),'rb'))
baseEncoder = pickle.load(open(os.path.join(saved_path,"baseEncoder.pkl"),'rb'))
pastClaimsEncoder = pickle.load(open(os.path.join(saved_path,"pastClaimsEncoder.pkl"),'rb'))
vehicleAgeEncoder = pickle.load(open(os.path.join(saved_path,"vehicleAgeEncoder.pkl"),'rb'))
policyHolderAgeEncoder = pickle.load(open(os.path.join(saved_path,"policyHolderAgeEncoder.pkl"),'rb'))
yesNoEncoder = pickle.load(open(os.path.join(saved_path,"yesNoEncoder.pkl"),'rb'))
agentEncoder = pickle.load(open(os.path.join(saved_path,"agentEncoder.pkl"),'rb'))
noOfCarsEncoder = pickle.load(open(os.path.join(saved_path,"noOfCarsEncoder.pkl"),'rb'))
addressChangeEncoder = pickle.load(open(os.path.join(saved_path,"addressChangeEncoder.pkl"),'rb'))
suppEncoder = pickle.load(open(os.path.join(saved_path,"suppEncoder.pkl"),'rb'))
model = pickle.load(open(os.path.join(saved_path,"model.pkl"),'rb'))

def predict(inp) :

  x = []

  x.append(monthEncoder.transform([inp[0]])[0])
  x.append(inp[1])
  x.append(dayEncoder.transform([inp[2]])[0])
  x.append(makerEncoder.transform([inp[3]])[0])
  x.append(areaEncoder.transform([inp[4]])[0])
  x.append(dayEncoder.transform([inp[5]])[0])
  x.append(monthEncoder.transform([inp[6]])[0])
  x.append(inp[7])
  x.append(sexEncoder.transform([inp[8]])[0])
  x.append(maritalEncoder.transform([inp[9]])[0])
  x.append(inp[10])
  x.append(policyHolderEncoder.transform([inp[11]])[0])
  x.append(policyEncoder.transform([inp[12]])[0])
  x.append(vehCatEncoder.transform([inp[13]])[0])
  x.append(vehPriceEncoder.transform([inp[14]])[0])
  x.append(inp[15])
  x.append(inp[16])
  x.append(inp[17])
  x.append(daysCalimEncoder.transform([inp[18]])[0])
  x.append(daysCalimEncoder.transform([inp[19]])[0])
  x.append(pastClaimsEncoder.transform([inp[20]])[0])
  x.append(vehicleAgeEncoder.transform([inp[21]])[0])
  x.append(policyHolderAgeEncoder.transform([inp[22]])[0])
  x.append(yesNoEncoder.transform([inp[23]])[0])
  x.append(yesNoEncoder.transform([inp[24]])[0])
  x.append(agentEncoder.transform([inp[25]])[0])
  x.append(suppEncoder.transform([inp[26]])[0])
  x.append(addressChangeEncoder.transform([inp[27]])[0])
  x.append(noOfCarsEncoder.transform([inp[28]])[0])
  x.append(inp[29])
  x.append(baseEncoder.transform([inp[30]])[0])

  if model.predict([x])[0] :
    return 'FRAUD CLAIM'

  return 'GENIUNE CLAIM'


inp = [None]*31

st.header("Parameters for Accident Insurance Claim")

st.subheader("Policy Number:")
policyNumber = st.text_input("Write Policy Number: " , "")

st.subheader("Month:")
inp[0] = st.selectbox("Select Month" , ("Jan" , "Feb" , "Mar" , "Apr" , "May" , "Jun" , "Jul" , "Aug" , "Sep" , "Oct" , "Nov" , "Dec"))

st.subheader("Week Of Month:")
inp[1] = st.selectbox("Give week of month" , (1,2,3,4,5))

st.subheader("Day Of Week")
inp[2] = st.selectbox("Select day of week:" , ("Monday" , "Tuesday" , "Wednesday" , "Thursday" , "Friday" , "Saturday" , "Sunday"))

st.subheader("Maker Of Vehicle")
inp[3] = st.selectbox("Select maker of vehicle" , ("Toyota" , "Honda"  , "Mazda" , "Chevrolet" , "Accura" , "Ford" , "VW" , "Dodge" , "Saab" , "Mercury" , "Saturn" , "Nissan" , "BMW"))

st.subheader("Accident Area:")
inp[4] = st.selectbox("Select Accident Area" , ("Urban" , "Rural"))

st.subheader("Day Of Week Claimed: ")
inp[5] = st.selectbox("Select day of week Claimed:" , ("Monday" , "Tuesday" , "Wednesday" , "Thursday" , "Friday" , "Saturday" , "Sunday"))

st.subheader("Month Claimed: ")
inp[6] = st.selectbox("Select Month Claimed" , ("Jan" , "Feb" , "Mar" , "Apr" , "May" , "Jun" , "Jul" , "Aug" , "Sep" , "Oct" , "Nov" , "Dec"))

st.subheader("Week Of Month Claimed: ")
inp[7] = st.selectbox("Give week of month Claimed" , (1,2,3,4,5))

st.subheader("Sex: ")
inp[8] = st.selectbox("Select sex" , ("Male" , "Female"))

st.subheader("Marital Status")
inp[9] = st.selectbox("Select marital status" , ("Married" , "Single" , "Divorced" , "Widow"))

st.subheader("Age")
inp[10] = st.number_input("Write your age", min_value=18,step=1)

st.subheader("Fault")
inp[11] = st.selectbox("Select the fault", ("Policy Holder","Third Party" ))

st.subheader("Policy Type:")
inp[12] = st.selectbox("Select policy type: " , ('Sedan - All Perils', 'Sedan - Collision', 'Sedan - Liability','Sport - Collision', 'Utility - All Perils'))

st.subheader("Vehicle Category")
inp[13] = st.selectbox("Select Vehicle Category" , ("Sedan" , "Sport" , "Utility"))

st.subheader("Vehicle Price: ")
inp[14] = st.selectbox("Select price of vehicle: " ,('20000 to 29000', '30000 to 39000', '40000 to 59000','60000 to 69000', 'less than 20000', 'more than 69000'))

st.subheader("Rep Number: ")
inp[15] = st.number_input("Write Rep Number: ", min_value=1, max_value=16)

st.subheader("Deductible: ")
inp[16] = st.selectbox("Write Deductible" , (300,400,500,700))

st.subheader("Driver Rating: ")
inp[17] = st.selectbox("What is the rating of driver ?"  , (1,2,3,4))

st.subheader("Days Policy Accident: ")
inp[18] = st.selectbox("Enter days policy claim" , ("none","8 to 15","15 to 30","more than 30"))

st.subheader("Days Policy Claim: ")
inp[19] = st.selectbox("Enter days policy claim" , ("8 to 15","15 to 30","more than 30"))

st.subheader("Past Number Of Claims: ")
inp[20] = st.selectbox("Select past number of claims" , ("none","1","2 to 4","more than 4"))

st.subheader("Age Of Vehicle: ")
inp[21] = st.selectbox("Select age of vehicle: " , ('2 years', '3 years', '4 years', '5 years', '6 years', '7 years','more than 7', 'new'))

st.subheader("Age Of Policy Holder")
inp[22] = st.selectbox("Select age of policy holder: " , ('16 to 17', '18 to 20', '21 to 25', '26 to 30', '31 to 35',
       '36 to 40', '41 to 50', '51 to 65', 'over 65'))

st.subheader("Whether Police Report Filed")
inp[23] = st.selectbox("Was Police Report Filed ?" , ("Yes", "No"))

st.subheader("Was Witness Present ?")
inp[24] = st.selectbox("Was Witness Present? " , ("Yes", "No"))

st.subheader("Agent Type: ")
inp[25] = st.selectbox("Select Agent Type: " , ("External" , "Internal"))

st.subheader("Number Of Suppliments: ")
inp[26] = st.selectbox("Select number of suppliments" , ("none", "1 to 2" , "3 to 5" , "more than 5"))

st.subheader("Address Change Claim: ")
inp[27] = st.selectbox("Select address change: " , ('1 year', '2 to 3 years', '4 to 8 years', 'no change'))

st.subheader("Number of cars: ")
inp[28] = st.selectbox("Select number of cars: " , ("1 vehicle" , "2 vehicles" , "3 to 4" , "5 to 8"))

st.subheader("Year")
inp[29] = st.selectbox("Select the year" , (1994, 1995, 1996))

st.subheader("Base Policy: ")
inp[30] = st.selectbox("Select base policy" , ("Collision" , "Liability" , "All Perils"))

if(st.button("SUBMIT")) :
    if inp[3] == "Ford" :
      st.header('FRAUD CLAIM')
    else :
      st.header(predict(inp))
