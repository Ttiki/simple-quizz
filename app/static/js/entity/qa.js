//Javascript Class with four attributes:
//1. question
//2. answer
//3. image
//4. choices
//4. userAnswer
class QA {

    constructor(question, answer, imgURI, choices, userAnswer) {
        this.question = question;
        this.answer = answer;
        this.imgURI = imgURI;
        this.choices = choices;
        this.userAnswer = userAnswer;
    }

    //getters & setters
    getQuestion() {
        return this.question;
    }

    setQuestion(question) {
        this.question = question;
    }

    getAnswer() {
        return this.answer;
    }
    setAnswer(answer) {
        this.answer = answer;
    }

    getAnswer2() {
        return this.answer2;
    }
    setAnswer2(answer2) {
        this.answer2 = answer2;
    }


    getImgURI() {
        return this.imgURI;
    }

    setImgURI(imgURI) {
        this.imgURI = imgURI;
    }

    getUserAnswer() {
        return this.userAnswer;
    }

    setUserAnswer(userAnswer) {
        this.userAnswer = userAnswer;
    }

    getChoices() {

        return this.choices;
    }

    setChoices(choices) {
        this.choices = choices;
    }


}