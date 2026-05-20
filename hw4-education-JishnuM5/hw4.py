'''
Jishnu Mehta   
Intermediate Data Programming
This file implements the programs for HW4
'''

import pandas as pd
# Your imports here
import matplotlib.pyplot as plt
from sklearn.tree import DecisionTreeRegressor
from sklearn.metrics import mean_squared_error
from sklearn.model_selection import train_test_split
from cse163_imgd_NCHS import compare_hw4_images


# Define these functions here
def compare_bachelors_1980(df):
    """
    This method returns a DataFrame showing total bachelor's degree attainment percentage in 1980 by sex
    """
    return df.loc[(df["Year"] == 1980) & (df["Min degree"] == "bachelor's") &
                  (df["Sex"] != "A"), ["Sex", "Total"]]


def top_2_2000s(df, sex='A'):
    """
    This method returns the top two most commonly awarded degrees from 2000-2010
    """
    two_ks = (df["Year"] >= 2000) & (df["Year"] <= 2010)
    df = df.loc[(df["Sex"] == sex) & two_ks].groupby("Min degree", as_index=False)["Total"].mean()
    return df.nlargest(2, "Total")


def line_plot_bachelors(df):
    """
    This method graphs the percent of people who have at least a Bachelor's degree over time
    """
    df = df[(df["Sex"] == "A") & (df["Min degree"] == "bachelor's")]
    df.plot(x="Year", y="Total", grid=True, legend=False)
    plt.title("Percentage Earning Bachelor's over Time")
    plt.xlabel("Year")
    plt.ylabel("Percentage")
    plt.savefig('line_plot_bachelors.png', bbox_inches='tight')


def bar_chart_high_school(df):
    """
    This method charts total percentages of male, females, and all people who graduated high school in 2009
    """
    df = df.loc[(df["Year"] == 2009) & (df["Min degree"] == "high school")]
    print(df)
    df.loc[:, 'Total'] = df['Total'] - 80
    df.plot(kind="bar", x="Sex", y="Total", color=["blue", "red", "green"], grid=True, legend=False)
    plt.xticks(rotation=0)
    plt.yticks(ticks=[0, 2, 4, 6, 8, 10], labels=[80, 82, 84, 86, 88, 90])
    plt.grid(axis="x")
    plt.title("Percentage Completed High School by Sex")
    plt.xlabel("Sex")

    plt.ylabel("Percentage")
    plt.savefig('bar_chart_high_school.png', bbox_inches='tight')


def plot_hispanic_min_degree(df):
    """
    This method graphs the percentage of Hispanic people with high school and bachelor's degrees, 1990-2010
    """

    degrees = (df["Min degree"] == "bachelor's") | (df["Min degree"] == "high school")
    period = (df["Year"] >= 1990) & (df["Year"] <= 2010) 

    df = df.loc[degrees & period, ["Year", "Hispanic", "Min degree"]]
    df.pivot_table(values="Hispanic", index="Year", columns="Min degree").plot(grid=True)
    plt.title("Percentage Hispanic Completed High School and Bachelor's over Time")
    plt.xlabel("Year")
    plt.xticks(ticks=[1990, 1995, 2000, 2005, 2010])
    plt.legend(["Bachelors", "High School"])
    plt.savefig('plot_hispanic_min_degree.png', bbox_inches='tight')


def fit_and_predict_degrees(df):
    """
    This method uses regression to predict the percentage of degrees attained for a given year, sex, and 
    minimum degree. It trains using 80% of the data, tests with 20%, and returns the test mean squared error
    """
    # Preprocessing data
    df = df.loc[:, "Year":"Total"].dropna()
    cols = ["Sex", "Min degree"]
    df_encoded = pd.get_dummies(df, prefix=cols)
    features_train, features_test, labels_train, labels_test = train_test_split(
        df_encoded.loc[:, df_encoded.columns != 'Total'], df_encoded['Total'], test_size=0.2)

    # An alternate way of doing the problem, although more code
    # encoder = OneHotEncoder(sparse_output=False)
    # one_hot_encoded = encoder.fit_transform(df[cols])
    # df_encoded = pd.DataFrame(one_hot_encoded, columns=encoder.get_feature_names_out(cols))
    # df_encoded = pd.concat([df.reset_index(drop=True), df_encoded], axis=1)
    # df_encoded = df_encoded.drop(cols, axis=1)
    # train_df = df_encoded.sample(frac=0.8)
    # test_df = df_encoded.drop(train_df.index)

    # Training and predicting based of random samples=
    model = DecisionTreeRegressor(random_state=0)  
    model.fit(features_train, labels_train) 
    predictions = model.predict(features_test)
    print("Predictions:", predictions)
    print("Actual     :", labels_test.values)
    return mean_squared_error(labels_test, predictions)


def main():
    df = pd.read_csv('nces-ed-attainment.csv', na_values=['---'])
    # Call your functions here
    # use plt.clf() to clear your figure between each plot!
    print(compare_bachelors_1980(df))
    print(top_2_2000s(df, 'A'))
    line_plot_bachelors(df)
    plt.clf()
    bar_chart_high_school(df)
    plt.clf()
    plot_hispanic_min_degree(df)
    fit_and_predict_degrees(df)
    print('done')
    compare_hw4_images()


if __name__ == '__main__':
    main()