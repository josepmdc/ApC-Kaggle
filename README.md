# Pràctica Kaggle APC UAB 2021-22

**Name:** Josep Maria Domingo Catafal

**NIU:** 1599946

**DATASET:** All products available on the Sephora website

**URL:** [kaggle](https://www.kaggle.com/raghadalharbi/all-products-available-on-sephora-website)

## Information about the dataset
Nowadays, most people buy online. This allows us to have a lot of data about the products and how they are received by the customers. It's very important when developing a new product to make sure it's something people will want to buy. So we can use all the data collected from online stores to predict if a product will have a good acceptance or not, and improve before releasing it if it doesn't.

In this case, we have information about all the different products of the Sephora online store. Sephora is a store specialized in cosmetics. Our goal will be to train different models in order to predict with the best accuracy as possible if the consumers of the store will like a product or not.

Heres' a description of all the attributes:

| Feature | Type | Description |
|:---|:---|:---
| id | int | The product ID at Sephora's website |
| brand | object | The brand of the product at Sephora's website |
| category | Object | The category of the product at Sephora's website |
| name | Object | The name of the product at Sephora's website |
| size | Object | The size of the product |
| rating | float | The rating of the product |
| numberofreviews | int | The number of reviews of the product |
| love | int | The number of people loving the product |
| price | float | The price of the product |
| value_price |	float | The value price of the product (for discounted products) |
| URL | object | The URL link of the product |
| MarketingFlags | bool | The Marketing Flags of the product from the website if they were exclusive or sold online only |
| MarketingFlags_content | 	object | The kinds of Marketing Flags of the product |
| options | object | The options available on the website for the product like colors and sizes|
| details | object | Details of the product available on the website |
| howtouse | object | The instructions of the product if available |
| ingredients | object | The ingredients of the product if available |
| online_only | int | If the product is sold online only |
| exclusive | int | If the product is sold exclusively on Sephora's website |
| limited_edition | int | If the product is limited edition |
| limitedtimeoffer | int | The product has a limited time offer |

## Setup
`python -m venv venv`

`. venv/bin/activate`

**Note:** If you are using the fish shell, run this instead:
`. venv/bin/activate.fish`

`pip install -r requirements.txt`

## Demo
A demo is available, you can use it running the following command in the
terminal:

```sh
python3 src/main.py
```

## Models
**Linear Regression** R2 score = 0.55

**Decision Tree Regressor**: R2 score = 0.66

**Random Forest Regressor**: R2 score = 0.75

**Gradient Boosting Regressor**: R2 score = 0.70

## Future improvements

## License
This project was developed under the AGPL v3.0 license (GNU Affero General Public License v3.0).
For more information read the [full license](https://github.com/josepmdc/ApC-Kaggle/blob/master/LICENSE)

