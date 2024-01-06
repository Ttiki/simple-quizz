var qas = JSON.parse(localStorage.getItem("qas"));

//foeach entry in the qas, create an object of QA
var qaList = [];
for (var i = 0; i < qas.length; i++) {
    var qa = new QA(qas[i].question, qas[i].answer, qas[i].imgURI, qas[i].choices, qas[i].userAnswer);
    qaList.push(qa);
}

appendToTable(qaList);