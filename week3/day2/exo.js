let favoritefood= "chocolate"  , favoritemail= "dinner" ;
console.log(`I eat ${favoritefood} every ${favoritefood}`);
let myWatchedSeries = ["black mirror", "money heist", "the big bang theory"];
let myWatchedSeriesLength = myWatchedSeries.length
let myWatchedSeriesSentence = "black mirror, money heist, and the big bang theory";
console.log(`I  watched ${myWatchedSeriesLength} series ${myWatchedSeries}`);
myWatchedSeries.splice(2,1,"friends");
myWatchedSeries.push("SUITS");
myWatchedSeries.unshift("VICKINGS");
myWatchedSeries.shift();
console.log(myWatchedSeries[1]);  
myWatchedSeries[1][3] ;

