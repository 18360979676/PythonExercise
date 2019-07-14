//@time: 2019/7/14 15:44
//@author: yezhu
//@File: insert_sort.js
//@PROJECT_NAME: Python

function insertSort(arr) {
    for(var i = 1;i < arr.length; i++){
        var current = arr[i];
        var pre_index = i -1;
        while(pre_index >= 0 && arr[pre_index > current]){
            arr[pre_index + 1] = arr[pre_index];
            pre_index -= 1;
        }
        arr[pre_index + 1] = current;
    }
    return arr
}