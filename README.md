# Leaflet Testing
Collection of code to create tiles of histo images to allow display using the [leaflet JavaScript library](https://leafletjs.com/).
This repo contains the commit history of pyLeafletTiler as it was being built, as well as several pre-processed image files for testing.

## About
Displays multiple histo images overlayed on top of each other. Images can be viewed at different zoom levels for more/less detail, and individual layers can be toggled on/off to show or hide the layer. Markers and annotations can be added (e.g. to indicate ROIs) at different zoom levels.

## Usage
As of right now, images must first be loaded into the Main.py file for processing (to add hue). These processed images should then be loaded into the Jupyter notebook to create tiles saved in a specific folder structure, and then this can be referenced in the html code to load the Leaflet app.

## Dependencies
* Imagemagick for the hard part of recursive image tiling
* Leaflet Javascript Library (usually hosted externally)
* Python 3.7.4 and Python packages:
    * docopt=0.6.2
    * opencv=4.2.0.34
    * pillow=7.1.2
    * numpy=1.17.2



