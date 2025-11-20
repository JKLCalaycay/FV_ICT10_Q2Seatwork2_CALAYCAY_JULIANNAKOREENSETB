from pyscript import document, display

def general_weighted_average (e):

    document.getElementById("student_info").innerHTML = ""
    document.getElementById("summary").innerHTML = ""
    document.getElementById("output").innerHTML = ""

    firstname = document.getElementById("first_name").value
    lastname = document.getElementById("last_name").value

    amountofdays = document.getElementById("daysnum").value
    daysabsent = document.getElementById("absentnum").value


    drill1 = float(document.getElementById('dr_1').value)
    drill2 = float(document.getElementById('dr_2').value)  
    seatwork1 = float(document.getElementById('sw_1').value)
    seatwork2 = float(document.getElementById('sw_2').value)
    skillstest = float(document.getElementById('sk_test').value)

    assesments = [drill1, drill2, seatwork1, seatwork2, skillstest]

    weights = (0.01, 0.01, 0.15, 0.15, 0.20)

    attendance_percentage = attendance_percentage = (daysabsent / (amountofdays + (amountofdays == ))) * (amountofdays != 0)

    weighted_assesment_score = (
        assesment[o] * rating_weights(0) +
        assesment[1] * rating_weights(1) +
        assesment[2] * rating_weights(2) +
        assesment[3] * rating_weights(3) +
        assesment[4] * rating_weights(4)
        
    )

    rating_weights = (0.1, 0.90)

    final_rating = attendance_percentage * rating_weights[0] + weighted_assessment_score * rating_weights[1]






