# BV Ulster Coding Challenge - Sample App

![Bazaarvoice](img/bv_logo.png)

## :wave: Welcome to the BV Coding Challenge!

You will find everything you need here for the challenge including:

* Prerequisites
* Getting Started
* The Challenge
* The Requirements
* Useful Resources

## :white_check_mark: Prerequisites

You should have been provided with the "Get ready guide!" before the session. You can also download it from [here](docs/SetupGuideForCodingChallenge.docx). If you have any issues check the [troublshooting guide](Troubleshooting.md) or ask for help in the slack channel.

## :metal: Getting Started

#### Fork the project repo

Once logged into your GitHub account, go to https://github.com/bazaarvoice/bvcodingchallenge-sampleapp and fork the repo by click the "Fork" button at the top right of the page.

#### Clone the project repo

```bash
git clone git@github.com:{YOUR-GITHUB-USERNAME}/bvcodingchallenge-sampleapp.git
```

#### Browse to project folder

```bash
cd bvcodingchallenge-sampleapp
```

#### Start the application

```bash
docker-compose up
```

**Notes:**

1. Docker will pull the required images.
2. A database will be created and populated with sample data.
3. Flask and other requirements will be installed. See [requirements.txt](requirements.txt)
4. The application will be running at [http://localhost:5000](http://localhost:5000)

_**You may need to refresh the page as the database connects.**_

#### Stop the application
 
 ```bash
docker-compose down
 ```

#### Database GUI _(Optional)_

**Connection Details**

- Host: 127.0.0.1
- Port: 3357
- User: root
- Password: password
- Database: uu_code_challenge

**Dataset**
Inside the database, there is one table. Each row in the table contains the following attributes which you can use to produce your statistics:
- id: The reviews ID.
- brewery_id: the ID of the brewery.
- brewery_name: The name of the beers producing access.
- review_time: Timestamp of the time the review was made.
- review_overall: The overall rating of the beer.
- review_aroma: The rating of the beers aroma.
- review_appearance: The rating of the beers appearance.
- review_profilename: The profile name of the person who made the review.
- beer_style: The particular style of the beer.
- review_palate: The rating of the beers palate.
- review_taste: The rating of the beers taste.
- beer_name: The name of the beer.
- beer_abv: The beers ABV.
- beer_id: The id of the beer.

## :chart_with_upwards_trend: The Coding Challenge

Build a statistics dashboard to help a drinks retailer understand product sentiment based on customer ratings and reviews data.

## :thinking: Problem

As a drinks retailer, I want to be able to view key stats on how our products are performing so that I can make informed business decisions. However, right now, we can only view raw csv data which we use to create our own reports in a third-party analytics tool. Currently, creating reports takes a lot of time and effort for each operational team within the company. In addition to this, teams have to share their reports with one another, instead of having one centralized dashboard that everyone can view.

## :bulb: Solution

This repo includes a starter template “Flask” application which is linked to a database with roughly 2,500 beer ratings and reviews. You will be asked to query the database for key product statistics and send these through to the front end of the application where you can use HTML, CSS and JS to present the statistics to the end user.

**Tip:** Lookout for _HINTS:_ within the code for some guidance.
 
#### Who is the user?
 
Marketing and sales teams, analysts and product managers all need to be able to quickly pull up key stats on their products. These stats are used to make critical informed business decisions, for example, identifying drink products with low (1-2 star) ratings that need improvement or identifying trends in products that customers rate highly (4-5 star).

## :blue_book: Requirements

### Level 1 Requirements/User Stories

* As a user, I want to be able to view my average overall review rating for all beers, so that I can understand overall customer sentiment
* As a user, I want to be able to see the top five highest rated beers by taste, so that our sales teams can use this data for sales forecasting
* As a user, I want to be able to view the five lowest rated beers by overall average review rating, alongside average taste rating so that I can see the influence taste has on overall review rating
 
**Optional:** What additional analysis do you think a drinks retailer could make using the dataset? Please provide a short summary paragraph to explain any additional analysis and why that analysis might be of value to a drinks retailer. 
 
### Level 2 Requirements/User Stories

* As a user, I want to see a visual comparison of 1 star reviews VS beer abv (%), so that I can see if there is a correlation between low review ratings and beer abv (%)
* As a user, I want to view a chart comparing Caldera Brewery Company with Amstel Brouwerij B. V. by average aroma rating, average appearance rating, and average taste rating
* As a user, I want to see a chart of the top five beer styles according to the number of 4 star + overall reviews they have received, so that I can see the correlation between beer style and high review ratings

**Optional:** We encourage you to come up with additional ways to visualise data analysis, so long as you present a valid theory on why this might be of value to a drinks retailer. Please provide a short summary paragraph to explain any additional visual analysis.

## :trophy: Reward

Your skills need recognition and that’s what we will be focusing on primarily in this coding challenge! The Ulster University Computing Society will mark and announce the overall winners. The winners will also receive a goodie bag from Bazaarvoice, recognition in all of Bazaarvoice's social media channels along with Amazon vouchers! :partying_face:

## :crystal_ball: Useful Resources

- [Python 3.9 - Docs](https://docs.python.org/3.9/)
- [Flask](https://flask.palletsprojects.com/en/1.1.x)
- [Jinja2](https://jinja.palletsprojects.com/en/2.11.x)
- [Bootstrap](https://getbootstrap.com/docs/4.5/getting-started/introduction)
- [Chart.js](https://www.chartjs.org)
