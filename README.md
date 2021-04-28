# PHSX815_Week12: University admissions data and Central Limit Theorem

1. University admissions: Run the code 'university_admissions.py' on the command line using the command 'python3.8 /path/university_admissions.py'. The user will see a scatter plot between the two chosen variables. The question chosen to answer for the homework is mentioned in the report. Unfortunately, I could not successfully run a correlation test because of the presence of NaN elements in the arrays.

2. Central Limit Theorem: One of the simplest ways of visualizing the Central Limit Theorem is by performing multiple die rolls and observing how the shape of the distribution resembles the bell shape, with increased number of simulations. Before running the code, the user should enter the path where they intend to save the gif file that will be generated on line 44 of the file. Once that's done, run it using the command 'python3.8 /path/CLT.py'. The user can then see the saved animated gif to see how the distribution for die rolls starts resembling normal distribution with increasing trials, thus visually respresenting the Central Limit Theorem. The other example (CLT_2.py) in the repository is a simple plotting of means of randomly generated numbers with increasing sample sizes. Run the code using 'python 3.8 /path/CLT_2.py', and the user will see 4 distributions for 4 sample sizes. One can play around with sample sizes by altering N and seeing how the distribution varies by varying N.

Answering the questionsposed on Blackboard:
Q: What does this distribution of averages look like as you increase N?
Ans: It begins resembling the Gaussian distribution as N increases.


References:

1. medium.com/analytics-vidhya
2. blog.quantinsti.com
3. towardsdatascience.com/central-limit-theorem-explained-with-python-code-230884d40ce0
4. www.freecodecamp.org
