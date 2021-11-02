
#### Problem of the statement
While entertainment is a centre of human happiness, it is also a global business enterprise in which film companies focus on success and popularity of movie releases to its audience. Movie ratings is a key metric for evaluating success of different movie genres. Besides, movie recommendations systems help audience make relevant choice of movies from the similar movies they have had interest in. Rating metric is one of the useful value a movie user base on to decide whether to watch a movie or not. The objective of the project was to develop a machine learning model to forecast the ratings of a movie based on its genre, title and tag information.


#### Dataset

The [movielens](http://grouplens.org/datasets/) is a public dataset consisting . The development dataset of movielens data was used. It consisted of 100,000 ratings with 3,600 tags for 9,000 movies from randomly selected 600 movie users with experience of rating at least 20 movies. The data covers the period between March 29, 1996 and September 24, 2018. The dataset was generated on September 26, 2018. It does not contain demographic information information about the users.

The used include were obtained from the following 3 files:
- _movies.csv_: movie information for each movie id. The _title_ contains the year release in parenthesis. The genre is one of the following: _Action, Adventure, Animation, Children\'s, Comedy, Crime, Documentary, Drama, Fantasy, Film-Noir, Horror, Musical, Mystery, Romance, Sci-Fi, Thriller, War, Western, (no genres listed)_
- _ratings.csv_: users ratings for the movies and the timestamp it was rated. The rating is in the range 0.5 stars - 5.0 stars. The time stamp is the seconds from midnight Coordinated Universal Time (UTC) of January 1, 1970.
- _tags.csv_: A tag (a single word or short phrase) applied to a movie by a user. The time stamp is the seconds from midnight Coordinated Universal Time (UTC) of January 1, 1970.


#### How to run the application
Clone the directory into you work space.
Install, build and run the application using the commands: 

```
docker build -t movieAnalysis .

docker run -it --rm -p 9696:9696 movieAnalysis

```

