# Movie Recommendation System App

![App Screenshot](images/screenshot_app.jpg")


This is a movie recommendation system app that suggests the most compatible movies based on the input movie title, 
genre, and optionally, actor's name. The app uses content-based filtering techniques to generate personalized movie 
recommendations for users.

## Features
- Easy-to-use web interface to enter movie details and get recommendations.
- Content-based filtering: Recommend movies similar to the input movie based on genre and, optionally, actor.
- Fast and efficient recommendation engine.
- Responsive design for desktop and mobile devices.

## Files
- `api`: directory with `omdb.py` and `tmdb.py` files for API requests
- `assets`: directory with `distance.csv` and `movies.csv` files containing data
- `images`: directory with images for this project
- `recsys`:  directory with main classes for scripts
- `app.py`: script for application using Streamlit
- `requirements.txt`: package requirements files

## Additional requirements

For deploying this the additional `.env` file is needed.
```
DISTANCE = 'assets/distance.csv'
MOVIES = 'assets/movies.csv'
API_KEY = 'YOUR_API_KEY_FOR_OMDB'
API_KEY_TMDB = 'YOUR_API_KEY_FOR_TMDB'
```
Please make sure to replace `YOUR_API_KEY_FOR_OMDB` and `YOUR_API_KEY_FOR_TMDB` with your actual API keys. 
Let me know if you need any further changes or assistance!


## Run App Locally

To run Streamlit locally, follow these steps in the root folder of the repository:
```
$ python -m venv venv 
$ source venv/bin/activate 
$ pip install -r requirements.txt
$ streamlit run app.py`
```
Open http://localhost:8501 to view the app.

## Contact me
If you have any questions or suggestions, do not hesitate to contact me at:

Email: dikarpova04@icloud.com 

GitHub: https://github.com/dikarpova04


