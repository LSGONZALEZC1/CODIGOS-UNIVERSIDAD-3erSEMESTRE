let numbers = [];
var conteoQsASC = 0;
var performanceQsAsc;
var conteoQsDESC = 0;
var performanceQsDsc;
var conteoBurbleAsc = 0;
var performanceBurbleAsc;
var conteoBurbleDsc = 0;
var performanceBurbleDsc;
var conteoMergeAsc = 0;
var performanceMergeAsc;
var conteoMergeDsc = 1;
var performanceMergeDsc;
var conteoSelecAsc = 0;
var performanceSelecAsc;
var conteoSelecDsc = 0;
var performanceSelecDsc;
var conteoInser = 0;
var performanceInser;
var conteoInserDsc = 0;
var performanceInserDsc;
var conteoCounting = 0;
var performanceCounting;
var conteoCountingDsc = 0;
var performanceCountingDsc;
var conteoBurbleBD = 0;
var performanceBurbleBD;
var conteoBurbleBDDsc = 0;
var performanceBurbleBDDsc;
var conteoRadix = 0;
var performanceRadix;
var conteoRadixDsc = 0;
var performanceRadixDsc;
var conteoGnome = 0;
var performanceGnome;
var conteoGnomeDsc = 0;
var performanceGnomeDsc;

// Función para añadir numeros al arreglo
function addNumbersToArray() {
  numbers = [];
  min = Math.ceil(0);
  var max = 10 ** parseInt(document.getElementById("number").value);
  for (let i = 0; i < max; i++) {
    numbers.push(Math.floor(Math.random() * (max - min) + min));
  }
  document.getElementById("tamañoArreglo").innerHTML= "El tamaño del arreglo es de: "+max;
  return numbers;
}

//Calcular el tiempo de ejecución
function calculatePerformance(callback, string, number){
  let startTime = performance.now();
  let cb = callback();
  let endTime = performance.now();
  let time = (endTime-startTime)/1000
  if( number == 1){
    performanceQsAsc = time;
    document.getElementById(string).innerHTML = time + " segundos";
  }
  if( number == 2){
    performanceQsDsc = time;
    document.getElementById(string).innerHTML = time + " segundos";
  }
  if( number == 3){
    performanceBurbleAsc = time;
    document.getElementById(string).innerHTML = time + " segundos";
  }
  if( number == 4){
    performanceBurbleDsc = time;
    document.getElementById(string).innerHTML = time + " segundos";
  }
  if( number == 5){
    performanceMergeAsc = time;
    document.getElementById(string).innerHTML = time + " segundos";
  }
  if( number == 6){
    performanceMergeDsc = time;
    document.getElementById(string).innerHTML = time + " segundos";
  }
  if( number == 7){
    performanceSelecAsc = time;
    document.getElementById(string).innerHTML = time + " segundos";
  }
  if( number == 8){
    performanceSelecDsc = time;
    document.getElementById(string).innerHTML = time + " segundos";
  }
  if( number == 9){
    performanceInser = time;
    document.getElementById(string).innerHTML = time + " segundos";
  }
  if( number == 10){
    performanceInserDsc = time;
    document.getElementById(string).innerHTML = time + " segundos";
  }
  if( number == 11){
    performanceCounting = time;
    document.getElementById(string).innerHTML = time + " segundos";
  }
  if( number == 12){
    performanceCountingDsc = time;
    document.getElementById(string).innerHTML = time + " segundos";
  }
  if( number == 13){
    performanceBurbleBD = time;
    document.getElementById(string).innerHTML = time + " segundos";
  }
  if( number == 14){
    performanceBurbleBDDsc = time;
    document.getElementById(string).innerHTML = time + " segundos";
  }
  if( number == 15){
    performanceRadix = time;
    document.getElementById(string).innerHTML = time + " segundos";
  }
  if( number == 16){
    performanceRadixDsc = time;
    document.getElementById(string).innerHTML = time + " segundos";
  }
  if( number == 17){
    performanceGnome = time;
    document.getElementById(string).innerHTML = time + " segundos";
  }
  if( number == 18){
    performanceGnomeDsc = time;
    document.getElementById(string).innerHTML = time + " segundos";
  }
  return cb;
}

//QUICKSORT

