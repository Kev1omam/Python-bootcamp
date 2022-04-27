// question 1
let planete = ['Mercure', 'Venus', 'Terre', 'Mars', 'Jupiter', 'Saturne', 'Uranus', 'Neptune'];

// question 2

for (let index = 0; index < planete.length ; index++) {
  let Newdiv = document.createElement('div');
  Newdiv.classList.add('planet');
  Newdiv.textContent = planete[index];
  Newdiv.style.background = "red";
  let sec = document.body.getElementsByClassName('listPlanets')[0];
  sec.append(Newdiv);
  

 
}



 