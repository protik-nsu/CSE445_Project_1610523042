{\rtf1\ansi\ansicpg1252\cocoartf2512
\cocoatextscaling0\cocoaplatform0{\fonttbl\f0\fswiss\fcharset0 Helvetica;}
{\colortbl;\red255\green255\blue255;}
{\*\expandedcolortbl;;}
\paperw11900\paperh16840\margl1440\margr1440\vieww25400\viewh16000\viewkind0
\pard\tx566\tx1133\tx1700\tx2267\tx2834\tx3401\tx3968\tx4535\tx5102\tx5669\tx6236\tx6803\pardirnatural\partightenfactor0

\f0\fs24 \cf0 \
\
import numpy as np \
import pandas as pd \
import seaborn as sns; sns.set(style="ticks", color_codes=True)\
from sklearn.model_selection import train_test_split\
from sklearn.tree import DecisionTreeRegressor \
from sklearn.svm import SVR\
from sklearn.feature_selection import RFE\
from sklearn.neural_network import MLPRegressor\
from sklearn.metrics import mean_absolute_error\
from sklearn.model_selection import KFold\
import matplotlib.pyplot as plt\
\
\
\
import os\
print(os.listdir("../input"))\
\
dataset = pd.read_csv("../input/train.csv", names=['Store','Dept','Date','weeklySales','isHoliday'],sep=',', header=0)\
features = pd.read_csv("../input/features.csv",sep=',', header=0,\
                       names=['Store','Date','Temperature','Fuel_Price','MarkDown1','MarkDown2','MarkDown3','MarkDown4',\
                              'MarkDown5','CPI','Unemployment','IsHoliday']).drop(columns=['IsHoliday'])\
stores = pd.read_csv("../input/stores.csv", names=['Store','Type','Size'],sep=',', header=0)\
dataset = dataset.merge(stores, how='left').merge(features, how='left')\
\
dataset\
\
def scatter(dataset, column):\
    plt.figure()\
    plt.scatter(dataset[column] , dataset['weeklySales'])\
    plt.ylabel('weeklySales')\
    plt.xlabel(column)\
\
scatter(dataset, 'Fuel_Price')\
scatter(dataset, 'Size')\
scatter(dataset, 'CPI')\
scatter(dataset, 'Type')\
scatter(dataset, 'isHoliday')\
scatter(dataset, 'Unemployment')\
scatter(dataset, 'Temperature')\
scatter(dataset, 'Store')\
scatter(dataset, 'Dept')\
\
}