function quickSortASC(array) {
  if (array.length <= 1) {
    return array;
  }
  
  var pivot = array[0];
  
  var left = [];
  var right = [];
  
  for (var i = 1; i < array.length; i++) {
    conteoQsASC++;
    array[i] < pivot ? left.push(array[i]) : right.push(array[i]);
  }

  return quickSortASC(left).concat(pivot, quickSortASC(right));
}

function quickSortDESC(array) {
  if (array.length <= 1) {
    return array;
  }
  
  var pivot = array[0];
  
  var left = [];
  var right = [];
  
  for (var i = 1; i < array.length; i++) {
    conteoQsDESC++;
    array[i] < pivot ? left.push(array[i]) : right.push(array[i]);
  }

  return quickSortDESC(right).concat(pivot, quickSortDESC(left));
}

function mostrarNums() {
  console.log(numbers);
  numbersSort = quickSortDESC(numbers);
  return (document.getElementById("sortResultQs1").innerHTML = numbers);
}

function sortAsc() {
  console.log(numbers);
  numbersSort = quickSortASC(numbers);
  return (document.getElementById("sortResultQs2").innerHTML = numbersSort + " <br> El número de iteraciones es "+conteoQsASC);
}

function sortDesc() {
  console.log(numbers);
  numbersSort = quickSortDESC(numbers);
  return (document.getElementById("sortResultQs3").innerHTML = numbersSort + " <br> El número de iteraciones es "+conteoQsDESC);
}

//BURBLE

function burbleAsc(array){
  let aux,a,b;
  for ( a = 1; a<array.length;a++){
    for( b = 0; b<(array.length-a);b++){
      if (array[b]>array[b+1]){
        conteoBurbleAsc++;
        aux = array[b];
        array[b] = array[b+1];
        array[b+1] = aux;
      }
    }
  }

  return array;
}

function burbleDsc(array){
  let aux,a,b;
  for ( a = 1; a<array.length;a++){
    for( b = 0; b<(array.length-a);b++){
      if (array[b]<array[b+1]){
        conteoBurbleDsc++;
        aux = array[b];
        array[b] = array[b+1];
        array[b+1] = aux;
      }
    }
  }

  return array;
}

function mostrarBurbleAsc() {
  console.log(numbers);
  let numbersBurble = burbleAsc(numbers);
  console.log(numbersBurble);
  return (document.getElementById("resultBurble1").innerHTML = numbersBurble + " <br> El número de iteraciones es "+conteoBurbleAsc);
}

function mostrarBurbleDsc() {
  console.log(numbers);
  let numbersBurble = burbleDsc(numbers);
  console.log(numbersBurble);
  return (document.getElementById("resultBurble2").innerHTML = numbersBurble + " <br> El número de iteraciones es "+conteoBurbleDsc);
}

// MERGESORT

function merge(left, right) {
  let arr = []
  while (left.length && right.length) {
    conteoMergeAsc++;
      if (left[0] < right[0]) {
        conteoMergeAsc++;
        arr.push(left.shift())  
      } else {
        conteoMergeAsc++;
        arr.push(right.shift()) 
      }
  }
  return [ ...arr, ...left, ...right ]
}

function mergeSort(array) {
  const half = array.length / 2
  
  if(array.length < 2){
    return array 
  }
  
  const left = array.splice(0, half)
  return merge(mergeSort(left),mergeSort(array))
}

function mergeDsc(left, right) {
  let arr = []
  while (left.length && right.length) {
    conteoMergeDsc++;
      if (left[0] < right[0]) {
        conteoMergeAsc++;
        arr.push(left.shift())  
      } else {
        conteoMergeAsc++;
        arr.push(right.shift()) 
      }
  }
  
  return [ ...right, ...left, ...arr ]
}

function mergeSortDsc(array) {
  const half = array.length / 2
  
  if(array.length < 2){
    return array 
  }
  
  const left = array.splice(0, half)
  return mergeDsc(mergeSortDsc(array),mergeSortDsc(left))
}

function mostrarMergeSort(){
  console.log(numbers);
  let numbersMerge = mergeSort(numbers);
  console.log(numbersMerge);
  return (document.getElementById("resultMerge1").innerHTML = numbersMerge+ " <br> El número de iteraciones es "+conteoMergeAsc);
}

