// function calcularArea (base, altura) {
//     area = base * altura
//     console.log(`El area es: ${area}`)
// }

// calcularArea(12,2) 
// calcularArea(10,5)
// calcularArea(15,8)

// 1 1 2 3 5 8

// function fino(limite) {
//     let previous = 1
//     let current = 0
//     let aux = 0


//     for (let i = 0; i <= limite; i++) {
//         aux = current
//         current = previous + current
//         previous = aux

//         console.log(current)
//     }

//     // return current
// }

// //for (let i = 0; i < 6; i++) {
//     // console.log(fino(10));
//     fino(10)

// //}

// complete the solution so that it reverse the string passed into it

// function solution(str) {
//     // return str.split('').reverse().join('')

//     let reverse = ''
//     for (let i = str.length - 1; i >= 0; i--) {
//         reverse += str[i]
//     }
//     return reverse
// }

// function getCounts(str) {
//     const abc = ['a', 'e', 'i', 'o', 'u']
//     let count = 0

//     for (let i = 0; i < str.length; i++) {
//         if (abc.includes(str[i])) {
//             count++
//         }
//     }
//     console.log(count)
//     // return count
// }

// getCounts('hola mundo') // 4


// numero primo 1, 2, 3, 5, 7, 11, 13, 17, 19, 23, 29,...

function numeroPrimo(numero) {
    if (numero < 1 ) { return console.log('✖️ No es primo ', numero) }
    
    for (let i = 2; i < numero; i++) {
        if (numero % i === 0) { return console.log('✖️ No es primo ', numero)}
    }
    return console.log('🆗 Numero primo ', numero) 
    
}

for (let i = 1; i < 10; i++) { numeroPrimo([i])}



// function oddOrEven(array) {
//     let sum = 0
//     for (let i = 0; i < array.length; i++) {
//         sum += sum + array[i]
//     }
//     // return sum > 0 ? "odd" : "even"
//     console.log (sum % 2 == 0 ? "even" : "odd")
// }

// oddOrEven([0,-1,-5])