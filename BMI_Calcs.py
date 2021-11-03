import json

def BMI_Calculator():
    # Load Json Data
    with open('./BMI.json', 'r') as c:
        params = json.load(c)   
    # I just considered the low value as 0 and for max evaluation as 50 but it will not affect the result
    BMI_Range={0:[0,18.5],1:[18.5,24.9],2:[25,29.9],3:[30,34.9],4:[35,39.9],5:[40,50]}
    Health_Risk=["Malnutrition risk","Low risk","Enhanced risk","Medium risk","High risk","Very high risk"]
    BMI_Category=["Underweight","Normal weight","Overweight","Moderately obese","Severely obese","Very severely obese"]
    # Final Result will store all the BMI based on given data and will store in Dictionary with key 1,2,3,...
    Final_Result={}
    i=1
    for Item in params:
        BMI=round(Item["WeightKg"]/(Item["HeightCm"]/100)**2,2)
        for key in BMI_Range:
            if key==5:
                Final_Result[i]=[BMI,Health_Risk[key],BMI_Category[key]]
                break
            if BMI >= BMI_Range[key][0] and BMI < BMI_Range[key+1][0]:
                Final_Result[i]=[BMI,Health_Risk[key],BMI_Category[key]]
                break
        i+=1

    return Final_Result

if __name__=='__main__':
    Final_Result=BMI_Calculator()
    total_overweighted_person=0
    for key in Final_Result:
        if "Overweight" in Final_Result[key]:
            total_overweighted_person+=1
    print(Final_Result)
    print(f"Total Number of Overweighted person {total_overweighted_person}")