function mostrarMergeSortDsc(){
  console.log(numbers);
  let numbersMergeDsc = mergeSortDsc(numbers);
  console.log(numbersMergeDsc);
  return (document.getElementById("resultMerge2").innerHTML = numbersMergeDsc+ " <br> El número de iteraciones es "+conteoMergeDsc);
}



//SELECTION

function selectionSort(arr) { 
  let n = arr.length;
      
  for(let i = 0; i < n; i++) {
    let min = i;
    for(let j = i+1; j < n; j++){
      if(arr[j] < arr[min]) {
        min=j; 
      }
    }
    if (min != i) {
      conteoSelecAsc++;
      let tmp = arr[i]; 
      arr[i] = arr[min];
      arr[min] = tmp;      
    }
  }
  return arr;
}

function selectionSortDsc(arr) { 
  let n = arr.length;
      
  for(let i = 0; i < n; i++) {
    let min = i;
    for(let j = i+1; j < n; j++){
      if(arr[j] > arr[min]) {
        min=j; 
      }
    }
    if (min != i) {
      conteoSelecDsc++;
      let tmp = arr[i]; 
      arr[i] = arr[min];
      arr[min] = tmp;      
    }
  }
  return arr;
}

function mostrarSelectionSort(){
  console.log(numbers);
  let numbersSelection = selectionSort(numbers);
  console.log(numbersSelection);
  return (document.getElementById("resultSelec1").innerHTML = numbersSelection+" <br> El número de iteraciones es "+conteoSelecAsc);
}

function mostrarSelectionSortDsc(){
  console.log(numbers);
  let numbersSelection2 = selectionSortDsc(numbers);
  console.log(numbersSelection2);
  return (document.getElementById("resultSelec2").innerHTML = numbersSelection2 +" <br> El número de iteraciones es " +conteoSelecDsc)
}

//INSERTION

function insertionSort(array) {
  for (let i = 0; i < array.length ; i++){
    for (let j = i; j>0 && array[j]<array[j-1]; j--){
      conteoInser++;
      [array[j],array[j-1]] = [array[j-1],array[j]];
    }
  }
  return array;
}

function insertionSortDsc(array) {
  for (let i = 0; i < array.length ; i++){
    for (let j = i; j>0 && array[j]>array[j-1]; j--){
      conteoInserDsc++;
      [array[j],array[j-1]] = [array[j-1],array[j]];
    }
  }
  return array;
}

function mostrarInser(){
  console.log(numbers);
  let numbersInser = insertionSort(numbers);
  console.log(numbersInser);
  return (document.getElementById("resultInser1").innerHTML = numbersInser +" <br> El número de iteraciones es " + conteoInser)
}

function mostrarInserDsc(){
  console.log(numbers);
  let numbersInser2 = insertionSortDsc(numbers);
  console.log(numbersInser2);
  return (document.getElementById("resultInser2").innerHTML = numbersInser2 +" <br> El número de iteraciones es " + conteoInserDsc)
}

//COUNTING
function countingSort(arr){
  if(arr.length < 2) return arr;
  let maxValue = arr[0];
  for (let i=1;i<arr.length;i++){
    if(arr[i] > maxValue){
      maxValue = arr[i];
    }
  }
  const countingArray = new Array(maxValue+1);
  for (let value of arr){
    if(!countingArray[value]){
      countingArray[value] = 0;
    }
    countingArray[value]++;
  }
  const resultArray = [];
  for(let i = 0;i<countingArray.length;i++){
    conteoCounting++;
    while(countingArray[i]>0){
      resultArray.push(i);
      countingArray[i]--;
    }
  }
  return resultArray
}

function countingSortDsc(arr){
  if(arr.length < 2) return arr;
  let maxValue = arr[0];
  for (let i=1;i<arr.length;i++){
    if(arr[i] > maxValue){
      maxValue = arr[i];
    }
  }
  const countingArray = new Array(maxValue+1);
  for (let value of arr){
    if(!countingArray[value]){
      countingArray[value] = 0;
    }
    countingArray[value]++;
  }
  const resultArray = [];
  for(let i = countingArray.length;i>=0;i--){
    conteoCountingDsc++;
    while(countingArray[i]>0){
      resultArray.push(i);
      countingArray[i]--;
    }
  }
  return resultArray
}

