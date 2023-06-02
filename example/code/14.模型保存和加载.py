from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
from sklearn.linear_model import SGDRegressor
from sklearn.linear_model import Ridge,RidgeCV
import joblib


def ridge_jump_load(mode: str):
    """
    模型的保存和加载
    :arg mode:jump/load 。对应保存和加载
    :return:
    """
    # 1 获取数据
    import pandas as pd
    import numpy as np

    data_url = "http://lib.stat.cmu.edu/datasets/boston"
    raw_df = pd.read_csv(data_url, sep="\s+", skiprows=22, header=None)
    boston_data = np.hstack([raw_df.values[::2, :], raw_df.values[1::2, :2]])
    target = raw_df.values[1::2, 2]

    # 2 数据集划分
    x_feature_train, x_feature_test, y_target_train, y_target_test = train_test_split(boston_data, target,
                                                                                      random_state=22)
    # 3 特征工程-标准化
    transfer = StandardScaler()
    x_feature_train = transfer.fit_transform(x_feature_train)
    x_feature_test = transfer.fit_transform(x_feature_test)

    if mode == 'jump':
        # 4 机器学习-线性回归（随机梯度下降）
        #estimator = Ridge(alpha=0.1)
        estimator = RidgeCV(alphas=(0.1, 1, 10))
        estimator.fit(x_feature_train, y_target_train)
        joblib.dump(estimator, "./14.模型保存和加载/test.pkl")
    elif mode == 'load':
        estimator = joblib.load("./14.模型保存和加载/test.pkl")
    else:
        raise '入参错误'

    # 5 模型评估
    # 5.1 获取系数
    y_target_predict = estimator.predict(x_feature_test)
    print(f'预测测试集目标值为\n {y_target_predict}')
    print(f'测试集的目标值为\n {y_target_test}')
    print(f'模型中的系数为\n：{estimator.coef_}')
    print(f'模型中的偏置为\n：{estimator.intercept_}')

    # 5.2 评价
    # 均方误差
    error_mean_square = mean_squared_error(y_target_test, y_target_predict)
    print(f'测试机的预测值和测试机的目标值的均方误差为:\n {error_mean_square}')

if __name__ == '__main__':
    ridge_jump_load('load')
