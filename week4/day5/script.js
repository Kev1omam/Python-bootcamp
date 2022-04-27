document.body.children[1]
document.body.children[1].children[0].nextElementSibling
document.body.children[1].lastElementChild
document.body.children[1].lastElementChild.innerText = "kevin"  

document.getElementById('container');
<div id=​"container">​Users:​</div>​
document.getElementsByClassName('list');


0: ul.list1: ul.listlength: 2[[Prototype]]: HTMLCollectionitem: ƒ item()length: (...)namedItem: ƒ namedItem()constructor: ƒ HTMLCollection()Symbol(Symbol.iterator): ƒ values()Symbol(Symbol.toStringTag): "HTMLCollection"get length: ƒ length()[[Prototype]]: Object
document.getElementsByClassName('list');
HTMLCollection(2) [ul.list, ul.list]
document.getElementsByClassName('list')[0];
<ul class=​"list">​<li>​::marker​"John"</li>​<li>​::marker​"Pete"</li>​</ul>​
document.getElementsByClassName('list')[0].firstElementChild;
<li>​::marker​"John"</li>​
document.getElementsByClassName('list')[0].firstElementChild.innerHTML;
'John'
document.getElementsByClassName('list')[1].firstElementChild.innerHTML;
'Sarah'