function mostrarCounting(){
  console.log(numbers);
  let numbersCounting = countingSort(numbers);
  console.log(numbersCounting);
  return (document.getElementById("resultCounting1").innerHTML = numbersCounting +" <br> El número de iteraciones es "+conteoCounting)
}

function mostrarCountingDsc(){
  console.log(numbers);
  let numbersCountingDsc = countingSortDsc(numbers);
  console.log(numbersCountingDsc);
  return (document.getElementById("resultCounting2").innerHTML = numbersCountingDsc +" <br> El número de iteraciones es "+conteoCountingDsc)
}

//BurbleBD

function BurbleBD(array){

  let izq = 0, der = array.length-1, aux, ultimo = array.length-1;
  do{
    for (let i = izq; i< der;i++){
      if(array[i]>array[i+1]){
        conteoBurbleBD++;
        aux = array[i];
        array[i] = array[i+1];
        array[i+1] = aux;
        ultimo = i;
      }
    }
    der = ultimo;
    
    for (let j = der; j>izq;j--){
      if(array[j-1]>array[j]){
        conteoBurbleBD++;
        aux = array[j];
        array[j] = array[j-1];
        array[j-1] = aux;
        ultimo = j;
      }
    }

    izq = ultimo;
  }while(izq<der);

  return array
}

function BurbleBDDsc(array){
  let izq = 0, der = array.length-1, aux, ultimo = array.length-1;
  do{
    for (let i = izq; i< der;i++){
      if(array[i]<array[i+1]){
        conteoBurbleBDDsc++;
        aux = array[i];
        array[i] = array[i+1];
        array[i+1] = aux;
        ultimo = i;
      }
    }
    der = ultimo;
    
    for (let j = der; j>izq;j--){
      if(array[j-1]<array[j]){
        conteoBurbleBDDsc++;
        aux = array[j];
        array[j] = array[j-1];
        array[j-1] = aux;
        ultimo = j;
      }
    }

    izq = ultimo;
  }while(izq<der);

  return array
}

function mostrarBurbleBD(){
  console.log(numbers);
  let numbersBurbleBD = BurbleBD(numbers);
  console.log(numbersBurbleBD);
  return (document.getElementById("resultBurbleBD1").innerHTML = numbersBurbleBD +" <br> El número de iteraciones es "+conteoBurbleBD)
}

function mostrarBurbleBDDsc(){
  console.log(numbers);
  let numbersBurbleBDDsc = BurbleBDDsc(numbers);
  console.log(numbersBurbleBDDsc);
  return (document.getElementById("resultBurbleBD2").innerHTML = numbersBurbleBDDsc +" <br> El número de iteraciones es "+conteoBurbleBDDsc)
}

//RADIX SORT

function RadixSort(array){
  let n = array.length;
  let maximo = array[0];
  let digitos = 1;
  let matrizAux = [];
  for (let i = 0; i < n; i++) {
    if (array[i] > maximo) {
      maximo = array[i];
    }
  }
  while ((maximo / digitos) > 1) {
    for (let i = 0; i < 10; i++) {
      matrizAux.push([]);
    }
    for (let i = 0; i < n; i++) {
      let indice = parseInt(array[i] / digitos) % 10;
      matrizAux[indice].push(array[i]);
      conteoRadix++;
    }
    let index = 0;
    for (let i = 0; i < 10; i++) {
      let aux = matrizAux[i];
      for (let j = 0; j < aux.length; j++) {
        array[index] = aux[j];
        index++;
      }
    }
    matrizAux = [];
    digitos *= 10;
  }
  return array;
}


let iteraciones = 0;
function radixSort(lista) {
    
    let n = 0;
    for (let e of lista) {
      if (e.length > n) {
        n = e.length;
      }
      
    }
  
    for (let i = 0; i < lista.length; i++) {
      while (lista[i].length < n) {
        lista[i] = "0" + lista[i];
      }
    }
  
    for (let j = n - 1; j >= 0; j--) {
      let grupos = Array.from({ length: 10 }, () => []);
  
      for (let i = 0; i < lista.length; i++) {
        // 9 - para volverla descendente
        grupos[ 9 - parseInt(lista[i][j])].push(lista[i]);
        iteraciones++;
      }
  
      lista = [].concat(...grupos);
    }
  
    return lista.map(Number);
}
  
  
function mostrarRadixSort(){
  console.log(numbers);
  let numbersRadix = RadixSort(numbers);
  console.log(numbersRadix);
  return (document.getElementById("resultRadix1").innerHTML = numbersRadix +" <br> El número de iteraciones es "+conteoRadix)
}

