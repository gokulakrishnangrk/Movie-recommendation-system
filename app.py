import pandas as pd
import os

# =====================================
# MOVIE RECOMMENDATION SYSTEM
# =====================================

print("=" * 50)
print("       MOVIE RECOMMENDATION SYSTEM")
print("=" * 50)

# Get User Name
name = input("\nEnter Your Name: ").strip()

if name == "":
    name = "User"

print("\nHello", name + "!")
print("Welcome to Movie Recommendation System!")

print("\nLet's find the best movies for you.")

# =====================================
# LOAD MOVIE DATASET
# =====================================

try:

    movies = pd.read_csv("dataset/movies.csv")

    print("\nMovie Dataset Loaded Successfully!")

    print("\nMOVIE DETAILS")
    print("-" * 50)

    print(movies.head())

    print("\nTotal Movies:", len(movies))

except FileNotFoundError:

    print("\nError: movies.csv not found!")

    exit()

except Exception as e:

    print("\nMovie Dataset Error:", e)

    exit()


# =====================================
# LOAD RATINGS DATASET
# =====================================

try:

    ratings = pd.read_csv("dataset/ratings.csv")

    print("\nRatings Dataset Loaded Successfully!")

    print("\nRATINGS DETAILS")
    print("-" * 50)

    print(ratings.head())

    print("\nTotal Ratings:", len(ratings))

except FileNotFoundError:

    print("\nError: ratings.csv not found!")

    exit()

except Exception as e:

    print("\nRatings Dataset Error:", e)

    exit()


# =====================================
# DATASET INFORMATION
# =====================================

print("\nDATASET INFORMATION")
print("-" * 50)

print("Movie Columns:", movies.columns.tolist())

print("Ratings Columns:", ratings.columns.tolist())

# =====================================
# USER INFORMATION
# =====================================

print("\nUSER INFORMATION")
print("-" * 50)

if "userId" in ratings.columns:

    print("Total Users:", ratings["userId"].nunique())

else:

    print("User ID column is not available in ratings dataset.")

# =====================================
# MOVIE INFORMATION
# =====================================

print("\nMOVIE INFORMATION")
print("-" * 50)

if "movieId" in movies.columns:

    print("Total Movie IDs:", movies["movieId"].nunique())

else:

    print("Movie ID column is missing.")

# =====================================
# FINAL MESSAGE
# =====================================

print("\n" + "=" * 50)

print("MOVIE RECOMMENDATION SYSTEM READY!")

print("=" * 50)

print("\nThank you", name + "!")

print("Enjoy Your Movie Recommendation System!")