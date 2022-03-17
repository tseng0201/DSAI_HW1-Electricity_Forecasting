import csv
import numpy as np
import argparse
from sklearn.ensemble import IsolationForest
feburay_2020 = list()
april_2020 = list()
feburay_2022 = list()

input_data_name = list()
output_data_name = list()
def rmse(value, mean):
    return np.sqrt(np.mean(np.square(value-mean)))
if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--training',
                       default='近三年每日尖峰備轉容量率.csv',
                       help='input training data file name')
    parser.add_argument('--training2',
                       default='本年度每日尖峰備轉容量率.csv',
                       help='input training data file name')
    parser.add_argument('--output',
                        default='submission.csv',
                        help='output file name')
    args = parser.parse_args()
    #從input_data_name中尋找需要的資料
    for file_name in [args.training, args.training2]:
        with open(file_name, newline='', encoding="utf-8") as csvfile:
            rows = csv.reader(csvfile)
            for row in rows:
                if ('2020/2/' in row[0]):
                    feburay_2020.append(float(row[1]))
                elif ('2020/4/' in row[0]):
                    april_2020.append(float(row[1]))
                elif ('2022/02/' in row[0]):
                    feburay_2022.append(float(row[1])) 
                    
                    
    
    
    feburay_2020 = np.array(feburay_2020)
    april_2020 = np.array(april_2020)
    feburay_2022 = np.array(feburay_2022)
    predict = 0 
    for i in range(100):
        tree = IsolationForest(n_estimators  = 100).fit(feburay_2020.reshape((29,1)))
        abnormal = tree.predict(feburay_2020.reshape((29,1)))
        new_feburay_2020 = feburay_2020[abnormal == 1]
        
        tree = IsolationForest(n_estimators  = 100).fit(feburay_2022.reshape((28,1)))
        abnormal = tree.predict(feburay_2022.reshape((28,1)))
        new_feburay_2022 = feburay_2022[abnormal == 1]
        
        tree = IsolationForest(n_estimators  = 100).fit(april_2020.reshape((30,1)))
        abnormal = tree.predict(april_2020.reshape((30,1)))
        new_april_2020 = april_2020[abnormal == 1]
        
        predict += np.mean(new_feburay_2022) * np.mean(new_april_2020) / np.mean(new_feburay_2020)
    predict = round(predict/100)
    #產生outputcsv 由於輸入數據單位萬瓩 故要*10來表示成MW
    with open(args.output, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['date','operating_reserve(MW)'])
        writer.writerow([20220330, predict*10])
        writer.writerow([20220331, predict*10])
        for i in range(1, 14):
            writer.writerow([20220400+i, predict*10])
