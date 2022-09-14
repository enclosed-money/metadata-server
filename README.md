# Metadata Server

Server for [enclosed.money](https://www.enclosed.money) metadata. To be replaced with on-chain solution.

### Routes
api/token/{token_id}
* Returns the metadata JSON for a token that is [standard compliant](https://docs.opensea.io/docs/metadata-standards) 

api/image/{token_id}
* Returns the dynamic image for the NFT

### Installation & Usage

NB: Make sure Docker is installed on machine and running 
1. Clone repo
2. cd metadata-server
3. Build and run using docker-compose:
> docker-compose up -d --build
4. With your favourite HTTP tool (Postman, curl or my personal favourite [HTTPie](https://httpie.io/cli)) test with GET request:
> GET http://localhost:8000/api/token/0xdAC17F958D2ee523a2206206994597C13D831ec7999

In this example the token ID has the USDT contract address encoded and a value of 999 units

To run tests use:

> docker-compose exec server python -m pytest

### Roadmap

Proof-of-concept:

* Implement generation of current SVG designs in app/image.py 
* Update get_image endpoint with generative function

Future implementations:

* Add /info route with endpoint that returns an info page for a specific token on the site 
