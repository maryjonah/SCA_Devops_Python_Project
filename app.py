from flask import Flask, render_template

app = Flask(__name__)

# File to store the count
count_file = "visit_count.txt"

def get_count():
  try:
    with open(count_file, "r") as f:
      return int(f.read())
  except FileNotFoundError:
    return 0

def update_count(count):
  with open(count_file, "w") as f:
    f.write(str(count))

@app.route("/")
def home():
  count = get_count()
  count += 1
  update_count(count)
  return render_template("index.html", count=count)

if __name__ == "__main__":
  app.run(debug=True)