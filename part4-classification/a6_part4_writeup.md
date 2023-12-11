# Part 4 - Classification Writeup

After completing `a6_part4.py` answer the following questions

## Questions to answer

# 1. Comment out the StandardScaler and re-run your test. How accurate is the model? Why is that?
The model is not very accuate because it has only a 0.68 for its accuracy score. I think this is because outliers can skew the data, leading to inaccurate results. Standardizing the model ensures that a trend can be seen in the data that is balanced. 

# 2. How accurate is the model with the StandardScaler? Is this model accurate enough for the given use case? Explain.
This model is very accurate. It has a 0.86 for its accuracy score. I feel that this model is accurate enough for its given use case because, assuming that the accuracy score's highest value is 1, this model is very close to 1 and thus highly accurate.

# 3. Looking at the predicted and actual results, how did the model do? Was there a pattern to the inputs that the model was incorrect about?
This model did relatively well regarding the predicted and actual results. Both results mostly matched; there were way less nonmatching genders than matching. A pattern to the inputs that the model was incorrect about was that some predicted perchases by men were actually bought by women.

# 4. Would a 34 year old Female who makes 56000 a year buy an SUV according to the model? Remember to scale the data before running it through the model.
According to the model, a 34-year-old female who makes 56,000 a year would buy an SUV. The value that was put in for female was 1; when I ran my prediction, I got "a 34-year-old female will [1]." Thus, I interpreted this as a "yes, she will."

