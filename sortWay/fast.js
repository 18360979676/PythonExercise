//@time: 2019/7/14 15:33
//@author: yezhu
//@File: fast.js
//@PROJECT_NAME: Pytho

function guessSort(arr) {
    if(arr.length < 2) return arr;
    var mid = arr[arr.length / 2];
    arr.splice(arr.length / 2, 1);
    var left = [], right = [];
    for(var item = 0; item < arr.length; item++){
        if(arr[item] >= mid)
            right.push(arr[item])
        else
            left.push(arr[item])
    }
    return guessSort(left) + [mid] + guessSort(right)
}