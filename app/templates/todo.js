const inputs = document.getElementById('newlist');
const Lists = document.getElementById('list');

function addnewTask(){
    if(inputs.value != ''){
        let li = document.createElement("li");
        li.innerHTML = inputs.value;
        Lists.appendChild(li);
        let span = document.createElement("span");
        span.innerHTML = "\u00d7";
        li.appendChild(span);
    }
    else{
    alert("Invalid task!");
    }
    inputs.value = '';
}


Lists.addEventListener("click",function(e){
    if(e.target.tagName == "LI"){
        e.target.classList.toggle("checked");
    }
    else if(e.target.tagName == "SPAN"){
        e.target.parentElement.remove();
    }
}, false);