function mostrarRadixSortDsc() {
    let lista = Array.from({ length: 100 }, () => String(Math.floor(Math.random() * 100)));
  
    let numbersRadixSortDsc = radixSort(lista);
    return (document.getElementById("resultRadixSort2").innerHTML = numbersRadixSortDsc +" <br> El número de iteraciones es "+iteraciones);
}

//Gnome
function GnomeSort(array){
  let i = 0, size = array.length;
  while (i < size) {
    if (i == 0) i++;
    if (array[i] >= array[i - 1]) i++;
    else {
      conteoGnome++;
      let temp = array[i];
      array[i] = array[i - 1];
      array[--i] = temp;
    }
  }
  return array;
}

function GnomeSortDsc(array){
  let i = 0, size = array.length;
  while (i < size) {
    if (i == 0) i++;
    if (array[i] >= array[i - 1]) i++;
    else {
      conteoGnome++;
      let temp = array[i];
      array[i] = array[i - 1];
      array[--i] = temp;
    }
  }
  return array;
}
  
function mostrarGnomeSort(){
  console.log(numbers);
  let numbersGnomeSort = GnomeSort(numbers);
  console.log(numbersGnomeSort);
  return (document.getElementById("resultGnomeSort").innerHTML = numbersGnomeSort +" <br> El número de iteraciones es "+conteoGnome)
}

function mostrarGnomeSortdes(){
    console.log(numbers);
    let numbersGnomeSort = GnomeSortDsc(numbers);
    console.log(numbersGnomeSort);
  return (document.getElementById("resultGnomeSort-1").innerHTML = numbersGnomeSort +" <br> El número de iteraciones es "+conteoGnomeDsc)
}

