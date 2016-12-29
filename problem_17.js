var words_1_19 = ["", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"];
var words_20_90 = ["", "ten", "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"];

function numberToWords(n) {
    if (n <= 19)
        return words_1_19[n];
    else if (n == 1000)
        return "onethousand";

    var str = n.toString();
    var words = "";

    if (str.length == 3) {
        words += words_1_19[parseInt(str[0])] + "hundred";
        if (str[1] != "0" || str[2] != "0")
            words += "and";
    }

    if (str.length >= 2) {
        if (parseInt(str[str.length - 2]) >= 2) {
            words += words_20_90[parseInt(str[str.length - 2])];
            words += words_1_19[parseInt(str[str.length - 1])];
        } else {
            words += words_1_19[parseInt(str[str.length - 2] + str[str.length - 1])];
        }
    }

    return words;
}

var sum = 0;
for (var i = 1; i <= 1000; i++)
    sum += numberToWords(i).length;

console.log(sum);
