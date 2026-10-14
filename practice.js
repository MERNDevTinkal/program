// const name = "Tinkal kumar";
// const howmany = name.length;

// console.log(howmany);

// const name = "Tinkal kumar";
// const firstlater = name[0]
// console.log(firstlater)

// indexOf()
// Finds the position of a character or substring.If something doesn't exist: -1

// const name = "Tinkal"
// const indofl = name.indexOf("n")
// console.log(indofl)

// includes()
// Checks whether something exists inside a string.
// It returns true or false.One important interview point
// JavaScript strings are case-sensitive:
// "Tinkal".includes("tinkal"); // false

// const name= "tinkalkumar"
// const isTinkal = name.includes("tinkal")
// const isz = name.includes("XDF")
// console.log(isTinkal,isz)

// const name = "tttttttinkalscript"
// const pos = name.indexOf("script")
// console.log(pos)

// split() do?
// It converts a string into an array based on a separator. (" ") or ("")Split by comma (",")

// reverse JavaScript

// let name = "Tinkal"
// let arr = name.split("")
// let left= 0
// let right = arr.length-1

// while (left < right){
//     [arr[left],arr[right]]=[arr[right],arr[left]]
//     left+=1
//     right-=1
// }
// name=arr.join("")
// console.log(name)

// const arr = ["Tinkal", "Kumar"];
// const result = arr.join(" ");
// console.log(result);

// slice()
// slice() is used to take a portion of a string or array without changing the original.
// slice(start, end)
// start is included, end is excluded.If you don't provide end, it takes everything until the end.

// const name = "Tinkal Kumar";
// console.log(name.slice(0, 6));

// splice() → changes original array - splice() is mainly used with arrays to add, remove, or replace elements.

// const arr = [10, 20, 30, 40, 50];
// arr.splice(1,3)
// console.log(arr)

// const arr = [2,3,4,3,4,3,2]
// arr.splice(3,0,43)
// console.log(arr)

// 0 means:
// Don't delete anything.

// arr.splice(1, 1, 200); 1 means replace

// The callback can receive 3 arguments:
// array.map((value, index, array) => {

// });

// map() returns a new array.

// const arr = [10, 20, 30];
// for (i=0;i<arr.length;i++){
//     console.log(i,arr[i])
// }

// const arr = [10, 20, 30];
// arr.map((v,i,a) =>{
//     console.log(i,v)
// })

// filter() goes through an array and keeps only the elements for which the condition is true
// filter() returns a new array

// const users = [
//     { name: "Tinkal", age: 25 },
//     { name: "Rahul", age: 18 },
//     { name: "Amit", age: 30 }
// ];

// const res = users.filter(u => u.age === 25)
// console.log(res)

// reduce() takes many array values and combines them into one final value.
// Most commonly: array → one number

// arr.reduce((accumulator, currentValue) => {
//     return something;
// }, initialValue);

// accumulator     → result collected so far
// currentValue   → current array element
// initialValue   → starting value

// const arr = [10, 20, 30];

// const total = arr.reduce((sum, value) => {
//     return sum + value;
// }, 0);

// some() checks whether at least one element in an array satisfies a condition.
// It returns only: 0 or 1

// array.some((value, index, array) => {
//     return condition;
// });

// const arr = [10, 20, 30, 40];

// const result = arr.some((value) => {
//     return value > 25;
// });

// console.log(result);

// const users = [
//     { name: "Tinkal", age: 25 },
//     { name: "Rahul", age: 17 },
//     { name: "Amit", age: 30 }
// ];

// const hasMinor = users.some(user => user.age < 18);

// console.log(hasMinor);

// every() is the opposite idea.
// It checks whether all elements satisfy the condition.

// const arr = [10, 20, 30, 40];

// const res= arr.every((v,i,a)=>{
//     return v>9
// })
// console.log(res)

// JavaScript sorts numbers as strings by default.changes the original array

// const arr = [10, 5, 20, 2];

// arr.sort((a, b) => {
//     return a - b;
// });
// console.log(arr);

// const arr = [10, 5, 20, 2];

// arr.sort((a, b) => {
//     return b - a;
// });
// console.log(arr);


