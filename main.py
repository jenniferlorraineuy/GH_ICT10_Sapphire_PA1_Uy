def convert():
    f = float(int("fahrenheit").value)
    celsius = (f - 32) * 5 / 9

    display(float(celsius), target = "output")

    if celsius >= 37.8:
        display("Fever", target = "output")
    else:
        display("No fever", target = "output")