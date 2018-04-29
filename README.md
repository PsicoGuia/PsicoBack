# PsicoBack

Aqui Paso JuanSe

sudo apt-get install binutils libproj-dev gdal-bin

sql '''

-- Enable PostGIS (includes raster)
CREATE EXTENSION postgis;
-- Enable Topology
CREATE EXTENSION postgis_topology;
-- Enable PostGIS Advanced 3D 
-- and other geoprocessing algorithms
-- sfcgal not available with all distributions
CREATE EXTENSION postgis_sfcgal;
-- fuzzy matching needed for Tiger
CREATE EXTENSION fuzzystrmatch;
-- rule based standardizer
CREATE EXTENSION address_standardizer;
-- example rule data set
CREATE EXTENSION address_standardizer_data_us;
-- Enable US Tiger Geocoder
CREATE EXTENSION postgis_tiger_geocoder;

'''

### Windows

https://docs.djangoproject.com/en/2.0/ref/contrib/gis/install/#postgisasb

https://trac.osgeo.org/osgeo4w/