// Optimized Bubble Sort
//  array=[32,4,2,2,1,2,3,0,7,5,70,5,0,1]
// # for i in range(len(array)):
// #     for j in range(len(array)-i-1):
// #         if array[j]>array[j+1]:
// #             array[j],array[j+1]=array[j+1],array[j]
// # print(array)

// const arr = [10, 5, 20, 2];

// for (i = 0; i < arr.length - 1; i++) {
//     for (j = 0; j < arr.length - i - 1; j++) {
//         if (arr[j] > arr[j + 1]) { // > for assending and < for desanding
//             [arr[j], arr[j + 1]] = [arr[j + 1], arr[j]]
//         }
//     }
// }

// console.log(arr)

// reverse a  array
// let arr = [2,4,5,6,79,0,5,2,22]
// let left=0
// let right= arr.length-1

// while(left < right){
//     [arr[left],arr[right]]=[arr[right],arr[left]]
//     left+=1
//     right-=1
// }

// console.log(arr)


// array.forEach((value, index, array) => {

// });
// It executes a function once for every element in an array. it doesnt create a new array

// Remove duplicates
// Set is a JavaScript object used to store unique values.A Set cannot contain duplicate values.

// let arr = [1, 2, 2, 3, 4, 4, 5, 5]
// // Step 1: Convert Array → Set

// let newArray = new Set(arr)
// console.log(newArray)

// // Step 2: Convert Set → Array
// newArray=[...newArray]
// console.log(newArray)

// Those ... are called the spread operator in JavaScript.the ... means take all values from the them and spread them into a new array.


// keys    → what are the property names?
// values  → what are the property values?
// entries → give me both
// Object.keys(), Object.values(), Object.entries()

// const user = {
//     name: "Tinkal",
//     age: 25,
//     city: "Jaipur"
// };

// const res = Object.keys(user)
// const val = Object.values(user)
// // console.log(res) // [ 'name', 'age', 'city' ]
// // console.log(val) // [ 'Tinkal', 25, 'Jaipur' ]
// const allkv = Object.entries(user)
// console.log(allkv) // . Object → Array
// [ [ 'name', 'Tinkal' ], [ 'age', 25 ], [ 'city', 'Jaipur' ] ]

// push(), pop(), shift(), unshift() All four modify the original array.

// const arr = [10, 20, 30];

// arr.push(40);

// console.log(arr); //You can add multiple values: arr.push(50, 60);

// pop()
// Removes the last element.
// const arr = [10, 20, 30];

// const result = arr.pop();

// console.log(arr);
// console.log(result);//[10, 20] this is new length 30

// unshift()
// Adds one or more elements to the beginning. arr.unshift(-10, 0);unshift() returns the new array length.

// shift()
// Removes the first element.array.shift()shift() returns the removed element.


// merge two array sorted 

// const arr1 = [0,5,6,8,9,12,32];
// const arr2 = [40, 50, 60];

// const result = []
// let i = 0
// let j = 0

// while (i < arr1.length && j < arr2.length) {
//     if (arr1[i] < arr2[j]) {
//         result.push(arr1[i])
//         i += 1
//     } else {
//         result.push(arr2[j])
//         j += 1
//     }
// }

// while (i < arr1.length) {
//     result.push(arr1[i])
//     i += 1
// }

// while (j < arr2.length) {
//     result.push(arr2[j])
//     j += 1
// }

// console.log(result)



/// merge unsorted aray


// arr1 = [2, 4, 23, 2, 0, 1]
// arr2 = [0, 23, 5, 7, 3, 56]

// let sortedarr = [...arr1,...arr2]
// console.log(sortedarr)

// for (i = 0; i < sortedarr.length; i++) {
//     for (j = 0; j < sortedarr.length - i - 1; j++) {
//         if (sortedarr[j] > sortedarr[j + 1]) {
//             [sortedarr[j], sortedarr[j + 1]] = [sortedarr[j + 1], sortedarr[j]]
//         }
//     }
// }
// console.log(sortedarr)

// // Check Palindrome

// const str = "madam";
// left=0
// right=str.length-1
// let isPalindrom=true
// for(i=0;i<str.length;i++){
//     if(str[left] !== str[right]){
//         isPalindrom=false
//         break
//     }
//     left+=1
//     right-=1
// }
// console.log(isPalindrom)

// Count Vowels

