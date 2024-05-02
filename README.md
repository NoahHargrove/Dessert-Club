# Dessert Club Results Write-Up / Read Me

**Noah Hargrove**  
**COMP 401**

Over the past semester, I worked on a project called the “Dessert Club”. The main 
objective was to create a dessert guesser using machine learning, similar to the 
Akinator, aimed at bringing people together over the simple joy of desserts. The 
project comprised three main parts: creating a web application using Google App 
Script to collect user-submitted data into a Google spreadsheet, researching and 
integrating machine learning algorithms using the collected data, and 
implementing a selected machine learning algorithm into a dessert guesser using 
Flask to create an interactive web application.

To train a machine learning algorithm, I needed data. The initial step was 
creating a web application that allowed users to upload data about desserts. Two 
web applications were created. The first, a broader survey using scale data like 
"How heavy is the dessert on a scale from 1-5", included a lot of noise from 
varying opinions on desserts and their characteristics. Additionally, users chose 
the desserts they submitted responses for, leading to some categories of desserts 
having few samples while others had many, resulting in imbalanced category sizes. 
Initially, I aimed for about 1,000 observations but only gathered about 130. This 
shortfall highlighted three issues: noisy data, unbalanced data, and an 
insufficient quantity of data.

To address these issues, I initially considered adding synthetic noise to increase 
the sample size and using SMOTE to oversample categories with few samples. However, 
given the potential poor quality of the data, I devised an alternative solution. I 
created a new survey with all yes/no questions to make choices more binary. I 
surveyed every dessert myself and had two friends do the same, ensuring an equal 
number of observations for each category with substantially less noise. I then 
added synthetic noise to expand the 200 observations to 10,000 to train my model.

With a robust dataset, I conducted basic research on machine learning. This 
research helped me understand the flaws in my original data and what needed 
correcting for the algorithms to function effectively. My research primarily 
focused on understanding basic classical machine learning algorithms like decision 
trees, random forests, SVM, and k-NN. I gained insights into each algorithm's 
benefits and suitable data types, and their basic implementations, including how 
to test their confidence with a given dataset. I concluded that random forest was 
the best fit for my data due to its high confidence and robustness with noisy data.

Once my machine learning algorithm was selected, I implemented it in a basic 
dessert guesser using Repl.it. I experimented with both static and iterative 
implementations, where the static version asked all questions before outputting a 
response, while the iterative version made guesses once a confidence threshold was 
reached. I created an interactive implementation of a dessert guesser that used a 
random forest algorithm in Repl.it. Then I shifted my focus to learning Flask, 
which was challenging, but I managed to transfer my understanding of implementing a 
dessert guesser into Flask. I created three HTMLs that welcomed the user, 
collected input from yes/no buttons for different questions, and output a dessert 
guess at the end. The app code called these HTMLs and contained the main 
implementation of the dessert guesser.

Overall, I was quite successful in achieving my goals: creating a dessert guesser 
that used a web application to gather data, code to increase the sample size by 
adding noise, and learning and implementing machine learning algorithms. There 
were potential areas for improvement, such as iterative imputation with question 
logic in the Flask implementation and enhancing the user-friendly aspect of 
updating the original web application used for surveying. However, these tasks 
were time-consuming, considering I was learning HTML, machine learning, and Flask 
all in one semester. With more time, these are areas I would like to improve, 
along with optimizing the machine learning algorithm and gathering more data.

From the above, you can see the multitude of different components that were part of 
my project. I will guide you through each one and how to access or use the code. 
For any Google-related code, I will add you as a collaborator so you can access the 
code. I will also include a text file with instructions for how to run the code. 
For the Repl.it sections of the code, I will do the same, including the original 
data I used and the data with synthetic noise. Finally, for the Flask code, I will 
include all of my code in a text file along with instructions on how to run them.

## Accessing the Code and Running It

