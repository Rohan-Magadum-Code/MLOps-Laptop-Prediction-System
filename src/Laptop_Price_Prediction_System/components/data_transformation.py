import os
import pandas as pd
import re
from sklearn.model_selection import train_test_split
from Laptop_Price_Prediction_System import logger
from Laptop_Price_Prediction_System.entity.config_entity import DataTransformationConfig

class DataTransformation:
    def __init__(self, config: DataTransformationConfig):
        self.config = config
    
    def fetch_processor(self, text):
        text = text.lower()

        if 'intel core i7' in text:
            return 'Intel Core i7'
        elif 'intel core i5' in text:
            return 'Intel Core i5'
        elif 'intel core i3' in text:
            return 'Intel Core i3'
        elif 'intel' in text:
            return 'Other Intel Processor'
        elif 'amd' in text:
            return 'AMD Processor'
        else:
            return 'Other Processor'
    
    def fetch_memory(self, text):
        ssd = 0
        hdd = 0
        hybrid = 0
        flash = 0

        if pd.isna(text):
            return pd.Series([ssd, hdd, hybrid, flash])

        text = text.lower()
        parts = text.split('+')

        for part in parts:
            part = part.strip()
            num_match = re.search(r'\d+', part)
            value = int(num_match.group())

            if 'gb ssd' in part:
                ssd += value
            elif 'tb hdd' in part:
                hdd += value
            elif 'hybrid' in part:
                hybrid += value
            elif 'flash' in part:
                flash += value

        return pd.Series([ssd, hdd, hybrid, flash])
    
    def categorize_os(self, input_str):
        input_str = str(input_str)

        if 'Windows 7' in input_str or 'Windows 10' in input_str or 'Windows 10 S' in input_str:
            return 'Windows'
        elif 'macOS' in input_str or 'Mac OS X' in input_str:
            return 'Mac'
        elif 'Linux' in input_str:
            return 'Linux'
        elif 'Chrome OS' in input_str:
            return 'Chrome OS'
        else:
            return 'No OS'
    
    def transform(self):
        logger.info("Loading Dataset")
        data = pd.read_csv(self.config.data_dir)

        logger.info("Creating Screen features")
        data['Touchscreen'] = data['ScreenResolution'].apply(lambda x: 1 if 'Touchscreen' in x else 0)

        data['IPS'] = data['ScreenResolution'].apply(lambda x: 1 if 'IPS' in x else 0)

        new = data['ScreenResolution'].str.split('x', n=1, expand=True)
        data['X_res'] = new[0].str.extract(r'(\d+)').astype('int')
        data['Y_res'] = new[1].astype('int')

        data['ppi'] = ((data['X_res']**2 + data['Y_res']**2)**0.5) / data['Inches']

        logger.info("Creating CPU features")
        data['Cpu Name'] = data['Cpu'].apply(lambda x: x.split()[0])

        data['Cpu Speed (GHz)'] = data['Cpu'].str.extract(r'(\d+\.\d+)GHz').astype(float)
        data['Cpu Speed (GHz)'] = data['Cpu Speed (GHz)'].fillna(data['Cpu Speed (GHz)'].mean())

        data['Cpu brand'] = data['Cpu'].apply(self.fetch_processor)

        logger.info("Transforming RAM")
        data.rename(columns={'Ram': 'Ram (GB)'}, inplace=True)
        data['Ram (GB)'] = data['Ram (GB)'].str.replace('GB', '').astype(int)

        logger.info("Transforming Memory")
        data[['SSD', 'TB HDD', 'TB Hybrid', 'Flash Storage']] = data['Memory'].apply(self.fetch_memory)

        logger.info("Creating GPU feature")
        data['Gpu Brand'] = data['Gpu'].apply(lambda x: x.split()[0])

        data['OS'] = data['OpSys'].apply(self.categorize_os)

        data['Weight'] = data['Weight'].str.replace('kg', '').astype(float)

        logger.info("Dropping unused columns")
        data.drop(columns=['ScreenResolution', 'Cpu', 'Memory', 'Gpu', 'OpSys', 'X_res', 'Y_res'], inplace=True)

        X = data.drop(columns=["Price"])
        y = data["Price"]

        logger.info("Splitting Dataset")
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

        train_df = X_train.copy()
        train_df['Price'] = y_train

        test_df = X_test.copy()
        test_df['Price'] = y_test

        train_df.to_csv(os.path.join(self.config.root_dir, "train.csv"), index = False)
        test_df.to_csv(os.path.join(self.config.root_dir, "test.csv"), index = False)