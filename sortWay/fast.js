//@time: 2019/7/14 15:33
//@author: yezhu
//@File: fast.js
//@PROJECT_NAME: Pytho

function guessSort(arr) {
    if(arr.length < 2) return arr;
    var mid = arr[arr.length / 2];
    arr.splice(arr.length / 2, 1);
    var left = [], right = [];
    for(var i = 0; i < arr.length; item++){
        if(arr[i] >= mid)
            right.push(arr[i])
        else
            left.push(arr[i])
    }
    return guessSort(left) + [mid] + guessSort(right)
}