### Web Application
Shared with you as "Final Dessert Survey" for the survey of all yes or no questions that was 
used in my later sections of code to train the random forest algorithm. Here is the 
corresponding Google Sheets shared link: 
[Final Dessert Survey Sheet](https://docs.google.com/spreadsheets/d/1oiK80folbw_Q3K43kFP9V1CuvQl8sHZ5SHk1AR7PUwA/edit?usp=sharing).

The first survey, which was not used for training the algorithm, is shared with you as 
"First Dessert Survey" and its corresponding Google Sheet link is: 
[First Dessert Survey Sheet](https://docs.google.com/spreadsheets/d/1oiK80folbw_Q3K43kFP9V1CuvQl8sHZ5SHk1AR7PUwA/edit?usp=sharing).

There is a folder called “Dessert Survey Web Application & Data.” Files are separated by either 
the first or final dessert survey. To run the code, open Google Apps Script and create a new 
project. Then create a file named `Code.gs` and copy-paste the code from the `code_gs` text 
file. Also, create another file called `WebApp.html` and copy-paste the respective code there. 
Then hit deploy and test deploy. You should be able to see the code, and if adding a response, 
see it in the shared Google Sheets. Alternatively, you can create your own Google Sheet and 
put the share link in its respective place in the `Code.gs` file.

### Data Manipulation
Done through Replit, so I will include the Replit link here. In the Replit, there should be a 
CSV file with correct data and an output noise data file that you can clear and rerun the code 
to see it work. I will also include a new folder called “Data Manipulation.” This folder will 
contain the CSV from the final dessert survey, a text file for the code that can be copy-pasted 
into your own Replit, and finally the output file. To run the code, either click on the Replit 
link or copy the code from the text file into a new Replit Python project. Add the `dessert.csv` 
file, create a `desserts_noise.csv` file, and run the code.
Replit link: [Data Manipulation Replit](https://replit.com/join/lknckpuoxh-noahhargrove)

### Machine Learning
All done in Replit. I will include the link as well as a text file for each piece of code and 
the needed CSV file to run it. Again, for both pieces of code, create a Replit, copy the text 
file, and add the `dessert.csv` to the file section (note: `dessert.csv` in this section is 
really the `desserts_noise.csv`). You can also access it through my share link and run both 
pieces of code.

The first file will be called “Machine Learning Selection,” which implements various machine 
learning algorithms and outputs their confidence level for the data.
Replit link: [Machine Learning Selection Replit](https://replit.com/join/sbvbqjbpza-noahhargrove)

The second file will be called “Iterative Implementation of Dessert Guesser” that includes the 
iterative implementation of a dessert guesser in Replit. To run, just add the `dessert.csv` 
file and hit the run button, then answer questions in the UI section. Note because this is 
not the final code, the UI is very primitive and answers must be entered correctly as 0 for 
no and 1 for yes.
Replit Link: [Iterative Implementation Replit](https://replit.com/join/jyhsclxqex-noahhargrove)

### Dessert Guesser Implementation in Flask
I will include the four needed files for this code to run. The first will be
called `app.py`, which uses the random forest algorithm and runs the actual app,
calling the three needed HTMLs. The next three files are the HTMLs. One is called
`welcome.html`, where the user is welcomed when using the dessert guesser. The
next is called `question.html`, where the user is given question prompts in yes/no
button formats that collect user data. Finally, the `result.html` takes the UI from
questions and outputs a dessert guess, asking the user if they want to play again.

To run the code, there will be a folder called "Flask_App." All code will be included
in the folder. Download it to your desktop and then it can be run by accessing your
terminal or command prompt. Use cd to navigate to the folder's location. Then run a
Python environment, run `app.py`, and finally copy and paste the HTTP link it gives
into a web browser, and you are good to go. For me, that means I open the command
prompt and enter:

cd C:\Users\Test\Desktop\Flask_App

env\Scripts\activate

python app.py

Then copy `http://127.0.0.1:5000` and paste it into a web browser.

## Project Results and Conclusion

The project results are challenging to format in a text document, as they encompass
the components described above. The main deliverable is a working dessert guesser
that can accurately predict desserts within the bounds of "human error." While it
identifies some desserts, minor discrepancies in how someone might describe a bar
or brownie can cause slight inaccuracies in the dessert guesser's predictions.
Overall, the project was successful, with two operational web application surveys,
code to add synthetic noise and increase the sample size, and code to test various
machine learning algorithms and implement them iteratively. Additionally, the project
culminated in a fully functional dessert guesser web application using Flask. Beyond
these results, the project also enhanced my knowledge and practical skills in working
with HTML, Flask, and machine learning algorithms.

#### Detailed Overview of the Final Product

The final product is a dessert guesser with a few main components. The first is the
main app that runs code to train the random forest algorithm. The main app then runs
the application, calling three HTML files in addition to the code for the application
to function. My dessert guesser welcomes a user to a welcome page asking if they want
to play the game. Upon hitting the play button, a series of approximately 40 questions
are asked that help the random forest algorithm correctly classify the dessert being
described. Each question is presented to the user with two buttons: one for "yes,"
and one for "no." When the user clicks one button, the next question is prompted,
and so on. Once all questions have been answered, the application makes a guess about
the dessert the user is thinking of and has been answering questions about. The results
are then displayed on the results page of the web application, where the guess is output,
and a prompt button to play again is shown. If the user clicks "play again," it brings
them back to the welcome page where they can play again. This can be done as many times
as the user wishes. These three HTML pages, along with the application, including training
a random forest algorithm to help come up with a guess, are the main results of my project.

#### Additional Concluding Remarks

As stated above, there are some smaller results which are the two other web applications
for gathering data, the code in Repl.it used to create noise, test different algorithms,
and implement one. One of the conclusions I can draw is the importance of understanding
the end goal. More research should have been done upfront to understand the necessary steps
to achieve my end product. For example, a better understanding of machine learning algorithms
and the data needed to train them would have been crucial in designing an effective survey.
Additionally, understanding more about HTML and Flask could have been helpful in developing
an approach to include question logic and iterative guesses. Overall, understanding that
learning new topics slows the development process drastically, turning small problems into
big ones is an important takeaway. Similarly, sticking to a path instead of allowing new
objectives to divert my attention is also key.


Note the use of AI to help with editing, errors in code, and images generated in presentations.


