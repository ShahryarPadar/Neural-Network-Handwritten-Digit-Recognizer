from pickle import load
from scipy.special import expit
from numpy import dot,argmax


with open("Model/weight_Input_to_hidden1.h5",mode="rb") as file:
    weight_Input_to_hidden1=load(file)


with open("Model/weight_hidden1_to_hidden2.h5",mode="rb") as file:
    weight_hidden1_to_hidden2=load(file)


with open("Model/weight_hidden2_to_output.h5",mode="rb") as file:
    weight_hidden2_to_output=load(file)



def predict(array):
    sigmoid=lambda x:expit(x)

    Input_to_hidden1_data = dot(weight_Input_to_hidden1,array)
    Input_to_hidden1_data = sigmoid(Input_to_hidden1_data)
    
    hidden1_to_hidden2_data = dot(weight_hidden1_to_hidden2,Input_to_hidden1_data)
    hidden1_to_hidden2_data = sigmoid(hidden1_to_hidden2_data)
    
    hidden2_to_output_data = dot(weight_hidden2_to_output,hidden1_to_hidden2_data)
    out = sigmoid(hidden2_to_output_data)
    
    result = argmax(out)
    return result


