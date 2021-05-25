def BMI_Calculate(height,weight):
    w = float(weight)
    h = float(height)
    bmi = w / ( h * h )
    print('\nBMI =', bmi)

    if bmi<=16.5:
        interpretation = 'undernutrition or anorexia'
    elif bmi<=18.5:
         interpretation = 'Underweight'
    elif bmi<=25:
         interpretation = 'Normal (healthy weight)'
    elif bmi<=30:
        interpretation = 'Overweight—at risk'
    elif bmi<=35:
        interpretation = 'Overweight—moderately obese'
    elif bmi<=40:
        interpretation = 'Overweight—severely obese'
    else:
        interpretation = 'Overweight—very severely obese'

    print('You are classified under the ',interpretation, 'category')