#require weight and height and recommend a diet and exercises to improve health.


class BMI:
    def __init__(self, weight, height) :
        if not weight or not height:
            raise ValueError("Missing Input")
        self.weight = weight
        self.height = height
    
    
    def bmi(weight, height):
        try:
            return (f"{float(weight)/(float(height)**2):.2f}")
        except ValueError:
            return ("Make sure your input is a number only and try again.")
    
    
    def interprate(weight, height):
        bmi = float(BMI.bmi(weight, height))
        if  bmi < 18.5:
             return "You are underweight"
        elif 18.5 < bmi < 24.99:
                return "You're of healthy weight"
        elif 25 < bmi < 29.99:           
            return "You're overweight"
        elif 30 < bmi < 34.99:            
            return "You're obese"
        elif 35 < bmi < 39.99:
            return "You're severely obese"
        elif bmi >= 40:           
            return "You're morbidly obese"
        
    
class Exercise:
    def __init__(self, exercise):
        while True:
            if exercise.lower() in ["abs", "glutes", "shoulder and back", "arms", "legs"]:
                break
            else:
                print("Please choose on of the options available.")
                exercise = input ("Enter part of body you plan on working on(abs, shoulder and back, glutes, quads, legs, arms): ")
                
            
        self.exercise = exercise  
       
    def __str__(self):
        return self.exercise
        
    def match(exercise):
        if exercise.lower() == "none":           
            return "Stay healthy"
        else:
            exercise = str(Exercise(exercise))
            if exercise.lower() == "abs":
                return f"""Abs:
                            Jumping jacks(30 secs,3 sets)
                            Abdominal crunches(×16)
                            Plank(20secs,2 sets)
                            Leg raises (×16)
                            
    NB: Increase workout intensity with time and gradually
    Drink enough water, get enough sleep and more importantly, take 2 restdays every week to rejuvenate your muscles."""
            elif exercise.lower() == "glutes":
                return f"""Glutes:
                            Hip thrusts(×15 per set,3 sets)
                            Knee push ups(×12)
                            Plank(15 secs,2 sets)
                            Squats(×20 per set,2 sets)
                            
    NB: Increase workout intensity with time and gradually
    Drink enough water, get enough sleep and more importantly, take 2 restdays every week to rejuvenate your muscles."""
            elif exercise.lower() == "shoulder and back":
                return f"""Shoulder and back:
                            Arm raises(×30)
                            Side arm raises(×15 per set,2 sets)
                            Knee push ups(×14)
                            Side lying floor stretch(Left and right(30 secs each side)
                            
    NB: Increase workout intensity with time and gradually
    Drink enough water, get enough sleep and more importantly, take 2 restdays every week to rejuvenate your muscles."""
            elif exercise.lower() == "legs":
                return f"""Leg workout:
                            Squats(×12 per set,two sets)
                            Side lying leg lift(left and right)(×12 for each side)
                            Donkey kick(left and right)(×16 for each side)
                            
    NB: Increase workout intensity with time and gradually
    Drink enough water, get enough sleep and more importantly, take 2 restdays every week to rejuvenate your muscles."""
            elif exercise.lower() == "arms":
                return f"""Arm workout:
                            Arm raise(×15 per set,2 sets)
                            Side arm raise(×15)
                            Tricep dip(×15)
                            Barbell raise left arm(×16)
                            Barbell raise right arm(×16)
                            
    NB: Increase workout intensity with time and gradually
    Drink enough water, get enough sleep and more importantly, take 2 restdays every week to rejuvenate your muscles."""  
                        

def main():
    #intro
    print("Fitness Checker")
    
    #BMI
    weight = input("Enter weight (in kg): ")
    height = input("Enter height (in m): ")
    output = BMI.bmi(weight, height)
    meaning = BMI.interprate(weight, height)
    print(f"BMI: {output}")
    print(f"Interpration: {meaning}")
    
    #Exercise
    
    exercise = input(f"Enter part of body you plan on working on(abs, shoulder and back, glutes, quads, legs, arms): ")
    print(Exercise.match(exercise))
    
if __name__ == "__main__":
    main()