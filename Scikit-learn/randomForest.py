# ランダムフォレスト実装(randomForest.py)
# ライブラリの読み込み
import glob
import pandas as pd
import numpy as np
import category_encoders as ce
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import r2_score
