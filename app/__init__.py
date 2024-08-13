from flask import Flask, render_template, request
import random


app = Flask(__name__, static_url_path='/static/css')

doors: list[int] = [1, 2, 3]

@app.route('/', methods=["GET", "POST"])

def monty_hall():
    if request.method == "POST":
        try:
            trials = int(request.form.get("trials"))
        except:
            return render_template("index.html", 
                                   error="Number of trials should be an integer")

        if trials <= 0 or trials > 1000000:
            return render_template("index.html", 
                                   error="Number of trials should be in between 1 - 1,000,000!")

        switch_wins: int = 0
        stay_wins: int = 0

        for _ in range(trials):
            car: int = random.choice(doors)
            choice: int = random.choice(doors)

            if car == choice:
                stay_wins += 1
            else:
                switch_wins += 1
        
            switch_win_rate: int = round(switch_wins / trials * 100, 2)
            stay_win_rate: int = round(stay_wins / trials * 100, 2)

        return render_template("index.html", 
                               switch_wins=switch_wins, 
                               stay_wins=stay_wins, 
                               trials=trials, 
                               switch_win_rate=switch_win_rate, 
                               stay_win_rate=stay_win_rate)

    return render_template("index.html")