#BMI

height,weight = eval(input("enter your height(M),weight(KG):"))
BMI = weight/pow(height,2)
print("BMI = {:.2f}".format(BMI))
who,nat = "",""
if BMI < 18.5:
    who,nat = "too thin","too thin"
elif 18.5 <=BMI<24:
    who,nat = "normal","normal"
elif 24 <= BMI <25:
    who,nat = "normal","a little fat"
elif 25 <= BMI <28:
    who,nat = "a little fat","a little fat"
elif 28 <=BMI <30:
    who,nat = "a little fat","too fat"
else:
    who,nat ="too fat","too fat"
print("international{},national{}".format(who,nat))