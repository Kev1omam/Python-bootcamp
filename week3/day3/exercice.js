let age = prompt(); if (age>18){
  console.log("vous etes majeur")
} else {
  console.log('vous etes mineur')
};
// temperature de leau
let temperature = prompt(); if (temperature<0)
{console.log('solide')} else if ( temperature <= 100) 
{console.log('liquide')}
 else { if ( temperature >=100 )  console.log('gazeux')}

// controle de lage
 let age = prompt(); if (age<18){
  alert("Sorry, you are too young to drive this car.")
} else if( age=18 ) { alert('Congratulations on your first year of driving. Enjoy the ride')}
  else{ if ( age<18 ) alert('Powering On. Enjoy the ride!')}

  let fruit = 'Papayas';

switch (fruit) {
  case 'Oranges':
    console.log('Oranges are $0.59 a pound.');
    break;
  case 'Mangoes':
  case 'Papayas':
    console.log('Mangoes and papayas are $2.79 a pound.');
    // expected output: "Mangoes and papayas are $2.79 a pound."
    break;
  default:
    console.log('Sorry, we are out of ' + fruit + '.');}
// decelarer les objets 

    let person = {
      firstName: "John",
      lastName: "Doe",
      age: 50,
      eyeColor: "blue"
    };
    //afficher un element person['lastName']


    let a = 2 + 2;

switch (a) {
  case 3:
    alert( 'Too small' );
    break;
  case 4:
    alert( 'Exactly!' );
    break;
  case 5:
    alert( 'Too large' );
    break;
  default:
    alert( "I don't know such values" );
}
let a = 2 + 2;

switch (a) {
  case 4:
    alert('Right!');
    break;

  case 3: // (*) grouped two cases
  case 5:
    alert('Wrong!');
    alert("Why don't you take a math class?");
    break;

  default:
    alert('The result is strange. Really.');
}


// determine (condition) ? code : code ;
let age = prompt (); age>18 ? alert('majeur') : console.log('mineur');

// cree lobjet personne avec des propriete

let personne = {
  username:"",
  password:"",}

  // mettre dans un tableau

  let database = ["username", "password"];

  //
  let newsfeed = ["properties" , "username","timeline"];



  let newsfeed = [{
    unsername :'kevin',
    timeline :"",
  }
  {
    unsername :'kevin',
    timeline :"",


  }
   { 
    unsername :'kevin',
    timeline :"",
   }
];
// expressions regular

let str = "Happy BirthDay";
let patt = /birthday/i;
let result = str.match(patt);
console.log(result); //returns true

if (result){
    console.log('Yes')
} else{
    console.log('No');
}
