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



# Docker build
cd ~/gitKraken/PsicoBack && git pull  &&
sudo docker build -t psicoback/dev . &&
sudo docker stop PsicoBack-dev &&
sudo docker rm PsicoBack-dev &&
sudo docker run --name PsicoBack-dev -d -p 8000:8000 -e "DJANGO_SETTINGS_MODULE=PsicoBack.development_docker" psicoback/dev 


# Normal run ubuntu
## install
python3 -m venv env
source env/bin/activate
pip3 install -r PsicoBack/requriments.txt

## run
source env/bin/activate
python3 PsicoBack/manage.py runserver 0:8000 --settings=PsicoBack.development