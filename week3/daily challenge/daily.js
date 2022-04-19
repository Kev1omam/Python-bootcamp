let fruits = ["Banana", "Apples", "Oranges", "Blueberries"];
fruits.shift('Banane');
fruits.sort();
console.log("fruits");
fruits.push("Kiwi");
fruits.splice(0,1);
fruits.reverse();
console.log('fruits');
let moreFruits = ["Banana", ["Apples", ["Oranges"], "Blueberries"]];
console.log(moreFruits[1][1]);
  