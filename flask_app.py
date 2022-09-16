from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def main_page():
    return render_template('split_check_main.html')


person_orders = []


def calc(check_tot,check_sub):
    strings = []
    person_sub_orders_list=[]
    for person in person_orders:
        person_order_list = person.split(',')
        name = person_order_list.pop(0)
        float_order_list = []
        for order in person_order_list:
            float_order_list.append(float(order))
        person_sub_orders_list.append(sum(float_order_list))
        person_total = (sum(float_order_list) / float(check_sub)) * float(check_tot)
        strings.append(f'{name} owes ${round(person_total, 2)}')
    person_orders.clear()
    string = "<h1 align='center'><a href='/'>SPLIT/CHECK</a></h1><h2 align='center' style='color:blue;'>Individual Totals</h2>"
    print(round(float(check_sub), 2), round(sum(person_sub_orders_list), 2))
    if (round(float(check_sub), 2) == round(sum(person_sub_orders_list), 2)) and float(check_tot) > float(check_sub):
        for person in strings:
            string = string + "<h1 align='center'>{}</h1>".format(person)
        return string
    else:
        return string+"<h1 align='center' style='color:red;'>* ENTRY ERROR. Go back to fix.*</h1>"


@app.route("/2", methods=['GET','POST'])
def page_2():
    if request.method == 'POST':
        check_tot = request.form['check-total2']
        check_sub = request.form['check-sub-total2']
        person_orders.extend((request.form['person21'],request.form['person22']))
        return calc(check_tot,check_sub)
    return render_template('split_check_2.html')

@app.route("/3", methods=['GET','POST'])
def page_3():
    if request.method == 'POST':
        check_tot = request.form['check-total3']
        check_sub = request.form['check-sub-total3']
        person_orders.extend((request.form['person31'], request.form['person32'],request.form['person33']))
        return calc(check_tot, check_sub)
    return render_template('split_check_3.html')

@app.route("/4", methods=['GET','POST'])
def page_4():
    if request.method == 'POST':
        check_tot = request.form['check-total4']
        check_sub = request.form['check-sub-total4']
        person_orders.extend((request.form['person41'], request.form['person42'],request.form['person43'],
                              request.form['person44']))
        return calc(check_tot, check_sub)
    return render_template('split_check_4.html')

@app.route("/5", methods=['GET','POST'])
def page_5():
    if request.method == 'POST':
        check_tot = request.form['check-total5']
        check_sub = request.form['check-sub-total5']
        person_orders.extend((request.form['person51'], request.form['person52'],request.form['person53'],
                              request.form['person54'],request.form['person55']))
        return calc(check_tot, check_sub)
    return render_template('split_check_5.html')

@app.route("/6", methods=['GET','POST'])
def page_6():
    if request.method == 'POST':
        check_tot = request.form['check-total6']
        check_sub = request.form['check-sub-total6']
        person_orders.extend((request.form['person61'], request.form['person62'],request.form['person63'],
                              request.form['person64'],request.form['person65'],request.form['person66']))
        return calc(check_tot, check_sub)
    return render_template('split_check_6.html')

@app.route("/7", methods=['GET','POST'])
def page_7():
    if request.method == 'POST':
        check_tot = request.form['check-total7']
        check_sub = request.form['check-sub-total7']
        person_orders.extend((request.form['person71'], request.form['person72'],request.form['person73'],
                              request.form['person74'],request.form['person75'],request.form['person76'],
                              request.form['person77']))
        return calc(check_tot, check_sub)
    return render_template('split_check_7.html')

@app.route("/8", methods=['GET','POST'])
def page_8():
    if request.method == 'POST':
        check_tot = request.form['check-total8']
        check_sub = request.form['check-sub-total8']
        person_orders.extend((request.form['person81'], request.form['person82'],request.form['person83'],
                              request.form['person84'],request.form['person85'],request.form['person86'],
                              request.form['person87'],request.form['person88']))
        return calc(check_tot, check_sub)
    return render_template('split_check_8.html')

@app.route("/info")
def info_page():
    return render_template('split_check_info.html')

if __name__ == "__main__":
    app.run(debug=True)
