# Part 3 - Multivariable Linear Regression Writeup

After completing `a6_part3.py` answer the following questions

## Questions to answer

1. # What is the R Squared coefficient for your model? What does that mean about the model in relation to your data?
The r squared coefficient for my model is 0.86. What this means about the model in relation to my data is that the model has been trained well on the data and is an accurate representation of it.

2. # Is your model accurate? Why or why not?
My model is accurate because there is a strong correlation in the data. The 0.86 squared coefficient is close to the perfect correlation coefficient of 1, showing that the data has a strong correlation.  

3. # What does the model predict a 10-year-old car with 89000 miles is worth? What about a car that is 20 years old with 150000 miles?
A 10-year-old car with 89,000 miles is worth $9,318.90. A car that is 20 years old with 150,000 miles is worth $2,062.17.

4. # You may notice that some of your predicted results are negative. This is occurring when the value of age and the mileage of the car are very high. Why do you think this is happening?
I think that this is happening because the older the car and the more miles it has, the more it depreciates in value. In real life, the value of the car would not depreciate below $0, however, there is no safeguard against that in this program. That in turn leads to the negative values. 