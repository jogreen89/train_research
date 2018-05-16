from station import Station
from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello, World!"

def run():
    first_station = "武蔵境"
    second_station = "三鷹"
    third_station = "吉祥寺"

    s = Station(first_station, "2 Chome-1-12 Kyonancho, Musashino-shi, 〒180-0023, Japan")
    s1 = Station(second_station, "3 Chome-46 Shimorenjaku, Mitaka-shi, 〒181-0013, Japan")
    s2 = Station(third_station, "Japan, 〒180-0003, Musashino-shi, Kichijōji Minamichō, 2 Chome−1, 吉祥寺南町1丁目")

    print("Hello, there. The train station to start is", s.get_name())
    print("Next, we proceed to", s1.get_name())
    print("Finally, we rest at", s2.get_name())

if __name__ == "__main__":
    run()
