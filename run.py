from station import Station
from flask import Flask, url_for

app = Flask(__name__)

@app.route("/")
def index():
    return "Index"

@app.route("/login")
def login():
    return "generic login form"

@app.route("/user/<username>")
def profile(username):
    return f"{username}'s profile"

@app.route("/test")
def test_contexts():
    with app.test_request_context():
        print(url_for("index"))
        print(url_for("login"))
        print(url_for("login", next="/"))
        print(url_for("profile", username="Jon©"))
    return "Sent all debugging information to Terminal"

def collect_stations():
    """ Create a simple chain of train stations """
    first_station = "武蔵境"
    second_station = "三鷹"
    third_station = "吉祥寺"

    # Creating a set of stations
    s = Station(first_station,
                "2 Chome-1-12 Kyonancho, Musashino-shi, 〒180-0023, Japan")
    s1 = Station(second_station,
                "3 Chome-46 Shimorenjaku, Mitaka-shi, 〒181-0013, Japan")
    s2 = Station(third_station,
              "2 Chome−1 Musashino-shi, Kichijōji Minamichō, 〒180-0003, Japan")

    print("Hello, there. The train station to start is", s.get_name())
    print("Next, we proceed to", s1.get_name())
    print("Finally, we rest at", s2.get_name())
