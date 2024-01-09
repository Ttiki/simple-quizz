//Dump all the data inside a table of object dezerialized from the json file
function openAnswer() {
    //Dezerialize the json data
    var jsonObj = JSON.parse('{{ questions_json|tojson|safe }}');
    //Create a table of qa objects
    var qas = [];
    for (var i = 0; i < jsonObj.length; i++) {
        //new qa object

        var qa = new QA(jsonObj[i].question, jsonObj[i].answer, jsonObj[i].imgURI, jsonObj[i].choices);
        qas.push(qa);
    }

    return qas.sort(() => Math.random() - 0.5);
    //return qas;

    // //Create a table to display the data
    // var table = document.createElement("table");
    // table.setAttribute("id", "table");
    // table.setAttribute("class", "table table-striped");
    // //Create a table header
    // var header = document.createElement("thead");
    // var row = document.createElement("tr");
    // var th = document.createElement("th");
    // th.innerHTML = "Question";
    // row.appendChild(th);
    // th = document.createElement("th");
    // th.innerHTML = "Answer";
    // row.appendChild(th);
    // th = document.createElement("th");
    // th.innerHTML = "Image";
    // row.appendChild(th);
    // th = document.createElement("th");
    // th.innerHTML = "User Answer";
    // row.appendChild(th);
    // header.appendChild(row);
    // table.appendChild(header);
    // //Create a table body
    // var body = document.createElement("tbody");
    // //Loop through the json object
    // for (var i = 0; i < jsonObj.length; i++) {
    //     //Create a table row
    //     var row = document.createElement("tr");
    //     //Create a table data
    //     var td = document.createElement("td");
    //     td.innerHTML = jsonObj[i].question;
    //     row.appendChild(td);
    //     td = document.createElement("td");
    //     td.innerHTML = jsonObj[i].answer;
    //     row.appendChild(td);
    //     td = document.createElement("td");
    //     td.innerHTML = jsonObj[i].imgURI;
    //     row.appendChild(td);
    //     td = document.createElement("td");
    //     td.innerHTML = jsonObj[i].userAnswer;
    //     row.appendChild(td);
    //     body.appendChild(row);
    // }
    // table.appendChild(body);
    // //Append the table to the div
    // var div = document.getElementById("answer");
    // div.appendChild(table);
}

//Function that call the openAnswer function 
//Create a new radio button for each question
//Display the question and the image
function populateQuiz(qas) {

    //get the length of qas
    var length = qas.length;

    //Append a new radio button to the q-select div
    for (var i = 0; i < length; i++) {
        //Create a new radio button
        var radio = document.createElement("input");
        radio.setAttribute("type", "radio");
        radio.setAttribute("name", "q-select");
        radio.setAttribute("value", "q" + i);
        radio.setAttribute("id", "q-" + i);
        radio.setAttribute("class", "q-select-radio");
        //Append the radio button to the q-select div
        document.getElementById("q-select").appendChild(radio);
    }

    addEventListenerToRadioButton();
    addEventListenerToNextButton();

    //Auto select the first radio button of the list
    document.getElementsByClassName("q-select-radio")[0].checked = true;
    //Set the question and the image
    var question = qas[0].question;
    var image = qas[0].getImgURI();
    //Display the question and the image
    document.getElementById("question").innerHTML = question;
    document.getElementById("image").src = "./res/Img/" + image;

    //Si nous avons une QCM
    if (qas[0].getChoices().length != 0) {
        console.log("QCM");
        document.getElementById("simple-input").setAttribute("class", "disable");
        document.getElementById("checkboxes").setAttribute("class", "");

        //We loop through all the choices and create a new checkbox for each of them
        var choices = qas[0].getChoices();
        //choices = shuffle(choices);
        var checkboxes = document.getElementById("checkboxList");
        checkboxes.innerHTML = "";
        for (var i = 0; i < choices.length; i++) {
            console.log(choices[i]);

            //Create a checkbox for each choice
            var checkbox = document.createElement("input");
            checkbox.setAttribute("type", "checkbox");
            checkbox.setAttribute("id", "choice" + i);
            checkbox.setAttribute("name", "choice");
            checkbox.setAttribute("value", choices[i]);
            checkboxes.appendChild(checkbox);
            checkboxes.appendChild(document.createTextNode(choices[i]));
            checkboxes.appendChild(document.createElement("br"));
        }

    } else { //Sinon, nous avons une "simple question"
        console.log("Simple question");
        document.getElementById("simple-input").setAttribute("class", "");
        document.getElementById("checkboxes").setAttribute("class", "disable");
    }
}

