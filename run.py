from station import Station

def run():
    first_station = "武蔵境"
    second_station = "三鷹"
    third_station = "吉祥寺"

    s = Station(first_station)
    s1 = Station(second_station)
    s2 = Station(third_station)

    print("Hello, there. The train station to start is", s.get_station())
    print("Next, we proceed to", s1.get_station())
    print("Finally, we rest at", s2.get_station())

if __name__ == "__main__":
    run()
