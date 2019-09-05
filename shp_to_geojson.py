#!/usr/bin/env python
# coding: utf-8

# Featured City Factsheets - Place Matters (Farrell, Wheat, and Grandet 2019)
# Nich Tremper
# August 2019

"""
Purpose: This file creates the administrative boundary files used in the place matters toolkit fact sheets
sent to stakeholders in New York, Miami, Detroit, Chicago, Houston, and San Francisco. As of August
29, 2019 this file CANNOT be run on JPMC systems because it uses the package geopandas, which is 
not on gtvuln or gtgold. This file was run on my personal computer and sent to institute@jpmchase.com.

This file imports shape files, changes projections to web mercator, and then exports geojson files to
be sent to the Institute.

Inputs: Boundary files for all states other than New York were downloaded as 2019 Census TIGER place 
shapefiles. Files can be downloaded from https://www2.census.gov/geo/tiger/TIGER2019/PLACE/ and
are organized by state FIPS codes:
	06 = California
	12 = Florida
	17 = Illinois
	26 = Michigan
	48 = Texas

Boundary files for New York were downloaded as counties to capture all five bouroughs in New York
City. County shapefile can be downloaded from: https://www2.census.gov/geo/tiger/TIGER2019/COUNTY/.

NOTE ON WORKING WITH SHAPEFILES: Although shapefiles can be identified by .shp, a shapefile is a collection
of multiple geographic files. In order to run this code you will download a zipped file for each state
or one zip file for all US counties. All files in the zip file must be in the same file from which you read
the .shp file. 

Outputs: geojson files for each area
"""

# 1. Introduction
print("1. Introduction")

## load packages
import geopandas as gpd
import pandas as pd
import datetime
from bokeh.models import GeoJSONDataSource
from bokeh.plotting import figure, show

## change to working directory
cd "C:\Users\nicht\communities-factsheets\"
print(pwd, datetime.datetime.now())


# 2. CALIFORNIA
print("2. California", datetime.datetime.now())

## read shape file into geopandas
ca_geo = gpd.read_file("tl_2019_06_place.shp")
ca_geo["NAME"] = ca_geo["NAME"].str.strip()

## filter out the San Francisco polygon
sanf = ca_geo.loc[(ca_geo["NAME"] == "San Francisco")]

## Reproject to web mercator
sanf = sanf.to_crs(epsg = 3857)
print(sanf.crs)
sanf.to_file("sanFrancisco_mercator.geojson", driver = "GeoJSON")

## do the same things for Oakland
oak = ca_geo.loc[ca_geo["NAME"] == "Oakland"]

oak = oak.to_crs(epsg = 3857)
print(oak.crs)
oak.to_file("oakland_mercator.geojson", driver = "GeoJSON")


# FLORIDA
print("3. Florida", datetime.datetime.now())

fl_geo = gpd.read_file("tl_2019_12_place.shp")
fl_geo["NAME"] = fl_geo["NAME"].str.strip()


miami = fl_geo.loc[(fl_geo['NAME'] == "Miami")]
miami = miami.to_crs(epsg = 3857)
print(miami.crs)

miami.to_file("miami_mercator.geojson", driver = "GeoJSON")

ftlaud = fl_geo.loc[fl_geo["NAME"] == "Fort Lauderdale"]
ftlaud = ftlaud.to_crs(epsg = 3857)
print(ftlaud.crs)
ftlaud.to_file("FtLauderdale_mercator.geojson", driver = "GeoJSON")


# ILLINOIS
print("4. Illinois", datetime.datetime.now())

il_geo = gpd.read_file("tl_2019_17_place.shp")
il_geo["NAME"] = il_geo["NAME"].str.strip()

chicago = il_geo.loc[il_geo["NAME"] == "Chicago"]
chicago = chicago.to_crs(epsg = 3857)
print(chicago.crs)

chicago.to_file("chicago_mercator.geojson", driver = "GeoJSON")


# MICHIGAN
print("5. Michicagn", datetime.datetime.now())

mi_geo = gpd.read_file("tl_2019_26_place.shp")
mi_geo["NAME"] = mi_geo["NAME"].str.strip()


detroit = mi_geo.loc[mi_geo["NAME"] == "Detroit"]
detroit = detroit.to_crs(epsg = 3857)
print(detroit.crs)

detroit.to_file("detroit_mercator.geojson", driver = "GeoJSON")


# NEW YORK
print("6. New York", datetime.datetime.now())

ny_geo = gpd.read_file("tl_2019_us_county.shp")
ny_geo = ny_geo.loc[ny_geo["STATEFP"] == "36"]
ny_geo.sort_values(by = "NAME")


## From the county list, I need to create a geodataframe for each county
## where New York = Manhattan, Kings = Brooklyn, Richmond = Staten Island
## within the loop I reproject and save the geojson file.
counties = ["New York", "Bronx", "Kings", "Richmond", "Queens"]
c = {}

for county in counties:
    c[county] = ny_geo.loc[ny_geo["NAME"] == str(county)]
    c[county] = c[county].to_crs(epsg = 3857)
    c[county].to_file(str(county) + "_mercator.geojson", driver = "GeoJSON")

# TEXAS
print("7. Texas", datetime.datetime.now())

tx_geo = gpd.read_file("tl_2019_48_place.shp")
tx_geo["NAME"] = tx_geo["NAME"].str.strip()

houston = tx_geo.loc[tx_geo["NAME"] == "Houston"]
houston = houston.to_crs(epsg = 3857)
print(houston.crs)

houston.to_file("houston_mercator.geojson", driver = "GeoJSON")



