( let i = 0 ; i <= 15 ; i ++;) {if ( i%2 === 1 ) { console.log(`${i} + le " nombre est paire")} else { console.log(${i}))`} 
let names= ["john", "sarah", 23, "Rudolf",34]
  for (let  index of names) {

    if (typeof(index) !== 'string' ){
      continue;
    }else if (index[0]  !== index[0].toLocaleUpperCase()){
      index.replace(index[0], index[0].toLocaleUpperCase());
      console.log(index);

    }
  }
  for ( let index of names){


    if(typeof(index) !=="string"){
      break;
    }else {
      console,log(index);
    }
  }