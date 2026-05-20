'''
Jishnu Mehta
Period 1
HW7 - Mapping
'''
import pandas as pd
import geopandas as gpd
import matplotlib.pyplot as plt
from cse163_imgd_NCHS import compare_image


def load_in_data(census_file, access_filename):
    '''
    census_file = the filename for the census dataset, JSON
    access_filename = the filename for the food access dataset, CSV
    This should merge the two datasets on CTIDFP00 / CensusTract
    and return the result as a GeoDataFrame.
    '''
    census_gpd = gpd.read_file(census_file)
    access_pd = pd.read_csv(access_filename)

    return census_gpd.merge(access_pd, left_on="CTIDFP00", right_on="CensusTract", how="left")


def percentage_food_data(state_data):
    '''
    This method takes a GeoDataFrame, state_data, and returns the percentage of
    census tract food access data that is NOT NaN in the GeoDataFrame as a
    float.
    '''
    df_len = len(state_data.index)
    filtered_len = len(state_data.dropna().index)
    return filtered_len / df_len * 100


def plot_map(state_data):
    '''
    This method takes the state data and plots a simple map of Washington with all census tracts.
    '''
    state_data.plot()
    plt.title("Washington State")
    plt.savefig('map.png')


def plot_population_map(state_data):
    '''
    This method takes the state data and plots a map of Washington colored by population.
    The population is grouped by census tract.
    '''
    fig, ax = plt.subplots(1)
    state_data.plot(color="#EEEEEE", ax=ax)
    state_data.plot(column="POP2010", ax=ax, legend=True)
    plt.title("Washington Census Tract Populations")
    plt.savefig("population_map.png") 


def plot_population_county_map(state_data):
    '''
    This method takes state data and plots a map of Washington colored by county population.
    '''
    fig, ax = plt.subplots(1)
    state_data.plot(color="#EEEEEE", ax=ax)

    state_data = state_data[['County', 'POP2010', 'geometry']]
    state_data = state_data.dissolve(by="County", aggfunc="sum")
    state_data.plot(column="POP2010", ax=ax, legend=True)
    plt.title("Washington County Populations")
    plt.savefig("county_population_map.png") 


def plot_food_access_by_county(state_data):
    '''
    This method takes the state data and plots four maps. 
    Each map plots the ratio of a low access population to the total population by county.
    The four low access populations plotted are: rural, rural + low income, urban, urban + low income.
    '''
    # Creating plots and grey backgrounds
    fig, axs = plt.subplots(2, 2, figsize=(20, 10))
    for ax in axs.flat:
        state_data.plot(color="#EEEEEE", ax=ax)

    state_data = state_data[['County', 'geometry', 'POP2010',
                             'lapophalf', 'lapop10', 'lalowihalf', 'lalowi10']]
    # Creating ratio columns
    state_data = state_data.dissolve(by="County", aggfunc="sum")
    state_data['lapophalf_ratio'] = state_data['lapophalf'] / state_data['POP2010']
    state_data['lapop10_ratio'] = state_data['lapop10'] / state_data['POP2010']
    state_data['lalowihalf_ratio'] = state_data['lalowihalf'] / state_data['POP2010']
    state_data['lalowi10_ratio'] = state_data['lalowi10'] / state_data['POP2010']

    # Plotting ratio data
    state_data.plot(column="lapophalf_ratio", vmin=0, vmax=1, ax=axs[0, 0], legend=True)
    axs[0, 0].set_title("Low Access: Half")
    state_data.plot(column="lapop10_ratio", vmin=0, vmax=1, ax=axs[1, 0], legend=True)
    axs[1, 0].set_title("Low Access: 10")
    state_data.plot(column="lalowihalf_ratio", vmin=0, vmax=1, ax=axs[0, 1], legend=True)
    axs[0, 1].set_title("Low Access + Low Income: Half")
    state_data.plot(column="lalowi10_ratio", vmin=0, vmax=1, ax=axs[1, 1], legend=True)
    axs[1, 1].set_title("Low Access + Low Income: 10")

    plt.savefig("county_food_access.png") 


def plot_low_access_tracts(state_data):
    '''
    This method takes the state data and plots low access census tracts, as defined in the README.MD file.
    '''
    rural = state_data[state_data['Rural'] == 1]
    rural = rural[['CensusTract', 'geometry', 'POP2010', 'lapop10']]
    rural['lapop10_ratio'] = rural['lapop10'] / rural['POP2010']

    urban = state_data[state_data['Urban'] == 1]
    urban = urban[['CensusTract', 'geometry', 'POP2010', 'lapophalf']]
    urban['lapophalf_ratio'] = urban['lapophalf'] / urban['POP2010']

    urban = urban[(urban['lapophalf'] > 500) | (urban['lapophalf_ratio'] > .33)]
    print(urban.head())
    rural = rural[(rural['lapop10'] > 500) | (rural['lapop10_ratio'] > .33)]
    print(rural.head())

    low_access = gpd.GeoDataFrame(pd.concat([rural, urban], ignore_index=True))

    fig, ax = plt.subplots(1)
    state_data.plot(color="#EEEEEE", ax=ax)
    state_data = state_data.dropna(subset=['POP2010'])
    state_data.plot(color='#AAAAAA', ax=ax)
    low_access.plot(ax=ax)
    plt.title("Low Access Census Tracts")
    plt.savefig('low_access.png')


def main():
    '''
    Each of these methods needs to be implemented by the student.
    '''
    state_data = load_in_data(
        'food_access/washington.json',
        'food_access/food_access.csv'
    )

    plot_map(state_data)
    compare_image('map.png')
    plot_population_map(state_data)
    compare_image('population_map.png')
    plot_population_county_map(state_data)
    compare_image('county_population_map.png')
    plot_food_access_by_county(state_data)
    compare_image('county_food_access.png')
    plot_low_access_tracts(state_data)
    compare_image('low_access.png')


if __name__ == '__main__':
    main()