//Adding an evenlistener to change the question when the radio button is selected
function addEventListenerToRadioButton() {
    var radios = document.getElementsByClassName("q-select-radio");
    for (var i = 0; i < radios.length; i++) {
        radios[i].addEventListener("change", function() {

            //Get the value of the selected radio button
            var value = this.value;
            //Get the index of the selected radio button
            var index = value.substring(1);
            //Get the question and the image
            var question = qas[index].question;

            var image = qas[index].getImgURI();
            //Display the question and the image
            document.getElementById("question").innerHTML = question;
            document.getElementById("image").src = "./res/Img/" + image;

            //Si nous avons une QCM
            if (qas[index].getChoices().length != 0) {
                console.log("QCM");
                document.getElementById("simple-input").setAttribute("class", "disable");
                document.getElementById("checkboxes").setAttribute("class", "");

                //We loop through all the choices and create a new checkbox for each of them
                var choices = qas[index].getChoices();
                //choices = shuffle(choices);
                var checkboxes = document.getElementById("checkboxList");
                checkboxes.innerHTML = "";
                for (var i = 0; i < choices.length; i++) {
                    console.log(choices[i]);

                    //Create a checkbox for each choice
                    var checkbox = document.createElement("input");
                    checkbox.setAttribute("type", "checkbox");
                    checkbox.setAttribute("id", "choice" + i);
                    checkbox.setAttribute("name", "choice");
                    checkbox.setAttribute("value", choices[i]);
                    checkboxes.appendChild(checkbox);
                    checkboxes.appendChild(document.createTextNode(choices[i]));
                    checkboxes.appendChild(document.createElement("br"));
                }

            } else { //Sinon, nous avons une "simple question"
                console.log("Simple question");
                document.getElementById("simple-input").setAttribute("class", "");
                document.getElementById("checkboxes").setAttribute("class", "disable");
            }
        })
    }
}

//Adding an eventlistener on the button to set the qa's userAnswer to the text input value
//Then select the next radio button
//If there is no next radio button (i.e the last button is seleted), the next button should change the page to the result one
//The text of the button should channge from the arrow to "Finir"
function addEventListenerToNextButton() {
    document.querySelectorAll('.next').forEach(item => {
        item.addEventListener('click', function handleClick(event) {
            //Get the value of the selected radio button
            var value = document.querySelector('input[name="q-select"]:checked').value;
            //Get the index of the selected radio button
            var index = value.substring(1);

            //Get the text input value
            if (qas[index].getChoices().length != 0) {
                var userAnswer = "";
                var checkboxes = document.getElementsByName("choice");
                for (var i = 0; i < checkboxes.length; i++) {
                    if (checkboxes[i].checked) {
                        userAnswer = userAnswer + checkboxes[i].value + ", ";
                    }
                }
            } else {
                var userAnswer = document.getElementById("user-answer_input").value;
            }

            //Set the userAnswer of the selected qa
            qas[index].setUserAnswer(userAnswer);

            //If there is no next radio button (i.e the last button is seleted), the next button should change the page to the result one
            //The text of the button should channge from the arrow to "Finir"
            if (index == qas.length - 1) {

                // document.getElementById("next").innerHTML = "Finir";
                document.querySelectorAll('.next').forEach(item => {
                    item.addEventListener('click', function handleClick(event) {
                        localStorage.setItem("qas", JSON.stringify(qas));


                        //Change the page to the result one
                        window.location.href = "./results.html";
                    });
                });

            } else {
                //Select the next radio button
                document.getElementsByClassName("q-select-radio")[parseInt(index) + 1].checked = true;
                //Select the next obj in the table and change the image accordingly
                var question = qas[parseInt(index) + 1].getQuestion();
                var image = qas[parseInt(index) + 1].getImgURI();
                //Display the question and the image
                document.getElementById("question").innerHTML = question;
                document.getElementById("image").src = "./res/Img/" + image;

                document.getElementById("user-answer_input").value = "";

                //Si nous avons une QCM
                if (qas[parseInt(index) + 1].getChoices().length != 0) {
                    console.log("QCM");
                    document.getElementById("simple-input").setAttribute("class", "disable");
                    document.getElementById("checkboxes").setAttribute("class", "");

                    //We loop through all the choices and create a new checkbox for each of them
                    var choices = qas[parseInt(index) + 1].getChoices();
                    //choices = shuffle(choices);
                    var checkboxes = document.getElementById("checkboxList");
                    checkboxes.innerHTML = "";
                    for (var i = 0; i < choices.length; i++) {
                        console.log(choices[i]);

                        //Create a checkbox for each choice
                        var checkbox = document.createElement("input");
                        checkbox.setAttribute("type", "checkbox");
                        checkbox.setAttribute("id", "choice" + i);
                        checkbox.setAttribute("name", "choice");
                        checkbox.setAttribute("value", choices[i]);
                        checkboxes.appendChild(checkbox);
                        checkboxes.appendChild(document.createTextNode(choices[i]));
                        checkboxes.appendChild(document.createElement("br"));
                    }

                } else { //Sinon, nous avons une "simple question"
                    console.log("Simple question");
                    document.getElementById("simple-input").setAttribute("class", "");
                    document.getElementById("checkboxes").setAttribute("class", "disable");
                }
            }
        });
    });
}


