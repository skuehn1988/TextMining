import pandas as pd
from sklearn import metrics
from sklearn.metrics import classification_report

categories = ["deleted"]

user = "banana"

def to_binary(predictions):
    for category in categories:
        predictions[category] = [1 if row > 0.5 else 0 for row in predictions[category]]
    return predictions


def get_f1_results(truth, predictions, name):
    target_names = ['not toxic','toxic']
    predictions = to_binary(predictions)

    print(name + ": " + str(metrics.classification_report(truth[categories], predictions[categories], target_names=target_names)))
    print("Micro: " + str(metrics.f1_score(truth[categories], predictions[categories], average='micro')))
    print("Macro: " + str(metrics.f1_score(truth[categories], predictions[categories], average='macro')))
    print("Average: " + str(metrics.f1_score(truth[categories], predictions[categories], average='weighted')))

    ## print(classification_report(y_true, y_pred, target_names=target_names))
     ##        precision    recall  f1-score   support

if __name__ == "__main__":
    truth = pd.read_csv("/Users/"+user+"/Desktop/Betty Example/truth.csv")

    prediction1 = pd.read_csv("/Users/"+user+"/Desktop/Betty Example/prediction.csv")

    get_f1_results(truth, prediction1, "Prediction 1")
