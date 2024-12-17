# 🏠 **Web Scraping Real Estate Listings in the UAE** 🇦🇪

Welcome to the **Web Scraping Real Estate Listings** project! This project was designed to teach the basics of **Web Scraping** and how to use the **Pandas** library for data manipulation in Python. The goal is to extract information from a real estate listings website named Property Finder in the United Arab Emirates, generate a CSV file with the data, and start exploring it with Pandas.

## 🎯 **Project Goal**

The main goal of this project is to provide a hands-on introduction to **Web Scraping** and **Pandas**. By going through this tutorial, you will learn how to:

- **Extract data** from a website using Python.
- **Manipulate** the extracted data using the **Pandas** library.
- **Save the data** in a CSV file.
- **Analyze** the extracted data for basic insights.

This project is perfect for anyone who wants to understand how to gather and work with web data, and get familiar with one of the most powerful libraries for data analysis: **Pandas**.

## 📖 **A Little Story Behind the Project**

So here’s the story: I was looking for a website to do a nice web scraping project for a class I was about to teach, something that would cover some cool techniques. I wanted to find something that would be challenging yet doable. By pure chance, while browsing through **StackOverflow** (as one does when procrastinating), I stumbled upon a piece of code (that had a problem with a request) with this URL. I thought to myself, “Hmm, let’s investigate this!” And well, what do you know, I found it intriguing enough to turn it into a full-blown project! 😅

The website turned out to be a real estate listings page for properties in the UAE. Challenge accepted, and here we are, scraping away!

## 🛠️ **Technologies Used**

This project uses the following technologies:

- **Python**: The main programming language used.
- **BeautifulSoup**: A library for parsing HTML and extracting data from web pages.
- **Requests**: A library for making HTTP requests.
- **Pandas**: A library for data manipulation and analysis.
- **PyYAML**: Used to load configuration variables from the `vars.yaml` file.

### 📝 **Installing Dependencies**

To run the project, you’ll need **Python 3.x** installed. Then, install the required dependencies via the `requirements.txt` file:

```bash
pip install -r requirements.txt
```

### 🔧 **Project Structure**

Here’s the structure of the project:

```
webscraping-property/
├── src/
│   ├── config.py          # Project configuration and variables
│   ├── scrapper.py        # Code responsible for web scraping
│   ├── vars.yaml          # Configuration file with variables like URL, CSS classes
│   ├── data/              # Folder where extracted data will be saved
├── main.py                # Main file that runs the scraping and generates the CSV
├── requirements.txt       # Project dependencies
└── README.md              # Project documentation (you’re reading it!)
```

## ⚙️ **How to Run the Project**

To execute the project and perform the scraping, follow these steps:

1. **Clone the Repository**:

```bash
git clone https://github.com/your_username/webscraping-property.git
cd webscraping-property
```

2. **Install Dependencies**:

```bash
pip install -r requirements.txt
```

3. **Run the Code**:

```bash
python main.py
```

When you run the code, it will:

- Access the real estate listings website in the UAE.
- Extract details about **property type**, **price**, **location**, **number of rooms**, **number of bathrooms**, and **area**.
- Save the extracted data into a CSV file in the `data/` directory.

## 🗂️ **Extracted Data Format**

The data extracted from each property listing will include the following information:

- **Details**: The title or a brief description of the property.
- **Price**: The price of the property.
- **Location**: The location of the property.
- **Number of Rooms**: How many rooms the property has.
- **Number of Bathrooms**: How many bathrooms the property has.
- **Area**: The total area of the property.
- **Link**: The URL to the full listing.
- **Contact**: The link for contacting the seller/agent.

Here’s an example of how the data will look in the CSV file:

| Details               | Price     | Location     | Rooms | Bathrooms | Area   | Link | Contact |
|-----------------------|-----------|--------------|-------|-----------|--------|------|---------|
| "2 Bedroom Apartment" | 50,000 AED| Dubai Marina | 2     | 2         | 120 m² | [link](#) | [contact](#) |
| "3 Bedroom House"     | 80,000 AED| Abu Dhabi    | 3     | 3         | 200 m² | [link](#) | [contact](#) |

### 💡 **Why the Data Isn't Treated**

Now, you may notice that the data we extracted isn’t pre-processed or cleaned. This was intentional! I purposely left the data untouched to make it part of the **Pandas** class I was teaching. The idea is to work through cleaning, transforming, and analyzing the data **dynamically with the students** during the class, which is more engaging and hands-on. So, feel free to experiment with the raw data and apply your **data wrangling** skills as you learn! 🧹✨

## 📊 **Analyzing with Pandas**

With the generated CSV file, you can start exploring and analyzing the data using **Pandas**. Here are some basic operations you can try:

- **Load the data**:

```python
import pandas as pd

df = pd.read_csv('data/data.csv')
```

- **Display the first few rows**:

```python
print(df.head())
```

- **Get basic statistics**:

```python
print(df.describe())
```

- **Filter properties with a price above 70,000 AED**:

```python
high_price_properties = df[df['Price'] > 70000]
print(high_price_properties)
```

These are just the basics! **Pandas** allows you to perform advanced data analysis and manipulation with just a few lines of code.

## 🤖 **Future Plans for the Project**

As part of the next steps, I’m planning to build a **complete ETL pipeline** that will:

1. **Extract**: Gather data through scraping, just as we’ve done so far.
2. **Transform**: Clean and process the data (including handling missing values, converting data types, and aggregating data).
3. **Load**: Insert the transformed data into a **database** (such as MySQL or PostgreSQL) for further analysis and better data management.

Additionally, I want to **automate data visualization** by creating a **web dashboard** or **site** that updates in real-time, showing insights from the data. This could include trends in property prices, location comparisons, and more.

I also plan to explore some **data modeling**, such as predicting property prices based on various features (rooms, area, location, etc.) using machine learning techniques.

## 🤝 **Contributions**

If you have suggestions or improvements for the project, feel free to open an **issue** or a **pull request**! Let’s make this project even better!

## 📧 **Contact**

If you have any questions about the project or need help, feel free to reach out:

- **Email**: [pedrohmvieira04@gmail.com](pedrohmvieira04@gmail.com)
