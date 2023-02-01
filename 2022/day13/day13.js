const fs = require('fs');

let file_path = String.raw`day13_input`;
let input_data = fs.readFileSync(file_path, 'utf8')
let answer1 = 0;
let pairs = [];
let array = input_data.split('\r\n\r\n');

for (let [index, subarray] of array.entries()) {
    // console.log(index, subarray)
    let pair1, pair2;
    [pair1, pair2] = subarray.split('\r\n');
    pair1 = eval(pair1);
    pair2 = eval(pair2);
    pairs.push(pair1);
    pairs.push(pair2);
    if (compare(pair1, pair2) === -1) {
        answer1 += index + 1;
    }
}
console.log(answer1)

let a = [[2]];
pairs.push(a); 
let b = [[6]];
pairs.push(b);

sorted_pairs = pairs.sort(compare);

answer2 = (sorted_pairs.indexOf(a) + 1) * (sorted_pairs.indexOf(b) + 1);
console.log(answer2);


function compare(value1, value2) {
    // console.log("COMPARING", value1, "VS", value2);
    if (typeof value1 === "number" && typeof value2 === "number") {
        if (value1 < value2) {
            return -1;
        } else if (value1 === value2) {
            return 0;
        } else {
            return 1;
        }
    } else if (Array.isArray(value1) && Array.isArray(value2)) {
        let i = 0;
        while (i < value1.length && i < value2.length) {
            let c = compare(value1[i], value2[i]);
            if (c === 1) {
                return 1;
            }
            if (c === -1) {
                return -1;
            }
            i++;
        }
        if (i === value1.length && i < value2.length) {
            return -1;
        } else if (i === value2.length && i < value1.length) {
            return 1;
        } else {
            return 0;
        }
    } else if (Array.isArray(value1) && typeof value2 === "number") {
        return compare(value1, [value2]);
    } else if (typeof value1 === "number" && Array.isArray(value2)) {
        return compare([value1], value2);
    }
}
