##############################################################
#
#  Kaggle Competition 
#  Toxic Comment Classification Challeng
#  https://www.kaggle.com/c/jigsaw-toxic-comment-classification-challenge
#
#  New York Group "Anagram"
#
#  This is the main script.
# 
#  Changelog:
#
#   1.  Inauguration code.  2018/01/11
#
#   Copyright, 2018  Anagram-Toxic
#
#   License: Apache v. 2
#
###############################################################

from sys import argv, exc_info


# First, import the data file as provided by the user...
try:
    # It is assumed that the input line will be something like:
    # $python3 <training_data_filename> <test_data_filename> <output_filename>
    fTraining = open(argv[1], 'r')
    fTest = open(argv[2], 'r')
    fOut = open(argv[3], 'w')
except:
    print("Unexpected error:", exc_info()[0])
    print("Expected input: $python3 <training_data_filename> <test_data_filename> <output_filename>")
    raise

