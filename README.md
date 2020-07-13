# Luvit

An API to consult and insert products
 
## Setup

#### Local Environment Setup

* Clone repository

git clone repo
cd repo

* Create and active virtual environment

virtualenv -p python3 eb-virt
source eb-virt/bin/activate

* Install dependencies 

cd luvitdjango-project
pip install -r requirements.txt

* Configure app
 
cp .env.dist to .env 
change the values according to your environment 


* Test Server 
###### Getting list of products
curl -H "Content-Type: application/json" http://luvit-env.eba-jbjf4g2s.us-east-1.elasticbeanstalk.com/api/products/

###### Bulk insert products
curl -H "Content-Type: application/json" -d '{"products": [{"name": "Bed shet",  "value": 200.0, "discount_value":50.0, "stock": 4}]}' http://luvit-env.eba-jbjf4g2s.us-east-1.elasticbeanstalk.com/api/products/bulk_insert/