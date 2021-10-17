let root = document.querySelector(selector:'#root')
let header = document.createElement(tagName: 'h1')
    header =.innerHTML ='Hello Stas'
    root.append(header)

   console.log(root)


let users = fetch(input:'')
.then (response=>response.json())
.then (user=>header.innerHTML=user.name)

let form_ok = document.querySelector(selector:'#form_ok')
form_ok.addEventListener(type:'click')