// let s="Tinkal kumar"
// let count =0
// for(i=0;i< s.length;i++){
//     if("aeiou".includes(s[i].toLocaleLowerCase())){
//         count+=1
//     }
// }
// console.log(count)

// Count Character Frequency and max frequency

// const str = "fswqjlksxvcfdlk56j";
//  const str = [3, 4, 5, 6, 7, 4, 4, 5, 6, 7, 8, 9, 0, 1, 2, 3];
//  feq={}
//  for(i=0;i<str.length;i++){
//     if(feq[str[i]]){
//         feq[str[i]]++
//     }else{
//         feq[str[i]]=1
//     }
//  }
//  console.log(feq)
//  let maxcount=0
//  let maxrepeating

//  for(let value in feq){
//     if(feq[value]>maxcount){
//         maxcount=feq[value]
//         maxrepeating=value
//     }
//  }

//  console.log(maxcount,maxrepeating)

// remove duplicates in-place without using Set
// const arr = [1, 2, 2, 3, 4, 4, 5, 5];
// let arr="sljkJLKLJKlkj"
// arr=arr.split("")
// for(i=0;i<arr.length;i++){
//     for(j=i+1;j<arr.length;j++){
//         if(arr[i] === arr[j]){
//             arr.splice(j,1)
//             j--
//         }
//     }
// }
// console.log(arr)

// Find Duplicate Elements

// const arr = [1, 2, 3, 2, 4, 5, 3, 6, 4];
// let dublicates=[]
// for (i=0;i<arr.length;i++){
//     for (j=i+1;j<arr.length;j++){
//         if(arr[i] === arr[j])
//             dublicates.push(arr[j])
//     }
// }
// console.log(dublicates)

// const s = "Tinkal kumar"
// let dublicates=""
// for (i=0;i<s.length;i++){
//     for (j=i+1;j<s.length;j++){
//         if(s[i] === s[j])
//             dublicates+=s[j]
//     }
// }
// console.log(dublicates)

// Find the Largest Number

// const arr = [5, 1220, 30];
// let max=arr[0]
// let smax=arr[1]
// for(i=0;i<arr.length;i++){
//     if(arr[i] > max){
//         smax=max
//         max=arr[i]
//     }else{
//         if(arr[i] < max && arr[i] > smax){
//             smax=arr[i]
//         }
//     }
// }
// console.log(max,smax)


// Sum of All Array Elements
// const arr = [10, 20, 30, 40, 50];
// let ts = 0
// for(i=0;i<arr.length;i++){
//     ts+=arr[i]
// }
// console.log(ts)

// Find Average of Array

// const arr = [10, 20, 30, 40, 50];
// let avs = 0
// let ts=0
// for(i=0;i<arr.length;i++){
//     ts+=arr[i]
// }
// avs=ts/arr.length
// console.log(avs)

// Find Common Elements

// const arr1 = [1, 2, 3, 4, 5];
// const arr2 = [3, 4, 5, 6, 7];

// let comman=[]
// for(i=0;i<arr1.length;i++){
//     for(j=0;j<arr2.length;j++){
//         if(arr1[i] === arr2[j]){
//             comman.push(arr1[i])
//         }
//     }
// }
// console.log(comman)

// Find Missing Number

// Find Missing Number

// const arr = [8, 1, 7, 2, 3, 5, 6];
// const n = arr.length+1
// const expected = n*(n+1)/2
// var total=0
// for(i=0;i<arr.length;i++){
//     total+=arr[i]
// }
// const m=expected-total
// console.log(m)

// Move Zeros to the End

// const arr = [5,0,0,0, 1, 0, 3, 0,12,4,0,0,5];
// let l=0

// for(i=0;i<arr.length;i++){
//     if(arr[i]!==0){
//         [arr[i],arr[l]]=[arr[l],arr[i]]
//         l+=1
//     }
// }
// console.log(arr)

// move 0 at begenning

// const arr = [5,0,0,0, 1, 0, 3, 0,12,4,0,0,5];
// let l=0
// for(i=0;i<arr.length;i++){
//     if(arr[i]==0){
//         [arr[i],arr[l]]=[arr[l],arr[i]]
//         l+=1
//     }
// }
// console.log(arr)

// Rotate Array Right by One Position

