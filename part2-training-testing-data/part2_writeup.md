# Part 2 - Training and Testing Data Writeup

After completing `a6_part2.py` answer the following questions

## Questions to answer

1. # What makes this model more effective than the model you created in the previous lesson?
What makes this model more effective than the model I created in the previous lesson is the addition of training and testing datasets that allows for more accurate predictions. 

2. # What does the R squared coefficient tell you about the model?
What the r squared coefficient tells me about the model is that there is a relatively strong correlation between age and blood pressure. The r squared value/Pearson correlation coefficient is 0.73 and close to the perect Pearson correlation of 1. 

3. # Would you say that your model is accurate? What evidence supports your conclusion? Consider the meaning of the predicted and actual values in the context of the chart below from the American Heart Association’s website on understanding blood pressure.
I would say that my model is accurate because, as listed about, my Pearson correlation coefficient was relatively close to the perfect correlation of 1. Evidence that supports my conclusion are the prediction points being exactly on the line of best fit. The meaning of the predicted and actual values in the context of the American Heart Association's website are that when the age increases (the x value), the blood pressure (the y value) increases from a normal blood pressure, to an elevated blood pressure, to hypertension stage one, and finally to hypertension stage 2. The predicted y value is less than the actual y value as a result of outliers. 