//Append every object of the table to the table table-results-body in the results.html page
function appendToTable(qas) {

    var noteDisplay = document.getElementById("note-display");
    var noteTitle = document.createElement("h1");

    noteDisplay.appendChild(noteTitle);
    noteDisplay.appendChild(document.createElement("hr"));


    //Get the table body
    var tableBody = document.getElementById("table-results-body");
    var note = 0;
    //Get the length of qas
    var length = qas.length;

    //Append a new row to the table body
    for (var i = 0; i < length; i++) {
        var row = document.createElement("tr");
        //Append a new cell to the row
        var cell = document.createElement("td");

        //Get the answer and the user answer for the current qa
        var answer = qas[i].getAnswer();
        var answer2;
        if (qas[i].getAnswer2() != undefined) {
            answer2 = qas[i].getAnswer2();
        }
        var userAnswer = qas[i].getUserAnswer();

        var chckmrk = document.createElement("input");
        chckmrk.setAttribute("type", "checkbox");



        //if the answer = userAnswer, the cell should be green and have a checkmark icon
        //else the cell should be red and have a cross icon
        if (answer2 != undefined) {
            if (userAnswer != undefined) {


                if (answer.replace(/\s+/g, '') == userAnswer.replace(/\s+/g, '')) {
                    row.setAttribute("class", "row-green");
                    chckmrk.checked = true;
                    note++;
                } else {
                    row.setAttribute("class", "row-red");
                    chckmrk.checked = false;
                }
            } else {
                row.setAttribute("class", "row-red");
                chckmrk.checked = false;
            }
        } else {
            if (userAnswer != undefined) {
                if (answer.replace(/\s+/g, '') == userAnswer.replace(/\s+/g, '')) {
                    row.setAttribute("class", "row-green");
                    chckmrk.checked = true;
                    note++;
                } else {
                    row.setAttribute("class", "row-red");
                    chckmrk.checked = false;
                }
            } else {
                row.setAttribute("class", "row-red");
                chckmrk.checked = false;
            }

        }

        chckmrk.addEventListener('change', function() {
            if (this.checked) {
                console.log("Checkbox is checked..");
                note++;
                testNote(noteTitle, note, length);
            } else {
                console.log("Checkbox is not checked..");
                note--;
                testNote(noteTitle, note, length);
            }
        });

        cell.appendChild(chckmrk);
        row.appendChild(cell);
        // cell = document.createElement("td");
        // //Set the text of the cell
        // var img = document.createElement("img");
        // img.src = "./res/Img/" + qas[i].getImgURI();
        // img.setAttribute("id", "image");
        // cell.appendChild(img);

        // row.appendChild(cell);
        cell = document.createElement("td");
        //Set the text of the cell

        cell.innerHTML = qas[i].question;

        //cell.appendChild(img);

        //cell.setAttribute("style", "background-image: URL('"./res/Img/" + qas[i].getImgURI() + "'); background-position: center; background-size: contain; background-repeat: no-repeat;");
        //cell.setAttribute("style", "background-po")
        //Append the cell to the row
        row.appendChild(cell);

        //Append a new cell to the row
        cell = document.createElement("td");

        var image = qas[i].getImgURI();

        var imgTag = document.createElement("img");
        imgTag.setAttribute("src", "./res/Img/" + image);
        cell.append(imgTag);
        row.append(cell);

        //Append a new cell to the row
        cell = document.createElement("td");
        //Set the text of the cell
        var answer = qas[i].getAnswer();
        var answer2 = qas[i].getAnswer2();
        if (answer2 != undefined) {
            cell.innerHTML = answer + " ou " + answer2;
        } else {
            cell.innerHTML = answer;
        }
        //Append the cell to the row
        row.appendChild(cell);
        //Append a new cell to the row
        cell = document.createElement("td");
        //Set the text of the cell
        cell.innerHTML = qas[i].getUserAnswer();
        //Append the cell to the row
        row.appendChild(cell);



        //Append the row to the table body
        tableBody.appendChild(row);
    }


    testNote(noteTitle, note, length);
}

function testNote(noteTitle, note, length) {
    noteTitle.innerHTML = note + "/" + length + " bonnes réponses (" + (note / length * 100).toFixed(2) + "%)";
    //Change the title attribute of the noteTitle div
    //Change the color of the title depending on the note
    if (note / length >= 0.8) {
        noteTitle.setAttribute("class", "title-green");
    } else if (note / length >= 0.5) {
        noteTitle.setAttribute("class", "title-orange");
    } else {
        noteTitle.setAttribute("class", "title-red");
    }


}

function shuffle(array) {
    let currentIndex = array.length,
        randomIndex;

    // While there remain elements to shuffle.
    while (currentIndex != 0) {

        // Pick a remaining element.
        randomIndex = Math.floor(Math.random() * currentIndex);
        currentIndex--;

        // And swap it with the current element.
        [array[currentIndex], array[randomIndex]] = [
            array[randomIndex], array[currentIndex]
        ];
    }

    return array;
}