// let arr = [1, 2, 3, 4, 5];
// l=0
// r=arr.length-1
// t=arr[arr.length-1]
// arr.unshift(t)
// arr.pop()
// console.log(arr)

// Rotate Array Right by k Positions
// let arr = [1, 2, 3, 4, 5, 6, 7];
// let k = 3;

// k=k%arr.length

// function reverse(l,r,arr){
//     while(l<r){
//         [arr[l],arr[r]]=[arr[r],arr[l]]
//         r-=1
//         l+=1
//     }
// }

// reverse(0,arr.length-1,arr)
// reverse(0,k-1,arr)
// reverse(k,arr.length-1,arr)
// console.log(arr)

// Two Sum

// const arr = [8, 7, 11,2, 15];
// const target = 9;
// let c=0
// for(i=0;i<arr.length-1;i++){
//     for(j=i+1;j<arr.length;j++){
//         c=arr[i]+arr[j]
//         if(c === target){
//             console.log(arr[i],arr[j])
//             break;
//         }
//     }
// }

// Check Anagram js is cas sensative t and T is not same so first convert in owercase 

// const str1 = "tinkaal";
// const str2 = "Tinkall";

// let anagram = true
// let f={}
// if(str1.length != str2.length){
//     anagram = false
// }else{
    
//     for(i=0;i<str1.length;i++){
//         if(f[str1[i]]){
//             f[str1[i]]+=1
//         }else{
//             f[str1[i]]=1
//         }
//     }
//     for(i=0;i<str2.length;i++){
//          if(f[str2[i]]){
//             f[str2[i]]-=1
//         }else{
//            anagram=false
//            break
//         }
//     }
// }
// console.log(anagram)

// // Find Unique Elements

// let arr = [1,1, 2, 2, 3, 4, 4, 5, 6, 6];

// // let newarr= new Set(arr)
// // newarr=[...newarr]
// // console.log(newarr)
// let f={}
// let u=[]
// for (i=0;i<arr.length;i++){
//     if(!f[arr[i]]){
//         f[arr[i]]=true
//         u.push(arr[i])
//     }
// }
// console.log(u)

// Find the Longest and Shortest Word

// const str = "I love learning JavaScript programming";

// const words = str.split(" ");
// let longest = words[0];
// let shortest = words[0];

// for (let i = 1; i < words.length; i++) {
//     if (words[i].length > longest.length) {
//         longest = words[i];
//     }

//     if (words[i].length < shortest.length) {
//         shortest = words[i];
//     }
// }

// console.log("Longest:", longest);
// console.log("Shortest:", shortest);

// Capitalize the First Letter of Each Word

// const str = "i love learning javascript";

// const result = str
//     .split(" ")
//     .map(word => word.charAt(0).toUpperCase() + word.slice(1))
//     .join(" ");

// console.log(result);

// Maximum sum subarray — Kadane's algorithm

// const arr = [-2, 1, -3, 4, -1, 2, 1, -5, 4];

// let currentSum = arr[0];
// let maxSum = arr[0];

// for (let i = 1; i < arr.length; i++) {
//     currentSum = Math.max(arr[i], currentSum + arr[i]);
//     maxSum = Math.max(maxSum, currentSum);
// }

// console.log(maxSum);

// Maximum sum subarray of size k — Sliding Window

// const arr = [2, 1, 5, 1, 3, 2];
// const k = 3;

// let windowSum = 0;

// for (let i = 0; i < k; i++) {
//     windowSum += arr[i];
// }

// let maxSum = windowSum;

// for (let i = k; i < arr.length; i++) {
//     windowSum = windowSum + arr[i] - arr[i - k];
//     maxSum = Math.max(maxSum, windowSum);
// }

// console.log(maxSum);

// Longest substring without repeating characters

// function lengthOfLongestSubstring(str) {
//     let left = 0;
//     let maxLength = 0;
//     const lastSeen = new Map();

//     for (let right = 0; right < str.length; right++) {
//         const char = str[right];

//         if (lastSeen.has(char) && lastSeen.get(char) >= left) {
//             left = lastSeen.get(char) + 1;
//         }

//         lastSeen.set(char, right);
//         maxLength = Math.max(maxLength, right - left + 1);
//     }

//     return maxLength;
// }

// console.log(lengthOfLongestSubstring("abcabcbb"));

