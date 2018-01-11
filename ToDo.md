# ToDo List

1. Figure out which (open source) Bazyes code is out there that we might want to use.  You can learn about Naive Bayes [here](https://en.wikipedia.org/wiki/Naive_Bayes_classifier).  There is quite a lot more on the web.  You can get some Python-specific examples [here](https://machinelearningmastery.com/naive-bayes-classifier-scratch-python/).
2. Start writing the glue logic.
3. Figure out the format for the (training and test) data and how it may need to be reformatted to suit our needs.  The training and test data are [here](https://www.kaggle.com/c/jigsaw-toxic-comment-classification-challenge/data).  Incidentally, they are csv (comma-spaced-variables) format.  There is Python libraries built specifically for handling csv files, which you can read about [here](https://docs.python.org/3/library/csv.html).
4. Start writing code for each of the six Bayes classifiers (toxic, severe_toxic, obscene, threat, insult, identity_hate)
5. Integrate the six classifiers into the glue logic to generate the output csv file that is to be uploaded to Kaggle.
