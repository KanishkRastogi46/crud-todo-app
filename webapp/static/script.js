var input = document.querySelectorAll("input");

var newarr = Array.from(input);

// for adding blue border in input field while in focus
newarr.forEach((item)=>{
    item.addEventListener('focus', (event)=>{
        event.target.style.border = "4px solid blue";
        console.log(event.target.style);
    })

    item.addEventListener('blur', (event)=>{
        event.target.style.border = "";
        console.log(event.target.style);
    })
})



// for closing the flash messages after submitting the form
document.querySelectorAll("div.message-box").forEach((box)=>{
    let btn = box.lastElementChild;
    btn.addEventListener('click', ()=>{
        box.style.display = "none";
    })
})


function deleteTodo(id){
    let formData = {id:id};
    fetch("/delete-todo", {
        method : "POST",
        headers : {
            "Content-Type" : "application/json"
        },
        body : JSON.stringify(formData)
    }).then((res)=>{});
}