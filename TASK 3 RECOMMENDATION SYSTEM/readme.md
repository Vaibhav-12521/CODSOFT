# Content-Based Movie Recommendation System 🎬

This project is a simple content-based movie recommendation system built in Python. It uses `scikit-learn` and `pandas` to suggest movies that are similar to a user's favorite movie. The recommendation is based on the movie's genre and overview.

## ✨ Features

* Recommends movies based on content similarity.
* Simple and interactive command-line interface.
* Uses a bag-of-words model (`CountVectorizer`) and **Cosine Similarity** to find the best matches.

## How It Works

The system works by creating a "tag" for each movie, which is a combination of its genre and overview. It then converts these text tags into numerical vectors. By calculating the cosine similarity between these vectors, the system can find and rank the movies that are most similar in content to the one you entered.

## 🚀 Usage & Instructions

To get movie recommendations, run the script from your terminal.

1.  The script will prompt you with:
    ```
    Enter Your fevourite Movie Name:
    ```

2.  Type the name of a movie you like and press **Enter**.
    * **Important:** Make sure to spell the movie title correctly and use proper capitalization (e.g., `Avatar`, `The Dark Knight`, `Forrest Gump`).

3.  The system will analyze your input and print a list of the top 5 recommended movies for you.
    ```
    I'll recommanded You:

    Movie Title 1
    Movie Title 2
    Movie Title 3
    Movie Title 4
    Movie Title 5
    ```

4.  The script runs in a continuous loop, so you can keep entering movie names to get new recommendations. To stop the script, press **`Ctrl + C`** in your terminal.

## 📋 Required Data

* This script requires a CSV file named **`dataset.csv`** to be present in the same directory as the Python script.
* The `dataset.csv` file must contain at least the following columns for the script to work correctly:
    * `id`
    * `title`
    * `genre`
    * `overview`