//Grafica
function verGrafica(){
  const ctx = document.getElementById('myChart')
  const ctx2 = document.getElementById('myChart2')
  const digitos = ["10^1",'10^2','10^3','10^4','10^5','10^6','10^7']
  // const iteracionesAsc = [conteoQsASC, conteoBurbleAsc, 712, conteoSelecAsc, conteoInser, conteoCounting,conteoBurbleBD,conteoRadix,conteoGnome]
  // const iteracionesDsc = [conteoQsDESC, conteoBurbleDsc, 331, conteoSelecDsc, conteoInserDsc, performanceCountingDsc,conteoBurbleBDDsc,iteraciones,conteoGnomeDsc]
  // const segundosAsc = [performanceQsAsc, performanceBurbleAsc, 0.0060999999046325686, performanceSelecAsc, performanceInser, performanceCounting,performanceBurbleBD,performanceRadix,performanceGnome]
  // const segundosDsc = [performanceQsDsc, performanceBurbleDsc, 0.006200000047683716, performanceSelecDsc, performanceInserDsc, 0.003,performanceBurbleBDDsc,performanceRadixDsc,performanceGnomeDsc]
  const QsIteracionesAsc = [23, 585, 10504, 159551, 2008736, 24767443,293128078]
  const QsTempAsc = [0.0025, 0.0032, 0.0221, 0.0893, 0.4231, 1.7,19.1] 
  const QsIteracionesDsc = [27,667,10998,158123,2064603,24822930,308122891]
  const QsTempDsc = [0.0017,0.0041,0.0233,0.0949,0.413,1.0497,13.141] 
  const BurbleIteracionesAsc = [28,2385,248312,1850000,1008114]
  const BurbleTempAsc = [0.0023,0.0026,0.0051,0.2195,0.7209] 
  const BurbleIteracionesDsc = [14,0.0026,498974,49989989]
  const BurbleTempDsc = [0.0024,0.0045,0.0107,0.1511]
  const MergeIteracionesAsc = [50,1142,17388,241078,3314110]
  const MergeTempAsc = [0.002,0.001,0.0161,0.0451,2.1343]
  const MergeIteracionesDsc = [18,330,4977,66285,829096]
  const MergeTempDsc = [0.0018,0.0051,0.0137,0.0286,0.9021]
  const SelecIteracionesAsc = [7,98,989,9988,99987]
  const SelecTempAsc = [0.0006,0.0039,0.0065,0.0906,6.9884]
  const SelecIteracionesDsc = [6,59,597,6107,61471]
  const SelecTempDsc = [0.0006,0.002,0.0046,0.1476,15.5261]
  const InseIteracionesAsc = [21,2324,249678,25001722,2499800321]
  const InserTempAsc = [0.0005,0.0035,0.012,0.159,30.1]
  const InserIteracionesDsc = [38,4894,498992,49990085,12399800321]
  const InserTempDsc = [0.0008,0.004,0.0107,0.2544,32]
  const countingIteracionesAsc = [10,99,986,99999,984300]
  const countingTempAsc = [0.003,0.0045,0.0035,0.0245,0.0457]
  const countingIteracionesDsc = [10,100,987,3500,10000,30000,120000]
  const countingTempDsc = [0.0022,0.0018,0.0040,0.0245,0.0376,0.3345,4.2546]
  const burbleBDIteracionesAsc = [13,2379,251815,25212590,2499946676]
  const burbleBDTempAsc = [0.0009,0.0044,0.0188,0.28,51.1]
  const burbleBDIteracionesDsc = [36,4912,499001,49989906,2502707778]
  const burbleBDTempDsc = [0.0006,0.0056,0.0132,0.2173,52.638]
  const radixIteracionesAsc = [10,200,3000,40000,500000,6000000]
  const radixTempAsc = [0.0033,0.0028,0.0094,0.08,0.2065,1.3]
  const gnomeIteracionesAsc = [12,2271,244766,24668491,2506185954]
  const gnomeTempAsc = [0.0034,0.0051,0.0279,0.4383,71.2235]
  const gnomeIteracionesDsc = [19,2271,244766,44668491,5506185954]
  const gnomeTempDsc = [0.001,0.0051,0.028,0.5383,81.2235]

  const myChart = new Chart(ctx, {
      type: 'line',
      data: {
          labels: digitos,
          datasets: [{
              label:'QuickSort',
              data: QsIteracionesAsc,
              backgroundColor: [
                  'rgba(159, 122, 74, 0.6)'
              ],
              borderColor: [
                  'rgba(159, 122, 74, 0.6)'
              ],
              borderWidth: 1.5
          },{
            label:'QuickSortDsc',
            data: QsIteracionesDsc,
            backgroundColor: [
                'rgba(81, 116, 104, 0.9)'
            ],
            borderColor: [
                'rgba(81, 116, 104, 0.9)'
            ],
            borderWidth: 1.5
          },{
            label:'BurbleSort',
            data: BurbleIteracionesAsc,
            backgroundColor: [
                'rgba(169, 54, 134, 0.2)'
            ],
            borderColor: [
                'rgba(169, 54, 134, 0.2)'
            ],
            borderWidth: 1.5
          },{
            label:'BurbleSortDsc',
            data: BurbleIteracionesDsc,
            backgroundColor: [
                'rgba(24, 40, 195, 0.4)'
            ],
            borderColor: [
                'rgba(24, 40, 195, 0.4)'
            ],
            borderWidth: 1.5
          },{
              label:'MergeSort',
              data: MergeIteracionesAsc,
              backgroundColor: [
                  'rgba(104, 45, 56, 0.1)'
              ],
              borderColor: [
                  'rgba(104, 45, 56, 0.1)'
              ],
              borderWidth: 1.5
            },{
                label:'MergeSortDsc',
                data: MergeIteracionesDsc,
                backgroundColor: [
                    'rgba(154, 37, 127, 0.2)'
                ],
                borderColor: [
                    'rgba(154, 37, 127, 0.2)'
                ],
                borderWidth: 1.5
              },{
                  label:'SelectionSort',
                  data: SelecIteracionesAsc,
                  backgroundColor: [
                      'rgba(144, 50, 246, 1)'
                  ],
                  borderColor: [
                      'rgba(144, 50, 246, 1)'
                  ],
                  borderWidth: 1.5
                },{
                    label:'SelectionSortDsc',
                    data: SelecIteracionesDsc,
                    backgroundColor: [
                        'rgba(32, 83, 4, 0.2)'
                    ],
                    borderColor: [
                        'rgba(32, 83, 4, 0.2)'
                    ],
                    borderWidth: 1.5
                  },{
                      label:'insertionSort',
                      data: InseIteracionesAsc,
                      backgroundColor: [
                          'rgba(235, 28, 177, 0.3)'
                      ],
                      borderColor: [
                          'rgba(235, 28, 177, 0.3)'
                      ],
                      borderWidth: 1.5
                    },{
                        label:'InsertionSortDsc',
                        data: InserIteracionesDsc,
                        backgroundColor: [
                            'rgba(214, 56, 202, 0.3)'
                        ],
                        borderColor: [
                            'rgba(214, 56, 202, 0.3)'
                        ],
                        borderWidth: 1.5
                      },{
                          label:'countingSort',
                          data: countingIteracionesAsc,
                          backgroundColor: [
                              'rgba(242, 142, 168, 0.4)'
                          ],
                          borderColor: [
                              'rgba(242, 142, 168, 0.4)'
                          ],
                          borderWidth: 1.5
                        },{
                            label:'countingSortDsc',
                            data: countingIteracionesDsc,
                            backgroundColor: [
                                'rgba(184, 74, 50, 0.7)'
                            ],
                            borderColor: [
                                'rgba(184, 74, 50, 0.7)'
                            ],
                            borderWidth: 1.5
                          },{
                              label:'Burble BD',
                              data: burbleBDIteracionesAsc,
                              backgroundColor: [
                                  'rgba(97, 136, 177, 0.5)'
                              ],
                              borderColor: [
                                  'rgba(97, 136, 177, 0.5)'
                              ],
                              borderWidth: 1.5
                            },{
                                label:'BuerbleBdDsc',
                                data: burbleBDIteracionesDsc,
                                backgroundColor: [
                                    'rgba(128, 14, 113, 0.6)'
                                ],
                                borderColor: [
                                    'rgba(128, 14, 113, 0.6)'
                                ],
                                borderWidth: 1.5
                              },{
                                  label:'Radix',
                                  data: radixIteracionesAsc,
                                  backgroundColor: [
                                      'rgba(147, 207, 82, 1)'
                                  ],
                                  borderColor: [
                                      'rgba(147, 207, 82, 1)'
                                  ],
                                  borderWidth: 1.5
                                },{
                                    label:'gnome',
                                    data: gnomeIteracionesAsc,
                                    backgroundColor: [
                                        'rgba(97, 247, 115, 0.9)'
                                    ],
                                    borderColor: [
                                        'rgba(97, 247, 115, 0.9)'
                                    ],
                                    borderWidth: 1.5
                                  },{
                                      label:'gnomeDsc',
                                      data: gnomeIteracionesDsc,
                                      backgroundColor: [
                                          'rgba(50, 26, 41, 0.6)'
                                      ],
                                      borderColor: [
                                          'rgba(50, 26, 41, 0.6)'
                                      ],
                                      borderWidth: 1.5
                                    }]

          
      },
      options:{
          events: ['mousemove', 'mouseout', 'click', 'touchstart', 'touchmove'],
          plugins:{
              tooltip: {
                  // Tooltip will only receive click events
                  events: ['click']
                },
              subtitle:{
                  display: true,
                  text: 'Iteraciones'
              }
          }
      }
    
  });

  const myChart2 = new Chart(ctx2, {
      type: 'line',
      data: {
          labels: digitos,
          datasets: [{
            label:'QuickSort',
            data: QsTempAsc,
            backgroundColor: [
                'rgba(159, 122, 74, 0.6)'
            ],
            borderColor: [
                'rgba(159, 122, 74, 0.6)'
            ],
            borderWidth: 1.5
        },{
          label:'QuickSortDsc',
          data: QsTempDsc,
          backgroundColor: [
              'rgba(81, 116, 104, 0.9)'
          ],
          borderColor: [
              'rgba(81, 116, 104, 0.9)'
          ],
          borderWidth: 1.5
        },{
          label:'BurbleSort',
          data: BurbleTempAsc,
          backgroundColor: [
              'rgba(169, 54, 134, 0.2)'
          ],
          borderColor: [
              'rgba(169, 54, 134, 0.2)'
          ],
          borderWidth: 1.5
        },{
          label:'BurbleSortDsc',
          data: BurbleTempDsc,
          backgroundColor: [
              'rgba(24, 40, 195, 0.4)'
          ],
          borderColor: [
              'rgba(24, 40, 195, 0.4)'
          ],
          borderWidth: 1.5
        },{
            label:'MergeSort',
            data: MergeTempAsc,
            backgroundColor: [
                'rgba(104, 45, 56, 0.1)'
            ],
            borderColor: [
                'rgba(104, 45, 56, 0.1)'
            ],
            borderWidth: 1.5
          },{
              label:'MergeSortDsc',
              data: MergeTempDsc,
              backgroundColor: [
                  'rgba(154, 37, 127, 0.2)'
              ],
              borderColor: [
                  'rgba(154, 37, 127, 0.2)'
              ],
              borderWidth: 1.5
            },{
                label:'SelectionSort',
                data: SelecTempAsc,
                backgroundColor: [
                    'rgba(144, 50, 246, 1)'
                ],
                borderColor: [
                    'rgba(144, 50, 246, 1)'
                ],
                borderWidth: 1.5
              },{
                  label:'SelectionSortDsc',
                  data: SelecTempDsc,
                  backgroundColor: [
                      'rgba(32, 83, 4, 0.2)'
                  ],
                  borderColor: [
                      'rgba(32, 83, 4, 0.2)'
                  ],
                  borderWidth: 1.5
                },{
                    label:'insertionSort',
                    data: InserTempAsc,
                    backgroundColor: [
                        'rgba(235, 28, 177, 0.3)'
                    ],
                    borderColor: [
                        'rgba(235, 28, 177, 0.3)'
                    ],
                    borderWidth: 1.5
                  },{
                      label:'InsertionSortDsc',
                      data: InserTempDsc,
                      backgroundColor: [
                          'rgba(214, 56, 202, 0.3)'
                      ],
                      borderColor: [
                          'rgba(214, 56, 202, 0.3)'
                      ],
                      borderWidth: 1.5
                    },{
                        label:'countingSort',
                        data: countingTempAsc,
                        backgroundColor: [
                            'rgba(242, 142, 168, 0.4)'
                        ],
                        borderColor: [
                            'rgba(242, 142, 168, 0.4)'
                        ],
                        borderWidth: 1.5
                      },{
                          label:'countingSortDsc',
                          data: countingTempDsc,
                          backgroundColor: [
                              'rgba(184, 74, 50, 0.7)'
                          ],
                          borderColor: [
                              'rgba(184, 74, 50, 0.7)'
                          ],
                          borderWidth: 1.5
                        },{
                            label:'Burble BD',
                            data: burbleBDTempAsc,
                            backgroundColor: [
                                'rgba(97, 136, 177, 0.5)'
                            ],
                            borderColor: [
                                'rgba(97, 136, 177, 0.5)'
                            ],
                            borderWidth: 1.5
                          },{
                              label:'BuerbleBdDsc',
                              data: burbleBDTempDsc,
                              backgroundColor: [
                                  'rgba(128, 14, 113, 0.6)'
                              ],
                              borderColor: [
                                  'rgba(128, 14, 113, 0.6)'
                              ],
                              borderWidth: 1.5
                            },{
                                label:'Radix',
                                data: radixTempAsc,
                                backgroundColor: [
                                    'rgba(147, 207, 82, 1)'
                                ],
                                borderColor: [
                                    'rgba(147, 207, 82, 1)'
                                ],
                                borderWidth: 1.5
                              },{
                                  label:'gnome',
                                  data: gnomeTempAsc,
                                  backgroundColor: [
                                      'rgba(97, 247, 115, 0.9)'
                                  ],
                                  borderColor: [
                                      'rgba(97, 247, 115, 0.9)'
                                  ],
                                  borderWidth: 1.5
                                },{
                                    label:'gnomeDsc',
                                    data: gnomeTempDsc,
                                    backgroundColor: [
                                        'rgba(50, 26, 41, 0.6)'
                                    ],
                                    borderColor: [
                                        'rgba(50, 26, 41, 0.6)'
                                    ],
                                    borderWidth: 1.5
                                  }]


          
      },
      options:{
          events: ['mousemove', 'mouseout', 'click', 'touchstart', 'touchmove'],
          plugins:{
              tooltip: {
                  // Tooltip will only receive click events
                  events: ['click']
                },
              subtitle:{
                  display: true,
                  text: 'Tiempo'
              }
          }
      }
    
  });
}