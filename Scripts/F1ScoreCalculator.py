##F1 Score
import pandas as pd
import sys
from sklearn.metrics import confusion_matrix
from sklearn import metrics
from sklearn.metrics import classification_report

categories = ["deleted"]


try:
    truth_file = str(sys.argv[1])
    prediction_file = str(sys.argv[2])
except:
    print("something went wrong in F1Score Calculation")

    
def to_binary(predictions):
    for category in categories:
        predictions[category] = [1 if row > 0.5 else 0 for row in predictions[category]]
    return predictions


def get_f1_results(truth, predictions, name):
# Label in Confusion Matrix Toxic und Not Toxic
    target_names = ['not toxic','toxic']
    predictions = to_binary(predictions)

    print(name + ": " + str(metrics.classification_report(truth[categories], predictions[categories], target_names=target_names)))
    print("Micro: " + str(metrics.f1_score(truth[categories], predictions[categories], average='micro')))
    print("Macro: " + str(metrics.f1_score(truth[categories], predictions[categories], average='macro')))
    print("Average: " + str(metrics.f1_score(truth[categories], predictions[categories], average='weighted')))

    ## print(classification_report(y_true, y_pred, target_names=target_names))
     ##        precision    recall  f1-score   support

if __name__ == "__main__":
    #truth = pd.read_csv("/Users/sebastian/Desktop/Fasttext_kaggle/truth.csv")
    truth = pd.read_csv(truth_file)
    prediction1 = pd.read_csv(prediction_file)

    #prediction1 = pd.read_csv("/Users/sebastian/Desktop/Fasttext_kaggle/truth_prediction_h1.csv")

    get_f1_results(truth, prediction1, "Prediction 1")

confusion_matrix(truth, prediction1)
